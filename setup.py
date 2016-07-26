import sys
sys.dont_write_bytecode = True
# This does the compilerign and error handling for us.
import compile_helper

# Never PYD ``__init__.py`` files. It will probably fuck things up until I find out otherwise.
# Also Do not PYD the followign files in DecoraterBotCore:
# BotCommands.py
# BotVoiceCommands.py
# Ignore.py
compile_helper.compile_to_pyd('to_build\\DecoraterBotCore\\', 'BotLogs.py')
compile_helper.compile_to_pyd('to_build\\DecoraterBotCore\\', 'BotPMError.py')
compile_helper.compile_to_pyd('to_build\\DecoraterBotCore\\', 'Login.py')
compile_helper.compile_to_pyd('to_build\\DecoraterBotCore\\', 'Core.py')

# Now lets pyd some of the dependencies to shorten exceptions somewhat.

# how lets build aiohttp to all pyd's.
compile_helper.compile_to_pyd('to_build\\aiohttp\\', 'abc.py')
compile_helper.compile_to_pyd('to_build\\aiohttp\\', 'client.py')
compile_helper.compile_to_pyd('to_build\\aiohttp\\', 'client_reqrep.py')
compile_helper.compile_to_pyd('to_build\\aiohttp\\', 'connector.py')
compile_helper.compile_to_pyd('to_build\\aiohttp\\', 'errors.py')
compile_helper.compile_to_pyd('to_build\\aiohttp\\', 'hdrs.py')
compile_helper.compile_to_pyd('to_build\\aiohttp\\', 'helpers.py')
compile_helper.compile_to_pyd('to_build\\aiohttp\\', 'log.py')
compile_helper.compile_to_pyd('to_build\\aiohttp\\', 'multidict.py')
compile_helper.compile_to_pyd('to_build\\aiohttp\\', 'multipart.py')
compile_helper.compile_to_pyd('to_build\\aiohttp\\', 'parsers.py')
compile_helper.compile_to_pyd('to_build\\aiohttp\\', 'protocol.py')
compile_helper.compile_to_pyd('to_build\\aiohttp\\', 'server.py')
compile_helper.compile_to_pyd('to_build\\aiohttp\\', 'signals.py')
compile_helper.compile_to_pyd('to_build\\aiohttp\\', 'streams.py')
compile_helper.compile_to_pyd('to_build\\aiohttp\\', 'test_utils.py')
compile_helper.compile_to_pyd('to_build\\aiohttp\\', 'web.py')
compile_helper.compile_to_pyd('to_build\\aiohttp\\', 'web_exceptions.py')
compile_helper.compile_to_pyd('to_build\\aiohttp\\', 'web_reqrep.py')
compile_helper.compile_to_pyd('to_build\\aiohttp\\', 'web_urldispatcher.py')
compile_helper.compile_to_pyd('to_build\\aiohttp\\', 'web_ws.py')
compile_helper.compile_to_pyd('to_build\\aiohttp\\', 'websocket.py')
compile_helper.compile_to_pyd('to_build\\aiohttp\\', 'websocket_client.py')
compile_helper.compile_to_pyd('to_build\\aiohttp\\', 'worker.py')
compile_helper.compile_to_pyd('to_build\\aiohttp\\', 'wsgi.py')

# Now lets build cffi to all pyd's.
compile_helper.compile_to_pyd('to_build\\cffi\\', 'api.py')
compile_helper.compile_to_pyd('to_build\\cffi\\', 'backend_ctypes.py')
compile_helper.compile_to_pyd('to_build\\cffi\\', 'cffi_opcode.py')
compile_helper.compile_to_pyd('to_build\\cffi\\', 'commontypes.py')
compile_helper.compile_to_pyd('to_build\\cffi\\', 'cparser.py')
compile_helper.compile_to_pyd('to_build\\cffi\\', 'ffiplatform.py')
compile_helper.compile_to_pyd('to_build\\cffi\\', 'gc_weakref.py')
compile_helper.compile_to_pyd('to_build\\cffi\\', 'lock.py')
compile_helper.compile_to_pyd('to_build\\cffi\\', 'model.py')
compile_helper.compile_to_pyd('to_build\\cffi\\', 'recompiler.py')
compile_helper.compile_to_pyd('to_build\\cffi\\', 'setuptools_ext.py')
compile_helper.compile_to_pyd('to_build\\cffi\\', 'vengine_cpy.py')
compile_helper.compile_to_pyd('to_build\\cffi\\', 'vengine_gen.py')
compile_helper.compile_to_pyd('to_build\\cffi\\', 'verifier.py')

# Now lets build chardet to all pyd's. (Also in requests too)
compile_helper.compile_to_pyd('to_build\\chardet\\', 'big5freq.py')
compile_helper.compile_to_pyd('to_build\\chardet\\', 'big5prober.py')
compile_helper.compile_to_pyd('to_build\\chardet\\', 'chardetect.py')
compile_helper.compile_to_pyd('to_build\\chardet\\', 'chardistribution.py')
compile_helper.compile_to_pyd('to_build\\chardet\\', 'charsetgroupprober.py')
compile_helper.compile_to_pyd('to_build\\chardet\\', 'charsetprober.py')
compile_helper.compile_to_pyd('to_build\\chardet\\', 'codingstatemachine.py')
compile_helper.compile_to_pyd('to_build\\chardet\\', 'compat.py')
compile_helper.compile_to_pyd('to_build\\chardet\\', 'constants.py')
compile_helper.compile_to_pyd('to_build\\chardet\\', 'cp949prober.py')
compile_helper.compile_to_pyd('to_build\\chardet\\', 'escprober.py')
compile_helper.compile_to_pyd('to_build\\chardet\\', 'escsm.py')
compile_helper.compile_to_pyd('to_build\\chardet\\', 'eucjpprober.py')
compile_helper.compile_to_pyd('to_build\\chardet\\', 'euckrfreq.py')
compile_helper.compile_to_pyd('to_build\\chardet\\', 'euckrprober.py')
compile_helper.compile_to_pyd('to_build\\chardet\\', 'euctwfreq.py')
compile_helper.compile_to_pyd('to_build\\chardet\\', 'euctwprober.py')
compile_helper.compile_to_pyd('to_build\\chardet\\', 'gb2312freq.py')
compile_helper.compile_to_pyd('to_build\\chardet\\', 'gb2312prober.py')
compile_helper.compile_to_pyd('to_build\\chardet\\', 'hebrewprober.py')
compile_helper.compile_to_pyd('to_build\\chardet\\', 'jisfreq.py')
compile_helper.compile_to_pyd('to_build\\chardet\\', 'jpcntx.py')
compile_helper.compile_to_pyd('to_build\\chardet\\', 'langbulgarianmodel.py')
compile_helper.compile_to_pyd('to_build\\chardet\\', 'langcyrillicmodel.py')
compile_helper.compile_to_pyd('to_build\\chardet\\', 'langgreekmodel.py')
compile_helper.compile_to_pyd('to_build\\chardet\\', 'langhebrewmodel.py')
compile_helper.compile_to_pyd('to_build\\chardet\\', 'langhungarianmodel.py')
compile_helper.compile_to_pyd('to_build\\chardet\\', 'langthaimodel.py')
compile_helper.compile_to_pyd('to_build\\chardet\\', 'latin1prober.py')
compile_helper.compile_to_pyd('to_build\\chardet\\', 'mbcharsetprober.py')
compile_helper.compile_to_pyd('to_build\\chardet\\', 'mbcsgroupprober.py')
compile_helper.compile_to_pyd('to_build\\chardet\\', 'mbcssm.py')
compile_helper.compile_to_pyd('to_build\\chardet\\', 'sbcharsetprober.py')
compile_helper.compile_to_pyd('to_build\\chardet\\', 'sbcsgroupprober.py')
compile_helper.compile_to_pyd('to_build\\chardet\\', 'sjisprober.py')
compile_helper.compile_to_pyd('to_build\\chardet\\', 'universaldetector.py')
compile_helper.compile_to_pyd('to_build\\chardet\\', 'utf8prober.py')

# Now lets build colorama to all pyd's.
compile_helper.compile_to_pyd('to_build\\colorama\\', 'ansi.py')
compile_helper.compile_to_pyd('to_build\\colorama\\', 'ansitowin32.py')
compile_helper.compile_to_pyd('to_build\\colorama\\', 'initialise.py')
compile_helper.compile_to_pyd('to_build\\colorama\\', 'win32.py')
compile_helper.compile_to_pyd('to_build\\colorama\\', 'winterm.py')

# Now lets build TinyURL to all pyd's.
compile_helper.compile_to_pyd('to_build\\TinyURL\\', 'TinyURL.py')

# Now lets build websockets to all pyd's.
compile_helper.compile_to_pyd('to_build\\websockets\\', 'client.py')
compile_helper.compile_to_pyd('to_build\\websockets\\', 'compatibility.py')
compile_helper.compile_to_pyd('to_build\\websockets\\', 'exceptions.py')
compile_helper.compile_to_pyd('to_build\\websockets\\', 'framing.py')
compile_helper.compile_to_pyd('to_build\\websockets\\', 'handshake.py')
compile_helper.compile_to_pyd('to_build\\websockets\\', 'http.py')
compile_helper.compile_to_pyd('to_build\\websockets\\', 'protocol.py')
compile_helper.compile_to_pyd('to_build\\websockets\\', 'server.py')
compile_helper.compile_to_pyd('to_build\\websockets\\', 'test_client_server.py')
compile_helper.compile_to_pyd('to_build\\websockets\\', 'test_framing.py')
compile_helper.compile_to_pyd('to_build\\websockets\\', 'test_handshake.py')
compile_helper.compile_to_pyd('to_build\\websockets\\', 'test_http.py')
compile_helper.compile_to_pyd('to_build\\websockets\\', 'test_protocol.py')
compile_helper.compile_to_pyd('to_build\\websockets\\', 'test_uri.py')
compile_helper.compile_to_pyd('to_build\\websockets\\', 'uri.py')
compile_helper.compile_to_pyd('to_build\\websockets\\', 'version.py')
compile_helper.compile_to_pyd('to_build\\websockets\\py35\\', 'client.py')
compile_helper.compile_to_pyd('to_build\\websockets\\py35\\', 'client_server.py')

# Now lets build PyNacl to all pyd's.
compile_helper.compile_to_pyd('to_build\\nacl\\', 'encoding.py')
compile_helper.compile_to_pyd('to_build\\nacl\\', 'exceptions.py')
compile_helper.compile_to_pyd('to_build\\nacl\\', 'hash.py')
compile_helper.compile_to_pyd('to_build\\nacl\\', 'public.py')
compile_helper.compile_to_pyd('to_build\\nacl\\', 'secret.py')
compile_helper.compile_to_pyd('to_build\\nacl\\', 'signing.py')
compile_helper.compile_to_pyd('to_build\\nacl\\', 'utils.py')
compile_helper.compile_to_pyd('to_build\\nacl\\bindings\\', 'crypto_box.py')
compile_helper.compile_to_pyd('to_build\\nacl\\bindings\\', 'crypto_hash.py')
compile_helper.compile_to_pyd('to_build\\nacl\\bindings\\', 'crypto_scalarmult.py')
compile_helper.compile_to_pyd('to_build\\nacl\\bindings\\', 'crypto_secretbox.py')
compile_helper.compile_to_pyd('to_build\\nacl\\bindings\\', 'crypto_sign.py')
compile_helper.compile_to_pyd('to_build\\nacl\\bindings\\', 'randombytes.py')
compile_helper.compile_to_pyd('to_build\\nacl\\bindings\\', 'sodium_core.py')

# Now lets build pycparser to all pyd's.
compile_helper.compile_to_pyd('to_build\\pycparser\\', '_ast_gen.py')
compile_helper.compile_to_pyd('to_build\\pycparser\\', '_build_tables.py')
compile_helper.compile_to_pyd('to_build\\pycparser\\', 'ast_transforms.py')
compile_helper.compile_to_pyd('to_build\\pycparser\\', 'c_ast.py')
compile_helper.compile_to_pyd('to_build\\pycparser\\', 'c_generator.py')
compile_helper.compile_to_pyd('to_build\\pycparser\\', 'c_lexer.py')
compile_helper.compile_to_pyd('to_build\\pycparser\\', 'c_parser.py')
compile_helper.compile_to_pyd('to_build\\pycparser\\', 'lextab.py')
compile_helper.compile_to_pyd('to_build\\pycparser\\', 'plyparser.py')
compile_helper.compile_to_pyd('to_build\\pycparser\\', 'yacctab.py')
compile_helper.compile_to_pyd('to_build\\pycparser\\ply\\', 'cpp.py')
compile_helper.compile_to_pyd('to_build\\pycparser\\ply\\', 'ctokens.py')
# Do not try to compile these 2 files.
# compile_helper.compile_to_pyd('to_build\\pycparser\\ply\\', 'lex.py')
# compile_helper.compile_to_pyd('to_build\\pycparser\\ply\\', 'yacc.py')

# Now lets build requests to all pyd's.
compile_helper.compile_to_pyd('to_build\\requests\\', 'adapters.py')
compile_helper.compile_to_pyd('to_build\\requests\\', 'api.py')
compile_helper.compile_to_pyd('to_build\\requests\\', 'auth.py')
compile_helper.compile_to_pyd('to_build\\requests\\', 'certs.py')
compile_helper.compile_to_pyd('to_build\\requests\\', 'compat.py')
compile_helper.compile_to_pyd('to_build\\requests\\', 'cookies.py')
compile_helper.compile_to_pyd('to_build\\requests\\', 'exceptions.py')
compile_helper.compile_to_pyd('to_build\\requests\\', 'hooks.py')
compile_helper.compile_to_pyd('to_build\\requests\\', 'models.py')
compile_helper.compile_to_pyd('to_build\\requests\\', 'sessions.py')
compile_helper.compile_to_pyd('to_build\\requests\\', 'status_codes.py')
compile_helper.compile_to_pyd('to_build\\requests\\', 'structures.py')
compile_helper.compile_to_pyd('to_build\\requests\\', 'utils.py')
compile_helper.compile_to_pyd('to_build\\requests\\packages\\chardet\\', 'big5freq.py')
compile_helper.compile_to_pyd('to_build\\requests\\packages\\chardet\\', 'big5prober.py')
compile_helper.compile_to_pyd('to_build\\requests\\packages\\chardet\\', 'chardetect.py')
compile_helper.compile_to_pyd('to_build\\requests\\packages\\chardet\\', 'chardistribution.py')
compile_helper.compile_to_pyd('to_build\\requests\\packages\\chardet\\', 'charsetgroupprober.py')
compile_helper.compile_to_pyd('to_build\\requests\\packages\\chardet\\', 'charsetprober.py')
compile_helper.compile_to_pyd('to_build\\requests\\packages\\chardet\\', 'codingstatemachine.py')
compile_helper.compile_to_pyd('to_build\\requests\\packages\\chardet\\', 'compat.py')
compile_helper.compile_to_pyd('to_build\\requests\\packages\\chardet\\', 'constants.py')
compile_helper.compile_to_pyd('to_build\\requests\\packages\\chardet\\', 'cp949prober.py')
compile_helper.compile_to_pyd('to_build\\requests\\packages\\chardet\\', 'escprober.py')
compile_helper.compile_to_pyd('to_build\\requests\\packages\\chardet\\', 'escsm.py')
compile_helper.compile_to_pyd('to_build\\requests\\packages\\chardet\\', 'eucjpprober.py')
compile_helper.compile_to_pyd('to_build\\requests\\packages\\chardet\\', 'euckrfreq.py')
compile_helper.compile_to_pyd('to_build\\requests\\packages\\chardet\\', 'euckrprober.py')
compile_helper.compile_to_pyd('to_build\\requests\\packages\\chardet\\', 'euctwfreq.py')
compile_helper.compile_to_pyd('to_build\\requests\\packages\\chardet\\', 'euctwprober.py')
compile_helper.compile_to_pyd('to_build\\requests\\packages\\chardet\\', 'gb2312freq.py')
compile_helper.compile_to_pyd('to_build\\requests\\packages\\chardet\\', 'gb2312prober.py')
compile_helper.compile_to_pyd('to_build\\requests\\packages\\chardet\\', 'hebrewprober.py')
compile_helper.compile_to_pyd('to_build\\requests\\packages\\chardet\\', 'jisfreq.py')
compile_helper.compile_to_pyd('to_build\\requests\\packages\\chardet\\', 'jpcntx.py')
compile_helper.compile_to_pyd('to_build\\requests\\packages\\chardet\\', 'langbulgarianmodel.py')
compile_helper.compile_to_pyd('to_build\\requests\\packages\\chardet\\', 'langcyrillicmodel.py')
compile_helper.compile_to_pyd('to_build\\requests\\packages\\chardet\\', 'langgreekmodel.py')
compile_helper.compile_to_pyd('to_build\\requests\\packages\\chardet\\', 'langhebrewmodel.py')
compile_helper.compile_to_pyd('to_build\\requests\\packages\\chardet\\', 'langhungarianmodel.py')
compile_helper.compile_to_pyd('to_build\\requests\\packages\\chardet\\', 'langthaimodel.py')
compile_helper.compile_to_pyd('to_build\\requests\\packages\\chardet\\', 'latin1prober.py')
compile_helper.compile_to_pyd('to_build\\requests\\packages\\chardet\\', 'mbcharsetprober.py')
compile_helper.compile_to_pyd('to_build\\requests\\packages\\chardet\\', 'mbcsgroupprober.py')
compile_helper.compile_to_pyd('to_build\\requests\\packages\\chardet\\', 'mbcssm.py')
compile_helper.compile_to_pyd('to_build\\requests\\packages\\chardet\\', 'sbcharsetprober.py')
compile_helper.compile_to_pyd('to_build\\requests\\packages\\chardet\\', 'sbcsgroupprober.py')
compile_helper.compile_to_pyd('to_build\\requests\\packages\\chardet\\', 'sjisprober.py')
compile_helper.compile_to_pyd('to_build\\requests\\packages\\chardet\\', 'universaldetector.py')
compile_helper.compile_to_pyd('to_build\\requests\\packages\\chardet\\', 'utf8prober.py')
compile_helper.compile_to_pyd('to_build\\requests\\packages\\urllib3\\', '_collections.py')
compile_helper.compile_to_pyd('to_build\\requests\\packages\\urllib3\\', 'connection.py')
compile_helper.compile_to_pyd('to_build\\requests\\packages\\urllib3\\', 'connectionpool.py')
compile_helper.compile_to_pyd('to_build\\requests\\packages\\urllib3\\', 'exceptions.py')
compile_helper.compile_to_pyd('to_build\\requests\\packages\\urllib3\\', 'fields.py')
compile_helper.compile_to_pyd('to_build\\requests\\packages\\urllib3\\', 'filepost.py')
compile_helper.compile_to_pyd('to_build\\requests\\packages\\urllib3\\', 'poolmanager.py')
compile_helper.compile_to_pyd('to_build\\requests\\packages\\urllib3\\', 'request.py')
compile_helper.compile_to_pyd('to_build\\requests\\packages\\urllib3\\', 'response.py')
compile_helper.compile_to_pyd('to_build\\requests\\packages\\urllib3\\contrib\\', 'appengine.py')
compile_helper.compile_to_pyd('to_build\\requests\\packages\\urllib3\\contrib\\', 'ntlmpool.py')
compile_helper.compile_to_pyd('to_build\\requests\\packages\\urllib3\\contrib\\', 'pyopenssl.py')
compile_helper.compile_to_pyd('to_build\\requests\\packages\\urllib3\\packages\\', 'ordered_dict.py')
compile_helper.compile_to_pyd('to_build\\requests\\packages\\urllib3\\packages\\', 'six.py')
compile_helper.compile_to_pyd('to_build\\requests\\packages\\urllib3\\packages\\ssl_match_hostname\\', '_implementation.py')
compile_helper.compile_to_pyd('to_build\\requests\\packages\\urllib3\\util\\', 'connection.py')
compile_helper.compile_to_pyd('to_build\\requests\\packages\\urllib3\\util\\', 'request.py')
compile_helper.compile_to_pyd('to_build\\requests\\packages\\urllib3\\util\\', 'response.py')
compile_helper.compile_to_pyd('to_build\\requests\\packages\\urllib3\\util\\', 'retry.py')
compile_helper.compile_to_pyd('to_build\\requests\\packages\\urllib3\\util\\', 'ssl_.py')
compile_helper.compile_to_pyd('to_build\\requests\\packages\\urllib3\\util\\', 'timeout.py')
compile_helper.compile_to_pyd('to_build\\requests\\packages\\urllib3\\util\\', 'url.py')

# Now lets build setuptools to all pyd's.
compile_helper.compile_to_pyd('to_build\\setuptools\\', 'archive_util.py')
compile_helper.compile_to_pyd('to_build\\setuptools\\', 'compat.py')
compile_helper.compile_to_pyd('to_build\\setuptools\\', 'depends.py')
compile_helper.compile_to_pyd('to_build\\setuptools\\', 'dist.py')
compile_helper.compile_to_pyd('to_build\\setuptools\\', 'extension.py')
compile_helper.compile_to_pyd('to_build\\setuptools\\', 'launch.py')
compile_helper.compile_to_pyd('to_build\\setuptools\\', 'lib2to3_ex.py')
compile_helper.compile_to_pyd('to_build\\setuptools\\', 'msvc9_support.py')
compile_helper.compile_to_pyd('to_build\\setuptools\\', 'package_index.py')
compile_helper.compile_to_pyd('to_build\\setuptools\\', 'py26compat.py')
compile_helper.compile_to_pyd('to_build\\setuptools\\', 'py27compat.py')
compile_helper.compile_to_pyd('to_build\\setuptools\\', 'py31compat.py')
# compile_helper.compile_to_pyd('to_build\\setuptools\\', 'sandbox.py')
# compile_helper.compile_to_pyd('to_build\\setuptools\\', 'site-patch.py')
compile_helper.compile_to_pyd('to_build\\setuptools\\', 'ssl_support.py')
compile_helper.compile_to_pyd('to_build\\setuptools\\', 'unicode_utils.py')
compile_helper.compile_to_pyd('to_build\\setuptools\\', 'utils.py')
compile_helper.compile_to_pyd('to_build\\setuptools\\', 'version.py')
compile_helper.compile_to_pyd('to_build\\setuptools\\', 'windows_support.py')
compile_helper.compile_to_pyd('to_build\\setuptools\\command\\', 'alias.py')
compile_helper.compile_to_pyd('to_build\\setuptools\\command\\', 'bdist_egg.py')
compile_helper.compile_to_pyd('to_build\\setuptools\\command\\', 'bdist_rpm.py')
compile_helper.compile_to_pyd('to_build\\setuptools\\command\\', 'bdist_wininst.py')
compile_helper.compile_to_pyd('to_build\\setuptools\\command\\', 'build_ext.py')
compile_helper.compile_to_pyd('to_build\\setuptools\\command\\', 'build_py.py')
compile_helper.compile_to_pyd('to_build\\setuptools\\command\\', 'develop.py')
compile_helper.compile_to_pyd('to_build\\setuptools\\command\\', 'easy_install.py')
compile_helper.compile_to_pyd('to_build\\setuptools\\command\\', 'egg_info.py')
compile_helper.compile_to_pyd('to_build\\setuptools\\command\\', 'install.py')
compile_helper.compile_to_pyd('to_build\\setuptools\\command\\', 'install_egg_info.py')
compile_helper.compile_to_pyd('to_build\\setuptools\\command\\', 'install_lib.py')
compile_helper.compile_to_pyd('to_build\\setuptools\\command\\', 'install_scripts.py')
compile_helper.compile_to_pyd('to_build\\setuptools\\command\\', 'register.py')
compile_helper.compile_to_pyd('to_build\\setuptools\\command\\', 'rotate.py')
compile_helper.compile_to_pyd('to_build\\setuptools\\command\\', 'saveopts.py')
compile_helper.compile_to_pyd('to_build\\setuptools\\command\\', 'sdist.py')
compile_helper.compile_to_pyd('to_build\\setuptools\\command\\', 'setopt.py')
compile_helper.compile_to_pyd('to_build\\setuptools\\command\\', 'test.py')
compile_helper.compile_to_pyd('to_build\\setuptools\\command\\', 'upload.py')
compile_helper.compile_to_pyd('to_build\\setuptools\\command\\', 'upload_docs.py')
