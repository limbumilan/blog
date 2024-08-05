import requests
import streamlit as st
from streamlit_lottie import st_lottie
from PIL import Image



# Find more emojis here: https://www.webfx.com/tools/emoji-cheat-sheet/
st.set_page_config(page_title="My Webpage", page_icon=":tada:", layout="wide")

st.sidebar.success("Select a page above.")



def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


# Use local CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


local_css("style/style.css")

# ---- LOAD ASSETS ----
lottie_coding = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_fcfjwiyb.json")
img_contact_form = Image.open("images/first.jpg")
img_lottie_animation = Image.open("images/ramri.jpg")

# ---- HEADER SECTION ----
with st.container():
    st.subheader("Hi, Anjana  :wave:")
    st.title("I will always love you...from milan")
    st.write(
        "I came up with an idea to surprise you in our 1st anniversary(2081-04-19) by messaging via website. But things were slower and I could not buid it in that day. I'm sorry for the delay."
    )
    st.write("Please!! म बाट धेरै गल्ति हुन्छन माफ गर्नु है।")

# ---- WHAT I DO ----
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("first date")
        st.write("##")
        st.write(
            """
            I was too Afraid to see you so near to me. How do i express, mix of excitement and nerves?
            I felt a bit of pressure to make a good impression. Maile timro hand hold gareko ta yaad xa ni oi!!????
            ma kaami raheko thye varai samma, body shake vairako thyu. tmlai thaha xa ni? first ma dekhda nai out dress
            ma kahile dekheko thiyena i was so shocked. jirringa thyu mero sarir ta. tyo bela hjurko ankha dekhna layak thyu maybe, 
            timi pani lajako nai thyu hola. 
            """

        )
        
    with right_column:
        st_lottie(lottie_coding, height=300, key="coding")

# ---- PROJECTS ----
with st.container():
    st.write("---")
    st.header("मेरो माया")
    st.write("##")
    image_column, text_column = st.columns((1, 2))
    with image_column:
        
        st.image(img_contact_form)
        st.image()
    with text_column:
        st.subheader("cutiePie")
        st.write(
            """
            my seuci budi!!. it is just the begining. I wanna live my life with you. may i find ways to
            love you more and more. How can i define my love to you budi. Presents kehi navayeni letter chai ramro patham
            vaneko late vayo. sorry!!. please stay with me in my rise and fall. ma maya garxu budi timlai tmle socheko vanda
            dherai. 
            """
        )
        
with st.container():
    image_column, text_column = st.columns((1, 2))
    
with text_column:
        st.subheader("")
        st.write(
            
        )
        

# ---- CONTACT ----
with st.container():
    st.write("---")
    st.header("केहि भन्ने भए हुन्छ है, बुडु...")
    st.write("##")

    # Documention: https://formsubmit.co/ !!! CHANGE EMAIL ADDRESS !!!
    contact_form = """
    <form action="https://formsubmit.co/subbapiyush776@gmail.com" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <textarea name="message" placeholder="your message here" required></textarea>
        <button type="submit">Send</button>
    </form>
    """
    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        st.empty()