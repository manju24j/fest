# Stubs for httplib (Python 2)
#
# Generated by stubgen and manually massaged a bit.
# Needs lots more work!

from typing import Any, Dict
import mimetools

class HTTPMessage(mimetools.Message):
    def addheader(self, key: str, value: str) -> None: ...
    def addcontinue(self, key: str, more: str) -> None: ...
    dict = ... # type: Dict[str, str]
    unixfrom = ... # type: str
    headers = ... # type: Any
    status = ... # type: str
    seekable = ... # type: bool
    def readheaders(self) -> None: ...

class HTTPResponse:
    fp = ... # type: Any
    debuglevel = ... # type: Any
    strict = ... # type: Any
    msg = ... # type: Any
    version = ... # type: Any
    status = ... # type: Any
    reason = ... # type: Any
    chunked = ... # type: Any
    chunk_left = ... # type: Any
    length = ... # type: Any
    will_close = ... # type: Any
    def __init__(self, sock, debuglevel=0, strict=0, method=None, buffering:bool=...) -> None: ...
    def begin(self): ...
    def close(self): ...
    def isclosed(self): ...
    def read(self, amt=None): ...
    def fileno(self): ...
    def getheader(self, name, default=None): ...
    def getheaders(self): ...

class HTTPConnection:
    response_class = ... # type: Any
    default_port = ... # type: Any
    auto_open = ... # type: Any
    debuglevel = ... # type: Any
    strict = ... # type: Any
    timeout = ... # type: Any
    source_address = ... # type: Any
    sock = ... # type: Any
    def __init__(self, host, port=None, strict=None, timeout=..., source_address=None) -> None: ...
    def set_tunnel(self, host, port=None, headers=None): ...
    def set_debuglevel(self, level): ...
    def connect(self): ...
    def close(self): ...
    def send(self, data): ...
    def putrequest(self, method, url, skip_host=0, skip_accept_encoding=0): ...
    def putheader(self, header, *values): ...
    def endheaders(self, message_body=None): ...
    def request(self, method, url, body=None, headers=...): ...
    def getresponse(self, buffering:bool=...): ...

class HTTP:
    debuglevel = ... # type: Any
    def __init__(self, host:str=..., port=None, strict=None) -> None: ...
    def connect(self, host=None, port=None): ...
    def getfile(self): ...
    file = ... # type: Any
    headers = ... # type: Any
    def getreply(self, buffering:bool=...): ...
    def close(self): ...

class HTTPSConnection(HTTPConnection):
    default_port = ... # type: Any
    key_file = ... # type: Any
    cert_file = ... # type: Any
    def __init__(self, host, port=None, key_file=None, cert_file=None, strict=None, timeout=..., source_address=None, context=None) -> None: ...
    sock = ... # type: Any
    def connect(self): ...

class HTTPS(HTTP):
    key_file = ... # type: Any
    cert_file = ... # type: Any
    def __init__(self, host:str=..., port=None, key_file=None, cert_file=None, strict=None, context=None) -> None: ...

class HTTPException(Exception): ...
class NotConnected(HTTPException): ...
class InvalidURL(HTTPException): ...

class UnknownProtocol(HTTPException):
    args = ... # type: Any
    version = ... # type: Any
    def __init__(self, version) -> None: ...

class UnknownTransferEncoding(HTTPException): ...
class UnimplementedFileMode(HTTPException): ...

class IncompleteRead(HTTPException):
    args = ... # type: Any
    partial = ... # type: Any
    expected = ... # type: Any
    def __init__(self, partial, expected=None) -> None: ...

class ImproperConnectionState(HTTPException): ...
class CannotSendRequest(ImproperConnectionState): ...
class CannotSendHeader(ImproperConnectionState): ...
class ResponseNotReady(ImproperConnectionState): ...

class BadStatusLine(HTTPException):
    args = ... # type: Any
    line = ... # type: Any
    def __init__(self, line) -> None: ...

class LineTooLong(HTTPException):
    def __init__(self, line_type) -> None: ...

error = ... # type: Any

class LineAndFileWrapper:
    def __init__(self, line, file) -> None: ...
    def __getattr__(self, attr): ...
    def read(self, amt=None): ...
    def readline(self): ...
    def readlines(self, size=None): ...

# Constants

responses = ... # type: Dict[int, str]

HTTP_PORT = ... # type: int
HTTPS_PORT = ... # type: int

# status codes
# informational
CONTINUE = ... # type: int
SWITCHING_PROTOCOLS = ... # type: int
PROCESSING = ... # type: int

# successful
OK = ... # type: int
CREATED = ... # type: int
ACCEPTED = ... # type: int
NON_AUTHORITATIVE_INFORMATION = ... # type: int
NO_CONTENT = ... # type: int
RESET_CONTENT = ... # type: int
PARTIAL_CONTENT = ... # type: int
MULTI_STATUS = ... # type: int
IM_USED = ... # type: int

# redirection
MULTIPLE_CHOICES = ... # type: int
MOVED_PERMANENTLY = ... # type: int
FOUND = ... # type: int
SEE_OTHER = ... # type: int
NOT_MODIFIED = ... # type: int
USE_PROXY = ... # type: int
TEMPORARY_REDIRECT = ... # type: int

# client error
BAD_REQUEST = ... # type: int
UNAUTHORIZED = ... # type: int
PAYMENT_REQUIRED = ... # type: int
FORBIDDEN = ... # type: int
NOT_FOUND = ... # type: int
METHOD_NOT_ALLOWED = ... # type: int
NOT_ACCEPTABLE = ... # type: int
PROXY_AUTHENTICATION_REQUIRED = ... # type: int
REQUEST_TIMEOUT = ... # type: int
CONFLICT = ... # type: int
GONE = ... # type: int
LENGTH_REQUIRED = ... # type: int
PRECONDITION_FAILED = ... # type: int
REQUEST_ENTITY_TOO_LARGE = ... # type: int
REQUEST_URI_TOO_LONG = ... # type: int
UNSUPPORTED_MEDIA_TYPE = ... # type: int
REQUESTED_RANGE_NOT_SATISFIABLE = ... # type: int
EXPECTATION_FAILED = ... # type: int
UNPROCESSABLE_ENTITY = ... # type: int
LOCKED = ... # type: int
FAILED_DEPENDENCY = ... # type: int
UPGRADE_REQUIRED = ... # type: int

# server error
INTERNAL_SERVER_ERROR = ... # type: int
NOT_IMPLEMENTED = ... # type: int
BAD_GATEWAY = ... # type: int
SERVICE_UNAVAILABLE = ... # type: int
GATEWAY_TIMEOUT = ... # type: int
HTTP_VERSION_NOT_SUPPORTED = ... # type: int
INSUFFICIENT_STORAGE = ... # type: int
NOT_EXTENDED = ... # type: int
