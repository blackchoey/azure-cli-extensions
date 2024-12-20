# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from azure.cli.testsdk import ScenarioTest, ResourceGroupPreparer
from .utils import ApicServicePreparer, ApimServicePreparer
from .constants import TEST_REGION, USERASSIGNED_IDENTITY

# if USERASSIGNED_IDENTITY is set, enable_system_assigned_identity is False, otherwise use system assigned identity
enable_system_assigned_identity = False if USERASSIGNED_IDENTITY else True

class IntegrationCommandTests(ScenarioTest):
    # TODO: change the location to TEST_REGION when the APIC resource provider is available in all regions
    @ResourceGroupPreparer(name_prefix="clirg", location="centraluseuap", random_name_length=32)
    @ApicServicePreparer(enable_system_assigned_identity=enable_system_assigned_identity)
    @ApimServicePreparer(enable_system_assigned_identity=enable_system_assigned_identity)
    def test_integration_create_apim(self):
        # prepare test data
        self.kwargs.update({
          'integration_name': self.create_random_name(prefix='cli', length=8)
        })

        if enable_system_assigned_identity:
            self.cmd('az apic integration create apim -g {rg} -n {s} --azure-apim {apim_name} -i {integration_name}')
        else:
            # TODO: ugly codes, need to find a better way to handle this
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
        # TODO: add more checks, e.g. status, etc.
        self.cmd('az apic integration list -g {rg} -n {s}', checks=[
            self.check('length(@)', 1),
            self.check('@[0].apiSourceType', 'AzureApiManagement'),
            self.check('@[0].name', '{integration_name}')
        ])
