import streamlit as st

def social_icons(width=24, height=24, **kwargs):
    icon_template = '''
    <a href="{url}" target="_blank" style="margin-right: 20px;">
        <img src="{icon_src}" alt="{alt_text}" width="{width}" height="{height}">
    </a>
    '''

    icons_html = ""
    for name, url in kwargs.items():
        icon_src = {
            "linkedin": "https://www.pinclipart.com/picdir/big/574-5743993_linkedin-icon-white-png-clipart.png",
            "github": "https://www.pinclipart.com/picdir/big/158-1581614_github-clipart.png",
        }.get(name.lower())

        if icon_src:
            icons_html += icon_template.format(url=url, icon_src=icon_src, alt_text=name.capitalize(), width=width, height=height)
    return icons_html

def add_footer():
    """Add a consistent footer to all pages"""
    import streamlit as st
    
    footer_html = """
    <style>
    .footer {
        position: fixed;
        left: 0;
        bottom: 0;
        width: 100%;
        background: linear-gradient(135deg, #1a1a2e 0%, #16213e 100%);
        padding: 12px 20px;
        text-align: center;
        font-size: 0.8em;
        color: #888;
        border-top: 1px solid rgba(230, 57, 70, 0.3);
        z-index: 999;
    }
    .footer a {
        color: #e63946;
        text-decoration: none;
    }
    .footer a:hover {
        text-decoration: underline;
    }
    .footer-icon {
        font-size: 1em;
        margin: 0 3px;
    }
    </style>
    <div class="footer">
        <span class="footer-icon">🤖</span> 
        <strong>AI-Assisted Portfolio</strong> — Built with 
        <a href="https://streamlit.io/" target="_blank">Streamlit</a> + 
        <a href="https://github.com/features/copilot" target="_blank">GitHub Copilot</a> 
        (Claude Opus 4.5)
        <span class="footer-icon">⚡</span>
        <br>
        <small>
            I'm an embedded systems engineer, not a web developer — so I orchestrated this fast & easy with AI assistance.
            <br>
            Template forked from <a href="https://github.com/issamjebnouni" target="_blank">issamjebnouni</a> 🙏
        </small>
    </div>
    """
    st.markdown(footer_html, unsafe_allow_html=True)


