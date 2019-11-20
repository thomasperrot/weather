class AppError(Exception):
    pass


class UnknownCityError(AppError):
    pass


class NetworkError(AppError):
    pass
