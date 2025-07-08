from fastmcp import FastMCP
# from tools.base import (
#     ADMET_predict,
#     Pharmacokinetics_predict,
#     ToxScan_predict,
#     InputData,
#     RES,
#     AdmetInnerData,
#     InputPK,
#     PKResult,
#     ToxResult
# )
# from structs.admet import description as admet_description
# from structs.pk import description as pk_description

from tools.diffsbdd import * 
mcp = FastMCP("DiffsbddTest")

@mcp.tool(
    name="molecule_generation_by_index",
    description="Generate molecule SMILES by protein index (and pocket)."
)
async def multi_denovo_tool(
    index_list: List[str],
    n_samples: int = 1,
) -> Dict[str, Any]:
    return await multi_denovo_predict(index_list, n_samples)

@mcp.tool(
    name="molecule_generation_by_gene",
    description="Generate molecule SMILES by gene (through getting protein and pocket from the gene)."
)
async def denovo_gene_tool(
    gene_list: List[str],
    n_samples: int = 1,
) -> Dict[str, Any]:
    return await denovo_gene_predict(gene_list, n_samples)

# @mcp.resource("data://ADMET_reference", name="ADMET Reference Data")
# async def admet_meta():
#     return {
#         "name": "ADMET",
#         "description": "ADMET is a collection of 20 molecular descriptors that are commonly used to predict the pharmacokinetic and pharmacodynamic properties of drugs.",
#         "properties": admet_description
#     }


# @mcp.resource("data://Pharmacokinetics_reference", name="Pharmacokinetics Reference Data")
# async def pk_meta():
#     return {
#         "name": "Pharmacokinetics",
#         "description": "Pharmacokinetics is a collection of 10 molecular descriptors that are commonly used to predict the pharmacokinetic and pharmacodynamic properties of drugs.",
#         "properties": pk_description
#     }


# @mcp.tool(
#     name="ADMET_Service", 
#     description="Predict the ADMET properties of a molecule. Absorption, Distribution, Metabolism, Excretion and Toxicity Prediction for Molecules"
# )
# async def ADMET_predict_tool(data: InputData) -> RES[AdmetInnerData]:
#     return await ADMET_predict(data)


# @mcp.tool(
#     name="Pharmacokinetics_Service",
#     description="Predict the Pharmacokinetics properties of a molecule. Pharmacokinetic Metabolism Curve Prediction, Prediction of Drug Concentration Changes over Time."
# )
# async def Pharmacokinetics_predict_tool(data: InputPK) -> RES[PKResult]:
#     return await Pharmacokinetics_predict(data)


# @mcp.tool(
#     name="ToxScan_predict",
#     description="Predict the ToxScan properties of a molecule. Safety Evaluation of Drugs, Chemicals or Environmental Pollutants.",
# )
# async def ToxScan_predict_tool(data: InputData) -> RES[ToxResult]:
#     return await ToxScan_predict(data)




if __name__ == "__main__":
    mcp.run(transport='sse',host="0.0.0.0",port=5003)
