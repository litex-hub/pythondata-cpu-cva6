// Copyright 2022 Thales DIS design services SAS
//
// Licensed under the Solderpad Hardware Licence, Version 2.0 (the "License");
// you may not use this file except in compliance with the License.
// SPDX-License-Identifier: Apache-2.0 WITH SHL-2.0
// You may obtain a copy of the License at https://solderpad.org/licenses/
//
// Original Author: Jean-Roch COULON (jean-roch.coulon@thalesgroup.com)


package cva6_config_pkg;

    localparam CVA6ConfigXlen = 32;

    localparam CVA6ConfigFpuEn = 0;
    localparam CVA6ConfigF16En = 0;
    localparam CVA6ConfigF16AltEn = 0;
    localparam CVA6ConfigF8En = 0;
    localparam CVA6ConfigFVecEn = 0;

    localparam CVA6ConfigCvxifEn = 1;
    localparam CVA6ConfigCExtEn = 1;
    localparam CVA6ConfigAExtEn = 0;

    localparam CVA6ConfigFetchUserEn = 0;
    localparam CVA6ConfigFetchUserWidth = CVA6ConfigXlen;
    localparam CVA6ConfigDataUserEn = 0;
    localparam CVA6ConfigDataUserWidth = CVA6ConfigXlen;

    localparam CVA6ConfigRenameEn = 0;

endpackage
