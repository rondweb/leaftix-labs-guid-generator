from pywebio.input import *
from pywebio.output import *
from pywebio.platform.flask import webio_view
from flask import Flask

app = Flask(__name__)


def generate_guid():
    import uuid

    put_html("<h1>UUID GENERATOR<h1>")
    put_text(
        "A universally unique identifier (UUID) is a 128-bit label used for information in computer systems. The term globally unique identifier (GUID) is also used. When generated according to the standard methods, UUIDs are, for practical purposes, unique. Their uniqueness does not depend on a central registration authority or coordination between the parties generating them, unlike most other numbering schemes. While the probability that a UUID will be duplicated is not zero, it is close enough to zero to be negligible. Thus, anyone can create a UUID and use it to identify something with near certainty that the identifier does not duplicate one that has already been, or will be, created to identify something else. Information labeled with UUIDs by independent parties can therefore be later combined into a single database or transmitted on the same channel, with a negligible probability of duplication. Adoption of UUIDs is widespread, with many computing platforms providing support for generating them and for parsing their textual representation. REFERENCE:https://en.wikipedia.org/wiki/Universally_unique_identifier"
    )
    xtimes = select("Generate UUIDs", [1, 2, 5, 7])
    lst = [str(uuid.uuid4()) + "<br/>" for x in range(xtimes)]
    put_table([["UUIDs Generated", put_html(" ".join(lst))]])


app.add_url_rule(
    "/", "webio_view", webio_view(generate_guid), methods=["GET", "POST", "OPTIONS"]
)
app.run(host="0.0.0.0", port=80)
