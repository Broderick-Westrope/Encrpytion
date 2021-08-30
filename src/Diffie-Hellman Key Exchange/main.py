import Endpoint

message = "This is a very secret message!!!"

s_public = 197
s_private = 199

m_public = 151
m_private = 157

Sadat = Endpoint(s_public, m_public, s_private)
Michael = Endpoint(s_public, m_public, m_private)
