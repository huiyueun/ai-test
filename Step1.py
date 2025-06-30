(unsloth_env) huiyu@huiyu-linux2:~/Workspace/test-1$ python3 step1.py 
🦥 Unsloth: Will patch your computer to enable 2x faster free finetuning.
🦥 Unsloth Zoo will now patch everything to make training faster!
Traceback (most recent call last):
  File "/usr/lib/python3/dist-packages/urllib3/connectionpool.py", line 700, in urlopen
    httplib_response = self._make_request(
  File "/usr/lib/python3/dist-packages/urllib3/connectionpool.py", line 383, in _make_request
    self._validate_conn(conn)
  File "/usr/lib/python3/dist-packages/urllib3/connectionpool.py", line 1017, in _validate_conn
    conn.connect()
  File "/usr/lib/python3/dist-packages/urllib3/connection.py", line 411, in connect
    self.sock = ssl_wrap_socket(
  File "/usr/lib/python3/dist-packages/urllib3/util/ssl_.py", line 449, in ssl_wrap_socket
    ssl_sock = _ssl_wrap_socket_impl(
  File "/usr/lib/python3/dist-packages/urllib3/util/ssl_.py", line 493, in _ssl_wrap_socket_impl
    return ssl_context.wrap_socket(sock, server_hostname=server_hostname)
  File "/usr/lib/python3.10/ssl.py", line 513, in wrap_socket
    return self.sslsocket_class._create(
  File "/usr/lib/python3.10/ssl.py", line 1100, in _create
    self.do_handshake()
  File "/usr/lib/python3.10/ssl.py", line 1371, in do_handshake
    self._sslobj.do_handshake()
ConnectionResetError: [Errno 104] Connection reset by peer

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "/home/huiyu/.local/lib/python3.10/site-packages/requests/adapters.py", line 667, in send
    resp = conn.urlopen(
  File "/usr/lib/python3/dist-packages/urllib3/connectionpool.py", line 756, in urlopen
    retries = retries.increment(
  File "/usr/lib/python3/dist-packages/urllib3/util/retry.py", line 534, in increment
    raise six.reraise(type(error), error, _stacktrace)
  File "/usr/lib/python3/dist-packages/six.py", line 718, in reraise
    raise value.with_traceback(tb)
  File "/usr/lib/python3/dist-packages/urllib3/connectionpool.py", line 700, in urlopen
    httplib_response = self._make_request(
  File "/usr/lib/python3/dist-packages/urllib3/connectionpool.py", line 383, in _make_request
    self._validate_conn(conn)
  File "/usr/lib/python3/dist-packages/urllib3/connectionpool.py", line 1017, in _validate_conn
    conn.connect()
  File "/usr/lib/python3/dist-packages/urllib3/connection.py", line 411, in connect
    self.sock = ssl_wrap_socket(
  File "/usr/lib/python3/dist-packages/urllib3/util/ssl_.py", line 449, in ssl_wrap_socket
    ssl_sock = _ssl_wrap_socket_impl(
  File "/usr/lib/python3/dist-packages/urllib3/util/ssl_.py", line 493, in _ssl_wrap_socket_impl
    return ssl_context.wrap_socket(sock, server_hostname=server_hostname)
  File "/usr/lib/python3.10/ssl.py", line 513, in wrap_socket
    return self.sslsocket_class._create(
  File "/usr/lib/python3.10/ssl.py", line 1100, in _create
    self.do_handshake()
  File "/usr/lib/python3.10/ssl.py", line 1371, in do_handshake
    self._sslobj.do_handshake()
urllib3.exceptions.ProtocolError: ('Connection aborted.', ConnectionResetError(104, 'Connection reset by peer'))

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "/home/huiyu/Workspace/test-1/step1.py", line 5, in <module>
    model, tokenizer = FastModel.from_pretrained(
  File "/home/huiyu/.local/lib/python3.10/site-packages/unsloth/models/loader.py", line 614, in from_pretrained
    files = HfFileSystem(token = token).glob(f"{model_name}/*.json")
  File "/home/huiyu/.local/lib/python3.10/site-packages/huggingface_hub/hf_file_system.py", line 520, in glob
    path = self.resolve_path(path, revision=kwargs.get("revision")).unresolve()
  File "/home/huiyu/.local/lib/python3.10/site-packages/huggingface_hub/hf_file_system.py", line 209, in resolve_path
    repo_and_revision_exist, err = self._repo_and_revision_exist(repo_type, repo_id, revision)
  File "/home/huiyu/.local/lib/python3.10/site-packages/huggingface_hub/hf_file_system.py", line 125, in _repo_and_revision_exist
    self._api.repo_info(
  File "/home/huiyu/.local/lib/python3.10/site-packages/huggingface_hub/utils/_validators.py", line 114, in _inner_fn
    return fn(*args, **kwargs)
  File "/home/huiyu/.local/lib/python3.10/site-packages/huggingface_hub/hf_api.py", line 2844, in repo_info
    return method(
  File "/home/huiyu/.local/lib/python3.10/site-packages/huggingface_hub/utils/_validators.py", line 114, in _inner_fn
    return fn(*args, **kwargs)
  File "/home/huiyu/.local/lib/python3.10/site-packages/huggingface_hub/hf_api.py", line 2628, in model_info
    r = get_session().get(path, headers=headers, timeout=timeout, params=params)
  File "/home/huiyu/.local/lib/python3.10/site-packages/requests/sessions.py", line 602, in get
    return self.request("GET", url, **kwargs)
  File "/home/huiyu/.local/lib/python3.10/site-packages/requests/sessions.py", line 589, in request
    resp = self.send(prep, **send_kwargs)
  File "/home/huiyu/.local/lib/python3.10/site-packages/requests/sessions.py", line 703, in send
    r = adapter.send(request, **kwargs)
  File "/home/huiyu/.local/lib/python3.10/site-packages/huggingface_hub/utils/_http.py", line 96, in send
    return super().send(request, *args, **kwargs)
  File "/home/huiyu/.local/lib/python3.10/site-packages/requests/adapters.py", line 682, in send
    raise ConnectionError(err, request=request)
requests.exceptions.ConnectionError: (ProtocolError('Connection aborted.', ConnectionResetError(104, 'Connection reset by peer')), '(Request ID: f1b33842-909e-48a5-afae-19e6802e9492)')
