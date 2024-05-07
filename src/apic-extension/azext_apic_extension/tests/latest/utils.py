# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from azure.cli.testsdk.preparers import NoTrafficRecordingPreparer, SingleValueReplacer, get_dummy_cli, CliTestError, ResourceGroupPreparer

class ApicServicePreparer(NoTrafficRecordingPreparer, SingleValueReplacer):
    def __init__(self, name_prefix='clitest', length=24,
                 parameter_name='service_name', resource_group_parameter_name='resource_group', key='s'):
        super(ApicServicePreparer, self).__init__(name_prefix, length)
        self.cli_ctx = get_dummy_cli()
        self.resource_group_parameter_name = resource_group_parameter_name
        self.parameter_name = parameter_name
        self.key = key

    def create_resource(self, name, **kwargs):
        group = self._get_resource_group(**kwargs)

        template = 'az apic service create --name {} -g {}'
        print(template.format(name, group))
        self.live_only_execute(self.cli_ctx, template.format(name, group))

        self.test_class_instance.kwargs[self.key] = name
        return {self.parameter_name: name}

    def remove_resource(self, name, **kwargs):
        # ResourceGroupPreparer will delete everything
        pass

    def _get_resource_group(self, **kwargs):
        try:
            return kwargs.get(self.resource_group_parameter_name)
        except KeyError:
            template = 'To create a API Center service a resource group is required. Please add ' \
                       'decorator @{} in front of this preparer.'
            raise CliTestError(template.format(ResourceGroupPreparer.__name__))

class ApicMetadataPreparer(NoTrafficRecordingPreparer, SingleValueReplacer):
    def __init__(self, name_prefix='clitest', length=24,
                 parameter_name='metadata_name', resource_group_parameter_name='resource_group',
                 apic_service_parameter_name='service_name',
                 schema='{"type":"boolean", "title":"Public Facing"}',
                 assignments='[{entity:api,required:true,deprecated:false}]',
                 key='m'):
        super(ApicMetadataPreparer, self).__init__(name_prefix, length)
        self.cli_ctx = get_dummy_cli()
        self.resource_group_parameter_name = resource_group_parameter_name
        self.api_service_parameter_name = apic_service_parameter_name
        self.parameter_name = parameter_name
        self.schema = schema
        self.assignments = assignments
        self.key = key

    def create_resource(self, name, **kwargs):
        group = self._get_resource_group(**kwargs)
        service = self._get_apic_service(**kwargs)

        template = 'az apic metadata create -g {} -s {} --name {} --schema \'{}\' --assignments \'{}\''
        cmd = template.format(group, service, name, self.schema, self.assignments)
        print(cmd)
        self.live_only_execute(self.cli_ctx, cmd)

        self.test_class_instance.kwargs[self.key] = name
        return {self.parameter_name: name}

    def remove_resource(self, name, **kwargs):
        # ResourceGroupPreparer will delete everything
        pass

    def _get_resource_group(self, **kwargs):
        try:
            return kwargs.get(self.resource_group_parameter_name)
        except KeyError:
            template = 'To create an API Center metadata a resource group is required. Please add ' \
                       'decorator @{} in front of this preparer.'
            raise CliTestError(template.format(ResourceGroupPreparer.__name__))

    def _get_apic_service(self, **kwargs):
        try:
            return kwargs.get(self.api_service_parameter_name)
        except KeyError:
            template = 'To create an API Center metadata a API Center service is required. Please add ' \
                       'decorator @{} in front of this preparer.'
            raise CliTestError(template.format(ApicServicePreparer.__name__))

class ApicEnvironmentPreparer(NoTrafficRecordingPreparer, SingleValueReplacer):
    def __init__(self, name_prefix='clitest', length=24,
                 parameter_name='environment_id', resource_group_parameter_name='resource_group',
                 apic_service_parameter_name='service_name', key='e'):
        super(ApicEnvironmentPreparer, self).__init__(name_prefix, length)
        self.cli_ctx = get_dummy_cli()
        self.resource_group_parameter_name = resource_group_parameter_name
        self.api_service_parameter_name = apic_service_parameter_name
        self.parameter_name = parameter_name
        self.key = key

    def create_resource(self, name, **kwargs):
        group = self._get_resource_group(**kwargs)
        service = self._get_apic_service(**kwargs)

        template = 'az apic environment create -g {} -s {} --environment-id {} --title "test environment" --type testing'
        cmd = template.format(group, service, name)
        print(cmd)
        self.live_only_execute(self.cli_ctx, cmd)

        self.test_class_instance.kwargs[self.key] = name
        return {self.parameter_name: name}

    def remove_resource(self, name, **kwargs):
        # ResourceGroupPreparer will delete everything
        pass

    def _get_resource_group(self, **kwargs):
        try:
            return kwargs.get(self.resource_group_parameter_name)
        except KeyError:
            template = 'To create an API Center environment a resource group is required. Please add ' \
                       'decorator @{} in front of this preparer.'
            raise CliTestError(template.format(ResourceGroupPreparer.__name__))

    def _get_apic_service(self, **kwargs):
        try:
            return kwargs.get(self.api_service_parameter_name)
        except KeyError:
            template = 'To create an API Center environment an API Center service is required. Please add ' \
                       'decorator @{} in front of this preparer.'
            raise CliTestError(template.format(ApicServicePreparer.__name__))

class ApicApiPreparer(NoTrafficRecordingPreparer, SingleValueReplacer):
    def __init__(self, name_prefix='clitest', length=24,
                 parameter_name='api_id', resource_group_parameter_name='resource_group',
                 apic_service_parameter_name='service_name', key='api'):
        super(ApicApiPreparer, self).__init__(name_prefix, length)
        self.cli_ctx = get_dummy_cli()
        self.resource_group_parameter_name = resource_group_parameter_name
        self.api_service_parameter_name = apic_service_parameter_name
        self.parameter_name = parameter_name
        self.key = key

    def create_resource(self, name, **kwargs):
        group = self._get_resource_group(**kwargs)
        service = self._get_apic_service(**kwargs)

        template = 'az apic api create -g {} -s {} --api-id {} --title "Echo API" --type rest'
        cmd = template.format(group, service, name)
        print(cmd)
        self.live_only_execute(self.cli_ctx, cmd)

        self.test_class_instance.kwargs[self.key] = name
        return {self.parameter_name: name}

    def remove_resource(self, name, **kwargs):
        # ResourceGroupPreparer will delete everything
        pass

    def _get_resource_group(self, **kwargs):
        try:
            return kwargs.get(self.resource_group_parameter_name)
        except KeyError:
            template = 'To create an API Center API a resource group is required. Please add ' \
                       'decorator @{} in front of this preparer.'
            raise CliTestError(template.format(ResourceGroupPreparer.__name__))

    def _get_apic_service(self, **kwargs):
        try:
            return kwargs.get(self.api_service_parameter_name)
        except KeyError:
            template = 'To create an API Center API an API Center service is required. Please add ' \
                       'decorator @{} in front of this preparer.'
            raise CliTestError(template.format(ApicServicePreparer.__name__))

class ApicVersionPreparer(NoTrafficRecordingPreparer, SingleValueReplacer):
    def __init__(self, name_prefix='clitest', length=24,
                 parameter_name='version_id', resource_group_parameter_name='resource_group',
                 apic_service_parameter_name='service_name', apic_api_parameter_name='api_id',
                 key='v'):
        super(ApicVersionPreparer, self).__init__(name_prefix, length)
        self.cli_ctx = get_dummy_cli()
        self.resource_group_parameter_name = resource_group_parameter_name
        self.apic_service_parameter_name = apic_service_parameter_name
        self.parameter_name = parameter_name
        self.apic_api_parameter_name = apic_api_parameter_name
        self.key = key

    def create_resource(self, name, **kwargs):
        group = self._get_resource_group(**kwargs)
        service = self._get_apic_service(**kwargs)
        api = self._get_apic_api(**kwargs)

        template = 'az apic api version create -g {} -s {} --api-id {} --version-id {} --lifecycle-stage production --title "v1.0.0"'
        cmd = template.format(group, service, api, name)
        print(cmd)
        self.live_only_execute(self.cli_ctx, cmd)

        self.test_class_instance.kwargs[self.key] = name
        return {self.parameter_name: name}

    def remove_resource(self, name, **kwargs):
        # ResourceGroupPreparer will delete everything
        pass

    def _get_resource_group(self, **kwargs):
        try:
            return kwargs.get(self.resource_group_parameter_name)
        except KeyError:
            template = 'To create an API Center API a resource group is required. Please add ' \
                       'decorator @{} in front of this preparer.'
            raise CliTestError(template.format(ResourceGroupPreparer.__name__))

    def _get_apic_service(self, **kwargs):
        try:
            return kwargs.get(self.apic_service_parameter_name)
        except KeyError:
            template = 'To create an API Center API an API Center service is required. Please add ' \
                       'decorator @{} in front of this preparer.'
            raise CliTestError(template.format(ApicServicePreparer.__name__))

    def _get_apic_api(self, **kwargs):
        try:
            return kwargs.get(self.apic_api_parameter_name)
        except KeyError:
            template = 'To create an API Center Version an API Center API is required. Please add ' \
                       'decorator @{} in front of this preparer.'
            raise CliTestError(template.format(ApicApiPreparer.__name__))
        
class ApicDefinitionPreparer(NoTrafficRecordingPreparer, SingleValueReplacer):
    def __init__(self, name_prefix='clitest', length=24,
                 parameter_name='version_id', resource_group_parameter_name='resource_group',
                 apic_service_parameter_name='service_name', apic_api_parameter_name='api_id',
                 apic_version_parameter_name='version_id', key='d'):
        super(ApicDefinitionPreparer, self).__init__(name_prefix, length)
        self.cli_ctx = get_dummy_cli()
        self.resource_group_parameter_name = resource_group_parameter_name
        self.apic_service_parameter_name = apic_service_parameter_name
        self.parameter_name = parameter_name
        self.apic_api_parameter_name = apic_api_parameter_name
        self.apic_version_parameter_name = apic_version_parameter_name
        self.key = key

    def create_resource(self, name, **kwargs):
        group = self._get_resource_group(**kwargs)
        service = self._get_apic_service(**kwargs)
        api = self._get_apic_api(**kwargs)
        version = self._get_apic_version(**kwargs)

        template = 'az apic api definition create -g {} -s {} --api-id {} --version-id {} --definition-id {} --title "OpenAPI"'
        cmd = template.format(group, service, api, version, name)
        print(cmd)
        self.live_only_execute(self.cli_ctx, cmd)

        self.test_class_instance.kwargs[self.key] = name
        return {self.parameter_name: name}

    def remove_resource(self, name, **kwargs):
        # ResourceGroupPreparer will delete everything
        pass

    def _get_resource_group(self, **kwargs):
        try:
            return kwargs.get(self.resource_group_parameter_name)
        except KeyError:
            template = 'To create an API Center API a resource group is required. Please add ' \
                       'decorator @{} in front of this preparer.'
            raise CliTestError(template.format(ResourceGroupPreparer.__name__))

    def _get_apic_service(self, **kwargs):
        try:
            return kwargs.get(self.apic_service_parameter_name)
        except KeyError:
            template = 'To create an API Center API an API Center service is required. Please add ' \
                       'decorator @{} in front of this preparer.'
            raise CliTestError(template.format(ApicServicePreparer.__name__))

    def _get_apic_api(self, **kwargs):
        try:
            return kwargs.get(self.apic_api_parameter_name)
        except KeyError:
            template = 'To create an API Center Version an API Center API is required. Please add ' \
                       'decorator @{} in front of this preparer.'
            raise CliTestError(template.format(ApicApiPreparer.__name__))
        
    def _get_apic_version(self, **kwargs):
        try:
            return kwargs.get(self.apic_version_parameter_name)
        except KeyError:
            template = 'To create an API Center Definition an API Center Version is required. Please add ' \
                       'decorator @{} in front of this preparer.'
            raise CliTestError(template.format(ApicVersionPreparer.__name__))