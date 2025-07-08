#!/bin/bash
source /internfs/geyutang/miniconda3/etc/profile.d/conda.sh
conda activate /internfs/geyutang/miniconda3/envs/cbgbench
fastmcp run main.py --transport sse --host 0.0.0.0 --port 5003 2>&1 | tee /internfs/geyutang/mcp/mcp_server_inference/logs/test.log