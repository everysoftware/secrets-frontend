from app.exceptions import BackendError


class RequiresLoginException(BackendError):
    pass


class AlreadyLoggedInException(BackendError):
    pass