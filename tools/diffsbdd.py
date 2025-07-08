import httpx
from httpx import Timeout
from typing import List, Dict, Any


DEFAULT_TIMEOUT = Timeout(600.0, connect=300.0)


async def multi_denovo_predict(
    index_list: List[str],
    n_samples: int = 1,
) -> Dict[str, Any]:
    """
    根据 PDB/链 ID 列表生成分子 SMILES。
    """
    MULTI_DENOVO_URL = "http://101.126.67.113:8444/multi_denovo"
    try:
        async with httpx.AsyncClient(timeout=DEFAULT_TIMEOUT) as client:
            payload = {"index_list": index_list, "n_samples": n_samples}
            resp = await client.post(
                MULTI_DENOVO_URL,
                json=payload,
                headers={"Content-Type": "application/json"},
            )
            resp.raise_for_status()
            return resp.json()                       # 直接透传后端响应
    except Exception as e:
        return {"code": -1, "msg": f"multi_denovo error: {e}", "data": None}


async def denovo_gene_predict(
    gene_list: List[str],
    n_samples: int = 1,
) -> Dict[str, Any]:
    """
    根据基因名列表生成分子 SMILES。
    """
    DENOVO_GENE_URL  = "http://101.126.67.113:8444/denovo_gene"
    try:
        async with httpx.AsyncClient(timeout=DEFAULT_TIMEOUT) as client:
            payload = {"gene_list": gene_list, "n_samples": n_samples}
            resp = await client.post(
                DENOVO_GENE_URL,
                json=payload,
                headers={"Content-Type": "application/json"},
            )
            resp.raise_for_status()
            return resp.json()
    except Exception as e:
        return {"code": -1, "msg": f"denovo_gene error: {e}", "data": None}



