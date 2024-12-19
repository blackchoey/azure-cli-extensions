# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from azure.cli.testsdk import ScenarioTest, ResourceGroupPreparer
from .utils import ApicServicePreparer
from .constants import TEST_REGION, USERASSIGNED_IDENTITY

# TODO: remove this when the APIC resource provider is available in all regions
USERASSIGNED_IDENTITY = "{/subscriptions/b72ba90c-17fc-4d42-a890-2de38220b1a9/resourceGroups/rg-apic-extension-cli-test/providers/Microsoft.ManagedIdentity/userAssignedIdentities/apic-extension-cli-test}"

# if USERASSIGNED_IDENTITY is set, enable_system_assigned_identity is False, otherwise use system assigned identity
enable_system_assigned_identity = False if USERASSIGNED_IDENTITY else True

class IntegrationCommandTests(ScenarioTest):
    # TODO: change the location to TEST_REGION when the APIC resource provider is available in all regions
    @ResourceGroupPreparer(name_prefix="clirg", location="centraluseuap", random_name_length=32)
    @ApicServicePreparer()
    def test_integration_create_apim(self):
        # prepare test data
        self.kwargs.update({
          'apim_name': self.create_random_name(prefix='cli', length=12),
          'integration_name': self.create_random_name(prefix='cli', length=8)
        })
        self._prepare_apim()

        import re
        self.kwargs.update({
            # remove curly braces from usi_id
            'usi_id': re.sub(r'^\{|\}$', '', self.kwargs['usi_id'])
        })
        self.cmd('az apic integration create apim -g {rg} -n {s} --azure-apim {apim_name} -i {integration_name} --msi-resource-id "{usi_id}"')
        self.kwargs.update({
            # add curly braces to usi_id
            'usi_id': f"{{{self.kwargs['usi_id']}}}"
        })

        # verify command results
        self.cmd('az apic integration list -g {rg} -n {s}', checks=[
            self.check('length(@)', 1),
            self.check('@[0].apiSourceType', 'AzureApiManagement'),
            self.check('@[0].name', '{integration_name}')
        ])

    def _prepare_apim(self):
        if self.is_live:
            # Only setup APIM in live mode
            # Get system assigned identity id for API Center
            apic_service = self.cmd('az apic show -g {rg} -n {s}').get_output_in_json()
            self.kwargs.update({
                'identity_id': apic_service['identity']['principalId']
            }) if enable_system_assigned_identity else None
            # Create APIM service
            apim_service = self.cmd('az apim create -g {rg} --name {apim_name} --publisher-name test --publisher-email test@example.com --sku-name Consumption').get_output_in_json()
            # Add echo api
            self.cmd('az apim api create -g {rg} --service-name {apim_name} --api-id echo --display-name "Echo API" --path "/echo"')
            self.cmd('az apim api operation create -g {rg} --service-name {apim_name} --api-id echo --url-template "/echo" --method "GET" --display-name "GetOperation"')
            # Add foo api
            self.cmd('az apim api create -g {rg} --service-name {apim_name} --api-id foo --display-name "Foo API" --path "/foo"')
            self.cmd('az apim api operation create -g {rg} --service-name {apim_name} --api-id foo --url-template "/foo" --method "GET" --display-name "GetOperation"')
            apim_id = apim_service['id']
            self.kwargs.update({
                'apim_id': apim_id,
                'usi_id': USERASSIGNED_IDENTITY
            })

            if enable_system_assigned_identity:
                # Grant system assigned identity of API Center access to APIM
                self.cmd('az role assignment create --role "API Management Service Reader Role" --assignee-object-id {identity_id} --assignee-principal-type ServicePrincipal --scope {apim_id}')
            else:
                # add user-assigned identity to api center service:
                self.cmd('az apic update --name {s} -g {rg} --identity {{type:UserAssigned,user-assigned-identities:{usi_id}}}')
