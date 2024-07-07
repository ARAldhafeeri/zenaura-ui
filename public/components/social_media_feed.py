from zenaura.ui.common import A, Image, OL, LI, Header1, Header2, Paragraph, Div, Span, NavItemText, NavItemIcon, HR, ButtonWithAttrsChildren
from zenaura.client.tags.builder import Builder
from zenaura.ui.input import Input
from zenaura.ui.button import Button
from zenaura.ui.card import Card
from zenaura.ui.badge import Badge

from zenaura.ui.select import Select, Option
from public.styles import with_theme_colors, with_theme_colors_text_no_hover, btn_one_class, btn_two_class

left_side_bar = with_theme_colors("text-light-white")
text = with_theme_colors_text_no_hover("")

def Header2(text, class_name):
    return Builder('h3').with_text(text).with_attribute('class', class_name).build()

def ListItem(class_name, children):
    return Builder("li").with_children(*children).with_class(class_name).build()

def TopNavControl(img_src, text):
    return ButtonWithAttrsChildren("", {}, [
      Div("flex flex-col px-1 items-center hover:bg-light-green rounded", [
          Image(img_src, "", "", "", "w-5 h-5 bg-gray-200 rounded-full"),
          Span("text-xs", text)
      ])
    ])

# Top Bar
top_bar = Div("flex justify-between items-center p-4 bg-light-white1 dark:bg-dark-gray1", [
    Header1("Linkedout", text + " text-2xl"),
    Div("flex items-center space-x-4", [
        Input("", {"placeholder": "Search..."}),
        Div("flex items-center space-x-4", [
            TopNavControl("./public/imgs/home.png", "Home"),
            TopNavControl("./public/imgs/networking.png", "Network"),
            TopNavControl("./public/imgs/job-seeker.png", "Jobs"),
            TopNavControl("./public/imgs/conversation.png", "Messages"),
            TopNavControl("./public/imgs/notification.png", "Notification"),
        ]),
        Button(btn_one_class, "Logout")
    ])
])

def ViewersImpressions():
    return Card( [
        Div("flex justify-between", [
            Div("", [
                Span("text-xs", "Vistors"),
                Span("text-xs text-light-green dark:text-dark-page1 ml-4", "97")
            ]),
            Div("", [
                Span("text-xs", "Impressions"),
                Span("text-xs text-light-green dark:text-dark-page1 ml-4", "321")
            ]),
        ]),
        Div("m-2", [
            HR()
        ]),
         Div("flex flex-wrap", [
            Div("w-2/5", [
                FeedControl("./public/imgs/like.png", "Liked"),
                FeedControl("./public/imgs/repost.png", "Saved"),
            ]),
            Div("w-3/5", [
                FeedControl("./public/imgs/chat.png", "My Comments"),
                FeedControl("./public/imgs/networking.png", "Groups"),
            ]),


        ])
    ], {})

def ProfileCard():
    return Card([
        Div("flex items-center", [
            # Avatar section
            Div("w-16 h-16 mr-4", [
                Image("./public/imgs/female.png", "", "", "", "w-11 h-11 bg-gray-200 rounded-full")
            ]),
            # Name, Title, and Location section
            Div("", [
                Span("text-lg font-semibold", "John Doe"),  # Name
                Div("", [
                    Span("text-sm text-gray-500", "Software Engineer")  # Title
                ]),
                Div("", [
                    Span("text-xs text-gray-400", "Berlin, Germany")  # Location
                ])
            ]),
        ]),
    ], {},  "shadow w-64 mb-2 px-2.5 py-0.5 bg-light-white dark:bg-light-green rounded" )

def FeedControl(img_src, text):
    return ButtonWithAttrsChildren("rounded-lg hover:bg-light-white2 dark:hover:bg-light-green", {}, [
                Div("flex flex-row px-1", [
                    Image(img_src, "", "", "", "w-5 h-5 bg-gray-200 rounded-full"),
                    Span("ml-2 text-xs", text)
                ])
            ])

# Left Sidebar
left_sidebar = Div("w-2/6 p-4 bg-light-white2 dark:bg-dark-gray1", [
    ProfileCard(),
    ViewersImpressions()
])

# Right Sidebar
right_sidebar = Div("w-1/5 p-4 bg-light-white2 dark:bg-dark-gray1", [
    Header2("Trending", text + " mb-4 text-2xl"),
    OL([
        ListItem("mb-2 p-2", [Button(btn_one_class, "Trending Topic 1")]),
        ListItem("mb-2 p-2", [Button(btn_one_class, "Trending Topic 1")]),
        ListItem("mb-2 p-2", [Button(btn_one_class, "Trending Topic 1")]),
    ], {})
])


# Feed Item
def FeedItem(username, time, content, likes, comments, reposts, image_src=None ):
    return Card([
        Div("flex items-center space-x-4", [
            Image("./public/imgs/female.png", "", "", "", "w-10 h-10 bg-gray-200 rounded-full"),
            Div("flex flex-col", [
                Header2(username, text + " text-xl font-bold"),
                Span(text, time),
            ])
        ]),
        Paragraph(content, text + " mt-4"),
        Image(image_src, "", "", "", "mt-4 rounded") if image_src else "",

        Div("flex justify-between mt-4", [
          Span("text-xs", str(likes) + " likes"), 
          Div("mt-2, mb-2", [
            Span("text-xs", str(comments) + " comment"),
            Span("text-xs", " | "),
            Span("text-xs", str(reposts) + " repost")
          ])
        ]),
        Div("mt-2 mb-2", [
            HR()
        ]),
        Div("flex justify-between", [
          FeedControl("./public/imgs/like.png", "Like"),
          FeedControl("./public/imgs/chat.png", "Comment"),
          FeedControl("./public/imgs/share.png", "Share"),
        ])
    ], {}, "shadow w-full mb-4 px-4 py-6 bg-light-white rounded dark:bg-dark-gray2")

# Main Feed
main_feed = Div("w-3/5 p-6 overflow-y-auto rounded bg-light-white2 dark:bg-dark-gray1 rounded-lg", [
    FeedItem("User1", "2h ago", "This is a sample post content. Just sharing some thoughts!",15,23,19),
    FeedItem("User2", "4h ago", "Check out this amazing view!",11,2,3, "./public/imgs/sample_image.png"),
    FeedItem("User3", "6h ago", "Had a great day today! #blessed",3,21,221),
])

# Final Layout
social_media_layout = Div("flex flex-col h-screen bg-light-white2 dark:bg-dark-gray1", [
    top_bar,
    Div("flex flex-grow", [left_sidebar, main_feed, right_sidebar])
])
