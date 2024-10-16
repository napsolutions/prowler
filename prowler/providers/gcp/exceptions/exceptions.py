from prowler.exceptions.exceptions import ProwlerException


class GCPBaseException(ProwlerException):
    """Base class for GCP Errors."""

    GCP_ERROR_CODES = {
        (1925, "GCPCloudResourceManagerAPINotUsedError"): {
            "message": "Cloud Resource Manager API not used",
            "remediation": "Enable the Cloud Resource Manager API for the project.",
        },
        (1926, "GCPHTTPError"): {
            "message": "HTTP error",
            "remediation": "Check the HTTP error and ensure the request is properly formatted.",
        },
        (1927, "GCPNoAccesibleProjectsError"): {
            "message": "No Project IDs can be accessed via Google Credentials",
            "remediation": "Ensure the project is accessible and properly set up.",
        },
        (1928, "GCPSetUpSessionError"): {
            "message": "Error setting up session",
            "remediation": "Check the session setup and ensure it is properly set up.",
        },
        (1929, "GCPGetProjectError"): {
            "message": "Error getting project",
            "remediation": "Check the project and ensure it is properly set up.",
        },
        (1930, "GCPTestConnectionError"): {
            "message": "Error testing connection to GCP",
            "remediation": "Check the connection and ensure it is properly set up.",
        },
        (1931, "GCPLoadCredentialsFromDictError"): {
            "message": "Error loading credentials from dictionary",
            "remediation": "Check the credentials and ensure they are properly set up. client_id, client_secret and refresh_token are required.",
        },
        (1932, "GCPStaticCredentialsError"): {
            "message": "Error loading static credentials",
            "remediation": "Check the credentials and ensure they are properly set up. client_id, client_secret and refresh_token are required.",
        },
    }

    def __init__(self, code, file=None, original_exception=None, message=None):
        provider = "GCP"
        error_info = self.GCP_ERROR_CODES.get((code, self.__class__.__name__))
        if message:
            error_info["message"] = message
        super().__init__(
            code=code,
            provider=provider,
            file=file,
            original_exception=original_exception,
            error_info=error_info,
        )


class GCPCredentialsError(GCPBaseException):
    """Base class for GCP credentials errors."""

    def __init__(self, code, file=None, original_exception=None, message=None):
        super().__init__(code, file, original_exception, message)


class GCPCloudResourceManagerAPINotUsedError(GCPBaseException):
    def __init__(self, file=None, original_exception=None, message=None):
        super().__init__(
            1925, file=file, original_exception=original_exception, message=message
        )


class GCPHTTPError(GCPBaseException):
    def __init__(self, file=None, original_exception=None, message=None):
        super().__init__(
            1926, file=file, original_exception=original_exception, message=message
        )


class GCPNoAccesibleProjectsError(GCPCredentialsError):
    def __init__(self, file=None, original_exception=None, message=None):
        super().__init__(
            1927, file=file, original_exception=original_exception, message=message
        )


class GCPSetUpSessionError(GCPCredentialsError):
    def __init__(self, file=None, original_exception=None, message=None):
        super().__init__(
            1928, file=file, original_exception=original_exception, message=message
        )


class GCPGetProjectError(GCPCredentialsError):
    def __init__(self, file=None, original_exception=None, message=None):
        super().__init__(
            1929, file=file, original_exception=original_exception, message=message
        )


class GCPTestConnectionError(GCPBaseException):
    def __init__(self, file=None, original_exception=None, message=None):
        super().__init__(
            1930, file=file, original_exception=original_exception, message=message
        )


class GCPLoadCredentialsFromDictError(GCPCredentialsError):
    def __init__(self, file=None, original_exception=None, message=None):
        super().__init__(
            1931, file=file, original_exception=original_exception, message=message
        )


class GCPStaticCredentialsError(GCPCredentialsError):
    def __init__(self, file=None, original_exception=None, message=None):
        super().__init__(
            1932, file=file, original_exception=original_exception, message=message
        )
