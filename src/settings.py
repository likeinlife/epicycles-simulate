from pydantic import Field
from pydantic_settings import BaseSettings


class EpicycleSettings(BaseSettings):
    width: int = Field(1400)
    height: int = Field(800)
    fps: int = Field(120)
    grid_size: int = Field(20)


epicycle_settings = EpicycleSettings()  # type: ignore
