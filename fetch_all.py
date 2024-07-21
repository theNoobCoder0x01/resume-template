import re
from pprint import pprint

import requests

urls = ["http://127.0.0.1:5500/assets/fonts/fonts.css"]

cssFileText = ""
cssFileOriginalContent = b""

defualtFileContent = b"""@font-face {
  font-family: 'Poppins';
  font-style: italic;
  font-weight: 100;
  font-display: swap;
  src: url(/assets/fonts/pxiAyp8kv8JHgFVrJJLmE3tF.ttf) format('truetype');
}
@font-face {
  font-family: 'Poppins';
  font-style: italic;
  font-weight: 200;
  font-display: swap;
  src: url(/assets/fonts/pxiDyp8kv8JHgFVrJJLmv1plEA.ttf) format('truetype');
}
@font-face {
  font-family: 'Poppins';
  font-style: italic;
  font-weight: 300;
  font-display: swap;
  src: url(/assets/fonts/pxiDyp8kv8JHgFVrJJLm21llEA.ttf) format('truetype');
}
@font-face {
  font-family: 'Poppins';
  font-style: italic;
  font-weight: 400;
  font-display: swap;
  src: url(/assets/fonts/pxiGyp8kv8JHgFVrJJLedw.ttf) format('truetype');
}
@font-face {
  font-family: 'Poppins';
  font-style: italic;
  font-weight: 500;
  font-display: swap;
  src: url(/assets/fonts/pxiDyp8kv8JHgFVrJJLmg1hlEA.ttf) format('truetype');
}
@font-face {
  font-family: 'Poppins';
  font-style: italic;
  font-weight: 600;
  font-display: swap;
  src: url(/assets/fonts/pxiDyp8kv8JHgFVrJJLmr19lEA.ttf) format('truetype');
}
@font-face {
  font-family: 'Poppins';
  font-style: italic;
  font-weight: 700;
  font-display: swap;
  src: url(/assets/fonts/pxiDyp8kv8JHgFVrJJLmy15lEA.ttf) format('truetype');
}
@font-face {
  font-family: 'Poppins';
  font-style: italic;
  font-weight: 800;
  font-display: swap;
  src: url(/assets/fonts/pxiDyp8kv8JHgFVrJJLm111lEA.ttf) format('truetype');
}
@font-face {
  font-family: 'Poppins';
  font-style: italic;
  font-weight: 900;
  font-display: swap;
  src: url(/assets/fonts/pxiDyp8kv8JHgFVrJJLm81xlEA.ttf) format('truetype');
}
@font-face {
  font-family: 'Poppins';
  font-style: normal;
  font-weight: 100;
  font-display: swap;
  src: url(/assets/fonts/pxiGyp8kv8JHgFVrLPTedw.ttf) format('truetype');
}
@font-face {
  font-family: 'Poppins';
  font-style: normal;
  font-weight: 200;
  font-display: swap;
  src: url(/assets/fonts/pxiByp8kv8JHgFVrLFj_V1s.ttf) format('truetype');
}
@font-face {
  font-family: 'Poppins';
  font-style: normal;
  font-weight: 300;
  font-display: swap;
  src: url(/assets/fonts/pxiByp8kv8JHgFVrLDz8V1s.ttf) format('truetype');
}
@font-face {
  font-family: 'Poppins';
  font-style: normal;
  font-weight: 400;
  font-display: swap;
  src: url(/assets/fonts/pxiEyp8kv8JHgFVrFJA.ttf) format('truetype');
}
@font-face {
  font-family: 'Poppins';
  font-style: normal;
  font-weight: 500;
  font-display: swap;
  src: url(/assets/fonts/pxiByp8kv8JHgFVrLGT9V1s.ttf) format('truetype');
}
@font-face {
  font-family: 'Poppins';
  font-style: normal;
  font-weight: 600;
  font-display: swap;
  src: url(/assets/fonts/pxiByp8kv8JHgFVrLEj6V1s.ttf) format('truetype');
}
@font-face {
  font-family: 'Poppins';
  font-style: normal;
  font-weight: 700;
  font-display: swap;
  src: url(/assets/fonts/pxiByp8kv8JHgFVrLCz7V1s.ttf) format('truetype');
}
@font-face {
  font-family: 'Poppins';
  font-style: normal;
  font-weight: 800;
  font-display: swap;
  src: url(/assets/fonts/pxiByp8kv8JHgFVrLDD4V1s.ttf) format('truetype');
}
@font-face {
  font-family: 'Poppins';
  font-style: normal;
  font-weight: 900;
  font-display: swap;
  src: url(/assets/fonts/pxiByp8kv8JHgFVrLBT5V1s.ttf) format('truetype');
}
/* latin-ext */
@font-face {
  font-family: 'Poppins';
  font-style: italic;
  font-weight: 100;
  font-display: swap;
  src: url(https://fonts.gstatic.com/s/poppins/v21/pxiAyp8kv8JHgFVrJJLmE0tMMPKhSkFEkm8.woff2) format('woff2');
  unicode-range: U+0100-02AF, U+0304, U+0308, U+0329, U+1E00-1E9F, U+1EF2-1EFF, U+2020, U+20A0-20AB, U+20AD-20C0, U+2113, U+2C60-2C7F, U+A720-A7FF;
}
/* latin */
@font-face {
  font-family: 'Poppins';
  font-style: italic;
  font-weight: 100;
  font-display: swap;
  src: url(https://fonts.gstatic.com/s/poppins/v21/pxiAyp8kv8JHgFVrJJLmE0tCMPKhSkFE.woff2) format('woff2');
  unicode-range: U+0000-00FF, U+0131, U+0152-0153, U+02BB-02BC, U+02C6, U+02DA, U+02DC, U+0304, U+0308, U+0329, U+2000-206F, U+2074, U+20AC, U+2122, U+2191, U+2193, U+2212, U+2215, U+FEFF, U+FFFD;
}
/* latin-ext */
@font-face {
  font-family: 'Poppins';
  font-style: italic;
  font-weight: 200;
  font-display: swap;
  src: url(https://fonts.gstatic.com/s/poppins/v21/pxiDyp8kv8JHgFVrJJLmv1pVGdeOYktMqlap.woff2) format('woff2');
  unicode-range: U+0100-02AF, U+0304, U+0308, U+0329, U+1E00-1E9F, U+1EF2-1EFF, U+2020, U+20A0-20AB, U+20AD-20C0, U+2113, U+2C60-2C7F, U+A720-A7FF;
}
/* latin */
@font-face {
  font-family: 'Poppins';
  font-style: italic;
  font-weight: 200;
  font-display: swap;
  src: url(https://fonts.gstatic.com/s/poppins/v21/pxiDyp8kv8JHgFVrJJLmv1pVF9eOYktMqg.woff2) format('woff2');
  unicode-range: U+0000-00FF, U+0131, U+0152-0153, U+02BB-02BC, U+02C6, U+02DA, U+02DC, U+0304, U+0308, U+0329, U+2000-206F, U+2074, U+20AC, U+2122, U+2191, U+2193, U+2212, U+2215, U+FEFF, U+FFFD;
}
/* latin-ext */
@font-face {
  font-family: 'Poppins';
  font-style: italic;
  font-weight: 300;
  font-display: swap;
  src: url(https://fonts.gstatic.com/s/poppins/v21/pxiDyp8kv8JHgFVrJJLm21lVGdeOYktMqlap.woff2) format('woff2');
  unicode-range: U+0100-02AF, U+0304, U+0308, U+0329, U+1E00-1E9F, U+1EF2-1EFF, U+2020, U+20A0-20AB, U+20AD-20C0, U+2113, U+2C60-2C7F, U+A720-A7FF;
}
/* latin */
@font-face {
  font-family: 'Poppins';
  font-style: italic;
  font-weight: 300;
  font-display: swap;
  src: url(https://fonts.gstatic.com/s/poppins/v21/pxiDyp8kv8JHgFVrJJLm21lVF9eOYktMqg.woff2) format('woff2');
  unicode-range: U+0000-00FF, U+0131, U+0152-0153, U+02BB-02BC, U+02C6, U+02DA, U+02DC, U+0304, U+0308, U+0329, U+2000-206F, U+2074, U+20AC, U+2122, U+2191, U+2193, U+2212, U+2215, U+FEFF, U+FFFD;
}
/* latin-ext */
@font-face {
  font-family: 'Poppins';
  font-style: italic;
  font-weight: 400;
  font-display: swap;
  src: url(https://fonts.gstatic.com/s/poppins/v21/pxiGyp8kv8JHgFVrJJLufntAOvWDSHFF.woff2) format('woff2');
  unicode-range: U+0100-02AF, U+0304, U+0308, U+0329, U+1E00-1E9F, U+1EF2-1EFF, U+2020, U+20A0-20AB, U+20AD-20C0, U+2113, U+2C60-2C7F, U+A720-A7FF;
}
/* latin */
@font-face {
  font-family: 'Poppins';
  font-style: italic;
  font-weight: 400;
  font-display: swap;
  src: url(https://fonts.gstatic.com/s/poppins/v21/pxiGyp8kv8JHgFVrJJLucHtAOvWDSA.woff2) format('woff2');
  unicode-range: U+0000-00FF, U+0131, U+0152-0153, U+02BB-02BC, U+02C6, U+02DA, U+02DC, U+0304, U+0308, U+0329, U+2000-206F, U+2074, U+20AC, U+2122, U+2191, U+2193, U+2212, U+2215, U+FEFF, U+FFFD;
}
/* latin-ext */
@font-face {
  font-family: 'Poppins';
  font-style: italic;
  font-weight: 500;
  font-display: swap;
  src: url(https://fonts.gstatic.com/s/poppins/v21/pxiDyp8kv8JHgFVrJJLmg1hVGdeOYktMqlap.woff2) format('woff2');
  unicode-range: U+0100-02AF, U+0304, U+0308, U+0329, U+1E00-1E9F, U+1EF2-1EFF, U+2020, U+20A0-20AB, U+20AD-20C0, U+2113, U+2C60-2C7F, U+A720-A7FF;
}
/* latin */
@font-face {
  font-family: 'Poppins';
  font-style: italic;
  font-weight: 500;
  font-display: swap;
  src: url(https://fonts.gstatic.com/s/poppins/v21/pxiDyp8kv8JHgFVrJJLmg1hVF9eOYktMqg.woff2) format('woff2');
  unicode-range: U+0000-00FF, U+0131, U+0152-0153, U+02BB-02BC, U+02C6, U+02DA, U+02DC, U+0304, U+0308, U+0329, U+2000-206F, U+2074, U+20AC, U+2122, U+2191, U+2193, U+2212, U+2215, U+FEFF, U+FFFD;
}
/* latin-ext */
@font-face {
  font-family: 'Poppins';
  font-style: italic;
  font-weight: 600;
  font-display: swap;
  src: url(https://fonts.gstatic.com/s/poppins/v21/pxiDyp8kv8JHgFVrJJLmr19VGdeOYktMqlap.woff2) format('woff2');
  unicode-range: U+0100-02AF, U+0304, U+0308, U+0329, U+1E00-1E9F, U+1EF2-1EFF, U+2020, U+20A0-20AB, U+20AD-20C0, U+2113, U+2C60-2C7F, U+A720-A7FF;
}
/* latin */
@font-face {
  font-family: 'Poppins';
  font-style: italic;
  font-weight: 600;
  font-display: swap;
  src: url(https://fonts.gstatic.com/s/poppins/v21/pxiDyp8kv8JHgFVrJJLmr19VF9eOYktMqg.woff2) format('woff2');
  unicode-range: U+0000-00FF, U+0131, U+0152-0153, U+02BB-02BC, U+02C6, U+02DA, U+02DC, U+0304, U+0308, U+0329, U+2000-206F, U+2074, U+20AC, U+2122, U+2191, U+2193, U+2212, U+2215, U+FEFF, U+FFFD;
}
/* latin-ext */
@font-face {
  font-family: 'Poppins';
  font-style: italic;
  font-weight: 700;
  font-display: swap;
  src: url(https://fonts.gstatic.com/s/poppins/v21/pxiDyp8kv8JHgFVrJJLmy15VGdeOYktMqlap.woff2) format('woff2');
  unicode-range: U+0100-02AF, U+0304, U+0308, U+0329, U+1E00-1E9F, U+1EF2-1EFF, U+2020, U+20A0-20AB, U+20AD-20C0, U+2113, U+2C60-2C7F, U+A720-A7FF;
}
/* latin */
@font-face {
  font-family: 'Poppins';
  font-style: italic;
  font-weight: 700;
  font-display: swap;
  src: url(https://fonts.gstatic.com/s/poppins/v21/pxiDyp8kv8JHgFVrJJLmy15VF9eOYktMqg.woff2) format('woff2');
  unicode-range: U+0000-00FF, U+0131, U+0152-0153, U+02BB-02BC, U+02C6, U+02DA, U+02DC, U+0304, U+0308, U+0329, U+2000-206F, U+2074, U+20AC, U+2122, U+2191, U+2193, U+2212, U+2215, U+FEFF, U+FFFD;
}
/* latin-ext */
@font-face {
  font-family: 'Poppins';
  font-style: italic;
  font-weight: 800;
  font-display: swap;
  src: url(https://fonts.gstatic.com/s/poppins/v21/pxiDyp8kv8JHgFVrJJLm111VGdeOYktMqlap.woff2) format('woff2');
  unicode-range: U+0100-02AF, U+0304, U+0308, U+0329, U+1E00-1E9F, U+1EF2-1EFF, U+2020, U+20A0-20AB, U+20AD-20C0, U+2113, U+2C60-2C7F, U+A720-A7FF;
}
/* latin */
@font-face {
  font-family: 'Poppins';
  font-style: italic;
  font-weight: 800;
  font-display: swap;
  src: url(https://fonts.gstatic.com/s/poppins/v21/pxiDyp8kv8JHgFVrJJLm111VF9eOYktMqg.woff2) format('woff2');
  unicode-range: U+0000-00FF, U+0131, U+0152-0153, U+02BB-02BC, U+02C6, U+02DA, U+02DC, U+0304, U+0308, U+0329, U+2000-206F, U+2074, U+20AC, U+2122, U+2191, U+2193, U+2212, U+2215, U+FEFF, U+FFFD;
}
/* latin-ext */
@font-face {
  font-family: 'Poppins';
  font-style: italic;
  font-weight: 900;
  font-display: swap;
  src: url(https://fonts.gstatic.com/s/poppins/v21/pxiDyp8kv8JHgFVrJJLm81xVGdeOYktMqlap.woff2) format('woff2');
  unicode-range: U+0100-02AF, U+0304, U+0308, U+0329, U+1E00-1E9F, U+1EF2-1EFF, U+2020, U+20A0-20AB, U+20AD-20C0, U+2113, U+2C60-2C7F, U+A720-A7FF;
}
/* latin */
@font-face {
  font-family: 'Poppins';
  font-style: italic;
  font-weight: 900;
  font-display: swap;
  src: url(https://fonts.gstatic.com/s/poppins/v21/pxiDyp8kv8JHgFVrJJLm81xVF9eOYktMqg.woff2) format('woff2');
  unicode-range: U+0000-00FF, U+0131, U+0152-0153, U+02BB-02BC, U+02C6, U+02DA, U+02DC, U+0304, U+0308, U+0329, U+2000-206F, U+2074, U+20AC, U+2122, U+2191, U+2193, U+2212, U+2215, U+FEFF, U+FFFD;
}
/* latin-ext */
@font-face {
  font-family: 'Poppins';
  font-style: normal;
  font-weight: 100;
  font-display: swap;
  src: url(https://fonts.gstatic.com/s/poppins/v21/pxiGyp8kv8JHgFVrLPTufntAOvWDSHFF.woff2) format('woff2');
  unicode-range: U+0100-02AF, U+0304, U+0308, U+0329, U+1E00-1E9F, U+1EF2-1EFF, U+2020, U+20A0-20AB, U+20AD-20C0, U+2113, U+2C60-2C7F, U+A720-A7FF;
}
/* latin */
@font-face {
  font-family: 'Poppins';
  font-style: normal;
  font-weight: 100;
  font-display: swap;
  src: url(https://fonts.gstatic.com/s/poppins/v21/pxiGyp8kv8JHgFVrLPTucHtAOvWDSA.woff2) format('woff2');
  unicode-range: U+0000-00FF, U+0131, U+0152-0153, U+02BB-02BC, U+02C6, U+02DA, U+02DC, U+0304, U+0308, U+0329, U+2000-206F, U+2074, U+20AC, U+2122, U+2191, U+2193, U+2212, U+2215, U+FEFF, U+FFFD;
}
/* latin-ext */
@font-face {
  font-family: 'Poppins';
  font-style: normal;
  font-weight: 200;
  font-display: swap;
  src: url(https://fonts.gstatic.com/s/poppins/v21/pxiByp8kv8JHgFVrLFj_Z1JlFd2JQEl8qw.woff2) format('woff2');
  unicode-range: U+0100-02AF, U+0304, U+0308, U+0329, U+1E00-1E9F, U+1EF2-1EFF, U+2020, U+20A0-20AB, U+20AD-20C0, U+2113, U+2C60-2C7F, U+A720-A7FF;
}
/* latin */
@font-face {
  font-family: 'Poppins';
  font-style: normal;
  font-weight: 200;
  font-display: swap;
  src: url(https://fonts.gstatic.com/s/poppins/v21/pxiByp8kv8JHgFVrLFj_Z1xlFd2JQEk.woff2) format('woff2');
  unicode-range: U+0000-00FF, U+0131, U+0152-0153, U+02BB-02BC, U+02C6, U+02DA, U+02DC, U+0304, U+0308, U+0329, U+2000-206F, U+2074, U+20AC, U+2122, U+2191, U+2193, U+2212, U+2215, U+FEFF, U+FFFD;
}
/* latin-ext */
@font-face {
  font-family: 'Poppins';
  font-style: normal;
  font-weight: 300;
  font-display: swap;
  src: url(https://fonts.gstatic.com/s/poppins/v21/pxiByp8kv8JHgFVrLDz8Z1JlFd2JQEl8qw.woff2) format('woff2');
  unicode-range: U+0100-02AF, U+0304, U+0308, U+0329, U+1E00-1E9F, U+1EF2-1EFF, U+2020, U+20A0-20AB, U+20AD-20C0, U+2113, U+2C60-2C7F, U+A720-A7FF;
}
/* latin */
@font-face {
  font-family: 'Poppins';
  font-style: normal;
  font-weight: 300;
  font-display: swap;
  src: url(https://fonts.gstatic.com/s/poppins/v21/pxiByp8kv8JHgFVrLDz8Z1xlFd2JQEk.woff2) format('woff2');
  unicode-range: U+0000-00FF, U+0131, U+0152-0153, U+02BB-02BC, U+02C6, U+02DA, U+02DC, U+0304, U+0308, U+0329, U+2000-206F, U+2074, U+20AC, U+2122, U+2191, U+2193, U+2212, U+2215, U+FEFF, U+FFFD;
}
/* latin-ext */
@font-face {
  font-family: 'Poppins';
  font-style: normal;
  font-weight: 400;
  font-display: swap;
  src: url(https://fonts.gstatic.com/s/poppins/v21/pxiEyp8kv8JHgFVrJJnecnFHGPezSQ.woff2) format('woff2');
  unicode-range: U+0100-02AF, U+0304, U+0308, U+0329, U+1E00-1E9F, U+1EF2-1EFF, U+2020, U+20A0-20AB, U+20AD-20C0, U+2113, U+2C60-2C7F, U+A720-A7FF;
}
/* latin */
@font-face {
  font-family: 'Poppins';
  font-style: normal;
  font-weight: 400;
  font-display: swap;
  src: url(https://fonts.gstatic.com/s/poppins/v21/pxiEyp8kv8JHgFVrJJfecnFHGPc.woff2) format('woff2');
  unicode-range: U+0000-00FF, U+0131, U+0152-0153, U+02BB-02BC, U+02C6, U+02DA, U+02DC, U+0304, U+0308, U+0329, U+2000-206F, U+2074, U+20AC, U+2122, U+2191, U+2193, U+2212, U+2215, U+FEFF, U+FFFD;
}
/* latin-ext */
@font-face {
  font-family: 'Poppins';
  font-style: normal;
  font-weight: 500;
  font-display: swap;
  src: url(https://fonts.gstatic.com/s/poppins/v21/pxiByp8kv8JHgFVrLGT9Z1JlFd2JQEl8qw.woff2) format('woff2');
  unicode-range: U+0100-02AF, U+0304, U+0308, U+0329, U+1E00-1E9F, U+1EF2-1EFF, U+2020, U+20A0-20AB, U+20AD-20C0, U+2113, U+2C60-2C7F, U+A720-A7FF;
}
/* latin */
@font-face {
  font-family: 'Poppins';
  font-style: normal;
  font-weight: 500;
  font-display: swap;
  src: url(https://fonts.gstatic.com/s/poppins/v21/pxiByp8kv8JHgFVrLGT9Z1xlFd2JQEk.woff2) format('woff2');
  unicode-range: U+0000-00FF, U+0131, U+0152-0153, U+02BB-02BC, U+02C6, U+02DA, U+02DC, U+0304, U+0308, U+0329, U+2000-206F, U+2074, U+20AC, U+2122, U+2191, U+2193, U+2212, U+2215, U+FEFF, U+FFFD;
}
/* latin-ext */
@font-face {
  font-family: 'Poppins';
  font-style: normal;
  font-weight: 600;
  font-display: swap;
  src: url(https://fonts.gstatic.com/s/poppins/v21/pxiByp8kv8JHgFVrLEj6Z1JlFd2JQEl8qw.woff2) format('woff2');
  unicode-range: U+0100-02AF, U+0304, U+0308, U+0329, U+1E00-1E9F, U+1EF2-1EFF, U+2020, U+20A0-20AB, U+20AD-20C0, U+2113, U+2C60-2C7F, U+A720-A7FF;
}
/* latin */
@font-face {
  font-family: 'Poppins';
  font-style: normal;
  font-weight: 600;
  font-display: swap;
  src: url(https://fonts.gstatic.com/s/poppins/v21/pxiByp8kv8JHgFVrLEj6Z1xlFd2JQEk.woff2) format('woff2');
  unicode-range: U+0000-00FF, U+0131, U+0152-0153, U+02BB-02BC, U+02C6, U+02DA, U+02DC, U+0304, U+0308, U+0329, U+2000-206F, U+2074, U+20AC, U+2122, U+2191, U+2193, U+2212, U+2215, U+FEFF, U+FFFD;
}
/* latin-ext */
@font-face {
  font-family: 'Poppins';
  font-style: normal;
  font-weight: 700;
  font-display: swap;
  src: url(https://fonts.gstatic.com/s/poppins/v21/pxiByp8kv8JHgFVrLCz7Z1JlFd2JQEl8qw.woff2) format('woff2');
  unicode-range: U+0100-02AF, U+0304, U+0308, U+0329, U+1E00-1E9F, U+1EF2-1EFF, U+2020, U+20A0-20AB, U+20AD-20C0, U+2113, U+2C60-2C7F, U+A720-A7FF;
}
/* latin */
@font-face {
  font-family: 'Poppins';
  font-style: normal;
  font-weight: 700;
  font-display: swap;
  src: url(https://fonts.gstatic.com/s/poppins/v21/pxiByp8kv8JHgFVrLCz7Z1xlFd2JQEk.woff2) format('woff2');
  unicode-range: U+0000-00FF, U+0131, U+0152-0153, U+02BB-02BC, U+02C6, U+02DA, U+02DC, U+0304, U+0308, U+0329, U+2000-206F, U+2074, U+20AC, U+2122, U+2191, U+2193, U+2212, U+2215, U+FEFF, U+FFFD;
}
/* latin-ext */
@font-face {
  font-family: 'Poppins';
  font-style: normal;
  font-weight: 800;
  font-display: swap;
  src: url(https://fonts.gstatic.com/s/poppins/v21/pxiByp8kv8JHgFVrLDD4Z1JlFd2JQEl8qw.woff2) format('woff2');
  unicode-range: U+0100-02AF, U+0304, U+0308, U+0329, U+1E00-1E9F, U+1EF2-1EFF, U+2020, U+20A0-20AB, U+20AD-20C0, U+2113, U+2C60-2C7F, U+A720-A7FF;
}
/* latin */
@font-face {
  font-family: 'Poppins';
  font-style: normal;
  font-weight: 800;
  font-display: swap;
  src: url(https://fonts.gstatic.com/s/poppins/v21/pxiByp8kv8JHgFVrLDD4Z1xlFd2JQEk.woff2) format('woff2');
  unicode-range: U+0000-00FF, U+0131, U+0152-0153, U+02BB-02BC, U+02C6, U+02DA, U+02DC, U+0304, U+0308, U+0329, U+2000-206F, U+2074, U+20AC, U+2122, U+2191, U+2193, U+2212, U+2215, U+FEFF, U+FFFD;
}
/* latin-ext */
@font-face {
  font-family: 'Poppins';
  font-style: normal;
  font-weight: 900;
  font-display: swap;
  src: url(https://fonts.gstatic.com/s/poppins/v21/pxiByp8kv8JHgFVrLBT5Z1JlFd2JQEl8qw.woff2) format('woff2');
  unicode-range: U+0100-02AF, U+0304, U+0308, U+0329, U+1E00-1E9F, U+1EF2-1EFF, U+2020, U+20A0-20AB, U+20AD-20C0, U+2113, U+2C60-2C7F, U+A720-A7FF;
}
/* latin */
@font-face {
  font-family: 'Poppins';
  font-style: normal;
  font-weight: 900;
  font-display: swap;
  src: url(https://fonts.gstatic.com/s/poppins/v21/pxiByp8kv8JHgFVrLBT5Z1xlFd2JQEk.woff2) format('woff2');
  unicode-range: U+0000-00FF, U+0131, U+0152-0153, U+02BB-02BC, U+02C6, U+02DA, U+02DC, U+0304, U+0308, U+0329, U+2000-206F, U+2074, U+20AC, U+2122, U+2191, U+2193, U+2212, U+2215, U+FEFF, U+FFFD;
}"""
# defualtFileContent = bytes(defualtFileContent)

while len(urls) > 0:
    print("fetching")
    url = urls.pop(0)
    response = requests.get(url)
    if response.status_code == 200:
        fileContent = response.content
    else:
        fileContent = defualtFileContent

    print("fetched", fileContent)
    fileName = f'./assets/fonts/{url.split("/")[-1]}'

    if url.endswith("woff2") or url.endswith("ttf"):
        with open(fileName, "wb") as woffFile:
            woffFile.write(fileContent)
    else:
        cssFileOriginalContent = fileContent
        cssFileOriginalText = fileContent.decode()
        cssFileText = f"{cssFileOriginalText}"

        # Regular expression to match the URL
        url_pattern = re.compile(r"url\((https?://[^\)]+)\)")

        # Find all matches
        for matchedUrl in [i for i in url_pattern.finditer(cssFileOriginalText)][::-1]:
            fileLink = cssFileText[matchedUrl.start() + 4 : matchedUrl.end() - 1]
            print(matchedUrl.start(), ":", matchedUrl.end())
            print(fileLink)
            print()
            urls.append(fileLink)
            cssFileText = cssFileText.replace(
                fileLink,
                f'./{fileLink.split("/")[-1]}',
            )

    with open("./assets/fonts/fonts.css", "w") as fontImportCSS:
        fontImportCSS.write(cssFileText)
    with open("poppins-original.css", "wb") as fontImportCSS:
        fontImportCSS.write(cssFileOriginalContent)
