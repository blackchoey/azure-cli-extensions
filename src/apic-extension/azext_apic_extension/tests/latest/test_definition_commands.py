# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from azure.cli.testsdk import ScenarioTest, ResourceGroupPreparer
from .utils import ApicServicePreparer, ApicApiPreparer, ApicVersionPreparer, ApicDefinitionPreparer

class VersionCommandsTests(ScenarioTest):

    @ResourceGroupPreparer(name_prefix="clirg", location='eastus', random_name_length=32)
    @ApicServicePreparer()
    @ApicApiPreparer()
    @ApicVersionPreparer()
    def test_definition_create(self):
        self.kwargs.update({
          'name': self.create_random_name(prefix='cli', length=24)
        })
        self.cmd('az apic api definition create -g {rg} -s {s} --api-id {api} --version-id {v} --definition-id {name} --title "OpenAPI"', checks=[
            self.check('name', '{name}'),
            self.check('title', 'OpenAPI'),
        ])

    @ResourceGroupPreparer(name_prefix="clirg", location='eastus', random_name_length=32)
    @ApicServicePreparer()
    @ApicApiPreparer()
    @ApicVersionPreparer()
    @ApicDefinitionPreparer()
    def test_definition_show(self):
        self.cmd('az apic api definition show -g {rg} -s {s} --api-id {api} --version-id {v} --definition-id {d}', checks=[
            self.check('name', '{d}'),
            self.check('title', 'OpenAPI'),
        ])

    @ResourceGroupPreparer(name_prefix="clirg", location='eastus', random_name_length=32)
    @ApicServicePreparer()
    @ApicApiPreparer()
    @ApicVersionPreparer()
    @ApicDefinitionPreparer(parameter_name="definition_id1")
    @ApicDefinitionPreparer(parameter_name="definition_id2")
    def test_definition_list(self, definition_id1, definition_id2):
        self.cmd('az apic api definition list -g {rg} -s {s} --api-id {api} --version-id {v}', checks=[
            self.check('length(@)', 2),
            self.check('[0].name', definition_id1),
            self.check('[1].name', definition_id2),
        ])

    @ResourceGroupPreparer(name_prefix="clirg", location='eastus', random_name_length=32)
    @ApicServicePreparer()
    @ApicApiPreparer()
    @ApicVersionPreparer()
    @ApicDefinitionPreparer()
    def test_definition_update(self):
        self.cmd('az apic api definition update -g {rg} -s {s} --api-id {api} --version-id {v} --definition-id {d} --title "Swagger"', checks=[
            self.check('name', '{d}'),
            self.check('title', 'Swagger'),
        ])

    @ResourceGroupPreparer(name_prefix="clirg", location='eastus', random_name_length=32)
    @ApicServicePreparer()
    @ApicApiPreparer()
    @ApicVersionPreparer()
    @ApicDefinitionPreparer()
    def test_definition_delete(self):
        self.cmd('az apic api definition delete -g {rg} -s {s} --api-id {api} --version-id {v} --definition-id {d} --yes')