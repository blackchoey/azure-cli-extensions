# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

# This file patches the commands generated by aaz to provide expected user experience per product design
# Always use aaz to update the commands if it's possible
from .aaz.latest.apic.api import (
    Create as CreateAPI,
    Delete as DeleteAPI,
    List as ListAPI,
    Show as ShowAPI,
    Update as UpdateAPI
)
from .aaz.latest.apic.api.definition import (
    Create as CreateAPIDefinition,
    Delete as DeleteAPIDefinition,
    ExportSpecification as ExportAPIDefinition,
    ImportSpecification as ImportAPIDefinition,
    List as ListAPIDefinition,
    Show as ShowAPIDefinition,
    Update as UpdateAPIDefinition
)
from .aaz.latest.apic.api.version import (
    Create as CreateAPIVersion,
    Delete as DeleteAPIVersion,
    List as ListAPIVersion,
    Show as ShowAPIVersion,
    Update as UpdateAPIVersion
)
from .aaz.latest.apic.api.deployment import (
    Create as CreateAPIDeployment,
    Delete as DeleteAPIDeployment,
    List as ListAPIDeployment,
    Show as ShowAPIDeployment,
    Update as UpdateAPIDeployment
)
from .aaz.latest.apic.environment import (
    Create as CreateEnvironment,
    Delete as DeleteEnvironment,
    List as ListEnvironment,
    Show as ShowEnvironment,
    Update as UpdateEnvironment
)
from .aaz.latest.apic.metadata import (
    Create as CreateMetadata,
    Export as ExportMetadata
)
from .aaz.latest.apic import ImportFromApim, Create as CreateService

from azure.cli.core.aaz._arg import AAZStrArg, AAZListArg


class DefaultWorkspaceParameter:
    # pylint: disable=too-few-public-methods
    @classmethod
    def _build_arguments_schema(cls, *args, **kwargs):
        # pylint: disable=protected-access
        args_schema = super()._build_arguments_schema(*args, **kwargs)
        args_schema.workspace_name._required = False
        args_schema.workspace_name._registered = False
        return args_schema

    def pre_operations(self):
        args = self.ctx.args
        args.workspace_name = "default"


# `az apic` commands
class CreateServiceExtension(CreateService):
    # pylint: disable=too-few-public-methods
    @classmethod
    def _build_arguments_schema(cls, *args, **kwargs):
        # pylint: disable=protected-access
        args_schema = super()._build_arguments_schema(*args, **kwargs)
        # temporary hide sku parameter as SKU has many fields and we needs more discussion on the UX
        args_schema.sku_name._registered = False
        return args_schema

    def pre_operations(self):
        args = self.ctx.args
        args.sku_name = "Free"


# `az apic api` commands
class CreateAPIExtension(DefaultWorkspaceParameter, CreateAPI):
    pass


class DeleteAPIExtension(DefaultWorkspaceParameter, DeleteAPI):
    pass


class ListAPIExtension(DefaultWorkspaceParameter, ListAPI):
    pass


class ShowAPIExtension(DefaultWorkspaceParameter, ShowAPI):
    pass


class UpdateAPIExtension(DefaultWorkspaceParameter, UpdateAPI):
    pass


# `az apic api definition` commands
class CreateAPIDefinitionExtension(DefaultWorkspaceParameter, CreateAPIDefinition):
    pass


class DeleteAPIDefinitionExtension(DefaultWorkspaceParameter, DeleteAPIDefinition):
    pass


class ExportAPIDefinitionExtension(DefaultWorkspaceParameter, ExportAPIDefinition):
    pass


class ImportAPIDefinitionExtension(DefaultWorkspaceParameter, ImportAPIDefinition):
    # pylint: disable=too-few-public-methods
    @classmethod
    def _build_arguments_schema(cls, *args, **kwargs):
        # pylint: disable=protected-access
        args_schema = super()._build_arguments_schema(*args, **kwargs)
        args_schema.format._required = True
        args_schema.specification._required = True
        args_schema.value._required = True
        return args_schema


class ListAPIDefinitionExtension(DefaultWorkspaceParameter, ListAPIDefinition):
    pass


class ShowAPIDefinitionExtension(DefaultWorkspaceParameter, ShowAPIDefinition):
    pass


class UpdateAPIDefinitionExtension(DefaultWorkspaceParameter, UpdateAPIDefinition):
    pass


# `az apic api version` commands
class CreateAPIVersionExtension(DefaultWorkspaceParameter, CreateAPIVersion):
    pass


class DeleteAPIVersionExtension(DefaultWorkspaceParameter, DeleteAPIVersion):
    pass


class ListAPIVersionExtension(DefaultWorkspaceParameter, ListAPIVersion):
    pass


class ShowAPIVersionExtension(DefaultWorkspaceParameter, ShowAPIVersion):
    pass


class UpdateAPIVersionExtension(DefaultWorkspaceParameter, UpdateAPIVersion):
    pass


# `az apic api deployment` commands
class CreateAPIDeploymentExtension(DefaultWorkspaceParameter, CreateAPIDeployment):
    # pylint: disable=too-few-public-methods
    @classmethod
    def _build_arguments_schema(cls, *args, **kwargs):
        # pylint: disable=protected-access
        args_schema = super()._build_arguments_schema(*args, **kwargs)
        args_schema.definition_id._required = True
        args_schema.environment_id._required = True
        args_schema.server._required = True
        args_schema.title._required = True
        return args_schema


class DeleteAPIDeploymentExtension(DefaultWorkspaceParameter, DeleteAPIDeployment):
    pass


class ListAPIDeploymentExtension(DefaultWorkspaceParameter, ListAPIDeployment):
    pass


class ShowAPIDeploymentExtension(DefaultWorkspaceParameter, ShowAPIDeployment):
    pass


class UpdateAPIDeploymentExtension(DefaultWorkspaceParameter, UpdateAPIDeployment):
    pass


# `az apic environment` commands
class CreateEnvironmentExtension(DefaultWorkspaceParameter, CreateEnvironment):
    pass


class DeleteEnvironmentExtension(DefaultWorkspaceParameter, DeleteEnvironment):
    pass


class ListEnvironmentExtension(DefaultWorkspaceParameter, ListEnvironment):
    pass


class ShowEnvironmentExtension(DefaultWorkspaceParameter, ShowEnvironment):
    pass


class UpdateEnvironmentExtension(DefaultWorkspaceParameter, UpdateEnvironment):
    pass


# `az apic metadata commands`
class CreateMetadataExtension(CreateMetadata):
    # pylint: disable=too-few-public-methods
    @classmethod
    def _build_arguments_schema(cls, *args, **kwargs):
        # pylint: disable=protected-access
        args_schema = super()._build_arguments_schema(*args, **kwargs)
        args_schema.assignments._required = True
        return args_schema


class ExportMetadataExtension(ExportMetadata):
    # pylint: disable=too-few-public-methods
    @classmethod
    def _build_arguments_schema(cls, *args, **kwargs):
        # pylint: disable=protected-access
        args_schema = super()._build_arguments_schema(*args, **kwargs)
        args_schema.assignments._required = True
        return args_schema


# `az apic service commands`
class ImportFromApimExtension(ImportFromApim):
    # pylint: disable=too-few-public-methods
    @classmethod
    def _build_arguments_schema(cls, *args, **kwargs):
        # pylint: disable=protected-access
        args_schema = super()._build_arguments_schema(*args, **kwargs)
        args_schema.source_resource_ids._required = False
        args_schema.source_resource_ids._registered = False

        args_schema.apim_subscription_id = AAZStrArg(
            options=["--apim-subscription"],
            help="The subscription id of the source APIM instance.",
            required=False
        )

        args_schema.apim_resource_group = AAZStrArg(
            options=["--apim-resource-group"],
            help="The resource group of the source APIM instance.",
            required=False
        )

        args_schema.apim_name = AAZStrArg(
            options=["--apim-name"],
            help="The name of the source APIM instance.",
            required=True
        )

        args_schema.apim_apis = AAZListArg(
            options=["--apim-apis"],
            help="The APIs to be imported.",
            required=True
        )
        args_schema.apim_apis.Element = AAZStrArg()

        return args_schema

    def pre_operations(self):
        super().pre_operations()
        args = self.ctx.args

        # compose sourceResourceIds property in the request body
        # Use same subscription id and resource group as API Center by default
        resource_group = args.resource_group
        subscription_id = self.ctx.subscription_id

        # Use user provided subscription id
        if args.apim_subscription_id:
            subscription_id = args.apim_subscription_id

        # Use user provided resource group
        if args.apim_resource_group:
            resource_group = args.apim_resource_group

        source_resource_ids = []
        for item in args.apim_apis:
            source_resource_ids.append(
                f"/subscriptions/{subscription_id}/resourceGroups/{resource_group}/providers/"
                f"Microsoft.ApiManagement/service/{args.apim_name}/apis/{item}"
            )

        args.source_resource_ids = source_resource_ids
