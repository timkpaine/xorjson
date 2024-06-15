# SPDX-License-Identifier: (Apache-2.0 OR MIT)

import xorjson

xorjson.JSONDecodeError(msg="the_msg", doc="the_doc", pos=1)

xorjson.dumps(xorjson.Fragment(b"{}"))
