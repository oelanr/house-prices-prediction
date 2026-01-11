from pydantic import BaseModel, Field

class HouseFeatures(BaseModel):
    OverallQual: int = Field(..., description="Overall material and finish quality")
    GrLivArea: int = Field(..., description="Above grade (ground) living area square feet")
    TotalBsmtSF: int = Field(..., description="Total basement square feet")
    FirstFlrSF: int = Field(..., alias="1stFlrSF", description="First Floor square feet")
    Fireplaces: int = Field(..., description="Number of fireplaces")
    GarageCars: int = Field(..., description="Size of garage in car capacity")
    LotArea: int = Field(..., description="Lot size in square feet")
    BsmtFinSF1: int = Field(..., description="Type 1 finished square feet of basement")
    GarageArea: int = Field(..., description="Size of garage in square feet")
    YearRemodAdd: int = Field(..., description="Remodel year")
    OverallCond: int = Field(..., description="Overall condition rating")
    YearBuilt: int = Field(..., description="Original construction year")
