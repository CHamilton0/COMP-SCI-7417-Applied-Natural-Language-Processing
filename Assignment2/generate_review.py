import typer
from typing_extensions import Annotated

def main(
    service_rating: Annotated[int, typer.Option(min=1, max=5)] = 5.0,
    cleanliness_rating: Annotated[int | None, typer.Option(min=1, max=5)] = None,
    overall_rating: Annotated[int | None, typer.Option(min=1, max=5)] = None,
    value_rating: Annotated[int | None, typer.Option(min=1, max=5)] = None,
    location_rating: Annotated[int | None, typer.Option(min=1, max=5)] = None,
    sleep_quality_rating: Annotated[int | None, typer.Option(min=1, max=5)] = None,
    rooms_rating: Annotated[int | None, typer.Option(min=1, max=5)] = None,
    check_in_front_desk_rating: Annotated[int | None, typer.Option(min=1, max=5)] = None,
    business_service_rating: Annotated[int | None, typer.Option(min=1, max=5)] = None,
):
    """
    Generate a text review based on ratings
    """
    print(service_rating)
    print(cleanliness_rating)
    print(overall_rating)
    print(value_rating)
    print(location_rating)
    print(sleep_quality_rating)
    print(rooms_rating)
    print(check_in_front_desk_rating)
    print(business_service_rating)


if __name__ == "__main__":
    typer.run(main)