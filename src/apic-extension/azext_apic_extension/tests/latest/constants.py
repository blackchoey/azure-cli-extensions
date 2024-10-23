# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

import os

TEST_REGION = "eastus"
USERASSIGNED_IDENTITY = os.getenv('USERASSIGNED_IDENTITY')
USERASSIGNED_IDENTITY = USERASSIGNED_IDENTITY if USERASSIGNED_IDENTITY else "{/subscriptions/976c6e22-5aa9-47a4-a6db-bc1dcfebf792/resourceGroups/rg-apim-reader-MI/providers/Microsoft.ManagedIdentity/userAssignedIdentities/apim-reader-MI}"