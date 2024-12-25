# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

import os

TEST_REGION = "eastus"
# to set USERASSIGNED_IDENTITY, refer to https://learn.microsoft.com/en-us/azure/api-center/import-api-management-apis?tabs=portal#option-2-import-apis-directly-from-your-api-management-instance
# USERASSIGNED_IDENTITY = os.getenv('USERASSIGNED_IDENTITY')
USERASSIGNED_IDENTITY = "/subscriptions/b72ba90c-17fc-4d42-a890-2de38220b1a9/resourceGroups/rg-apic-extension-cli-test/providers/Microsoft.ManagedIdentity/userAssignedIdentities/apic-extension-cli-test"
# aws credentials KeyVault references
ACCESS_KEY_LINK = "https://kv-canary-franktest.vault.azure.net/secrets/AccessKey"
SECRET_ACCESS_KEY_LINK = "https://kv-canary-franktest.vault.azure.net/secrets/SecretAccessKey"
AWS_REGION = "us-west-2"