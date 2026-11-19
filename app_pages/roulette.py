"""Mock roulette table (European, single zero). Play money only.

The game runs entirely in the browser (roulette_table.html) so chips can be
dragged onto the felt; Streamlit just hosts it.
"""

from pathlib import Path

import streamlit as st
import streamlit.components.v1 as components

TABLE_HTML = (Path(__file__).parent / "roulette_table.html").read_text()

st.title("🎰 Roulette")
st.caption("A mock European roulette table. Drag chips onto the felt and spin. Play money only.")

components.html(TABLE_HTML, height=640, scrolling=True)

with st.expander("Payouts"):
    st.markdown(
        """
| Bet | Pays |
|---|---|
| Single number (0 to 36) | 35 to 1 |
| Dozen (1st / 2nd / 3rd 12) or Column (2 to 1) | 2 to 1 |
| Red / Black, Odd / Even, 1 to 18 / 19 to 36 | 1 to 1 |

Zero loses every outside bet.
"""
    )
