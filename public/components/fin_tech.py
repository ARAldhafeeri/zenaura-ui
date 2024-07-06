from zenaura.ui.common import A, Image, OL, LI, Header1, Header2, Paragraph, Div, Span, NavItemText, NavItemIcon
from zenaura.client.tags.builder import Builder
from zenaura.ui.input import Input
from zenaura.ui.button import Button
from zenaura.ui.badge import Badge
from zenaura.ui.card import Card
from public.styles import with_theme_colors, with_theme_colors_text_no_hover, btn_one_class



left_side_bar = with_theme_colors("text-light-white")
text = with_theme_colors_text_no_hover("")
def Header3(text, class_name):
    return Builder('h3').with_text(text).with_attribute('class', class_name).build()

def ListItem(class_name, children):
    return Builder("li").with_children(*children).with_class(class_name).build()
# nav Item 
sidebar = Div("w-1/5  h-3/5 bg-light-gray2 dark:bg-dark-gray2 rounded min-h-screen text-white p-4", [
    Header3("ezx bank", "text-2xl font-bold mb-8 text-light-white dark:text-dark-page1"),
    OL([
      LI(NavItemText("#", "Dashboard",left_side_bar), {"class": "mb-4"}),
      LI(NavItemText("#","Transaction",  left_side_bar), {"class": "mb-4"}),
      LI(NavItemText("#", "Payment", left_side_bar), {"class": "mb-4"}),
      LI(NavItemText("#", "Card", left_side_bar), {"class": "mb-4"}),
      LI(NavItemText("#", "Insights", left_side_bar), {"class": "mb-4"}),
      LI(NavItemText("#", "Settings", left_side_bar), {"class": "mb-4"}),
      LI(NavItemText("#", "Logout", left_side_bar), {"class": "mb-4"}),
    ], {})
])

# Main Content
main_content = Div("w-4/5 p-6 h-3/5", [
    Div("flex justify-between items-center mb-8", [
        Header2("Dashboard", text),
        Div("flex items-center space-x-4", [
            Div("relative", [
                Input("", {"placeholder": "Search" }, "bg-gray-200 rounded-full py-2 px-4"),
                Span("absolute inset-y-0 right-0 flex items-center pr-3")
            ]),
            Div("flex items-center space-x-2", [
                NavItemIcon("#", Image("./public/imgs/bell.png", "", "15", "15", "w-8 h-8 bg-gray-400 rounded-full")),
                NavItemIcon("#", Image("./public/imgs/profile.png", "", "15", "15", "w-8 h-8 bg-gray-400 rounded-full"))

            ])
        ])
    ]),
    Div("grid grid-cols-4 gap-2 mb-8", [
        Div("p-4 bg-white rounded shadow", [
            Paragraph("Balance", text),
            Header3("$3,596", text + " text-2xl  font-bold")
        ]),
        Div("p-4 bg-white rounded shadow", [
            Paragraph("Income", text),
            Header3("$421", text + " text-2xl  font-bold")
        ]),
        Div("p-4 bg-white rounded shadow", [
            Paragraph("Expenses", text),
            Header3("$164", text + " text-2xl  font-bold")
        ]),
        Div("p-4 bg-white rounded shadow", [
            Paragraph("Savings", text),
            Header3("$257", text + " text-2xl  font-bold")
        ])
    ]),
    Div("bg-white p-4 rounded shadow mb-8", [
        Header3("Finances", text),
        Builder("canvas ").with_attribute("id", "panel").build()
    ]),
    Div("bg-white p-4 rounded shadow", [
        Header3("Transaction History", text + " mb-4"),
        OL([
            ListItem("flex justify-between items-center mb-2", [
                Div("flex items-center", [
                    Image("./public/imgs/food.png", "", "", "", "w-8 h-8 bg-gray-300 rounded-full mr-4"),
                    Div("", [
                        Paragraph("Aaron Evans",text),
                        Paragraph("Food", "text-gray-600 text-sm")
                    ])
                ]),
                Div("text-right", [
                    Paragraph("$45",text),
                    Paragraph("March 29, 2022", "text-gray-600 text-sm")
                ])
            ]),
            ListItem("flex justify-between items-center mb-2", [
                Div("flex items-center", [
                    Image("./public/imgs/Shopping.png", "", "", "", "w-8 h-8 bg-gray-300 rounded-full mr-4"),
                    Div("", [
                        Paragraph("Clement Stewart",text),
                        Paragraph("Shopping", "text-gray-600 text-sm")
                    ])
                ]),
                Div("text-right", [
                    Paragraph("-$241",text),
                    Paragraph("March 27, 2022", "text-gray-600 text-sm")
                ])
            ]),
            ListItem("flex justify-between items-center", [
                Div("flex items-center", [
                    Image("./public/imgs/other.png", "", "", "", "w-8 h-8 bg-gray-300 rounded-full mr-4"),
                    Div("", [
                        Paragraph("Jessica Johane",text),
                        Paragraph("Others", "text-gray-600 text-sm")
                    ])
                ]),
                Div("text-right", [
                    Paragraph("$100",text),
                    Paragraph("March 25, 2022", "text-gray-600 text-sm")
                ])
            ])
        ], {})
    ])
])

def Transaction(image, span):
    return Div("flex flex-row hover:text-light-green", [
        image, span
    ])
# Right Sidebar
right_sidebar = Div("w-1/4 p-6 bg-gray-100", [
    Div("bg-white p-4 rounded shadow mb-8", [
        Header3("My Card", text + " mb-4"),
        Image("./public/imgs/bank.png", "", "", "", "w-64 h-32 bg-gray-300 rounded mr-2"),
        Button(btn_one_class, "New Card")
    ]),
    Div("bg-white p-4 rounded shadow mb-8", [
        Header3("Reports", text + " mb-4"),
        Div("flex flex-col m-2 gap-2", [
            Transaction(
                Image("./public/imgs/transfer.png", "", "", "", "w-8 h-8 bg-gray-300 rounded-full mr-2"),
                A(Span("text-sm", "Transfers"), {"href": "#"})
            ),
            Transaction(
                Image("./public/imgs/saving.png", "", "", "", "w-8 h-8 bg-gray-300 rounded-full mr-2"),
                A(Span("text-sm", "Savings"), {"href": "#"})
            ),
            Transaction(
                Image("./public/imgs/earning.png", "", "", "", "w-8 h-8 bg-gray-300 rounded-full mr-2"),
                A(Span("text-sm", "Investments"), {"href": "#"})
            ),
        ]),
    ]),
    Div("bg-white p-4 rounded shadow", [
        Header3("My Goals", text + " mb-4"),
        OL([
            ListItem("mb-2", [
              Card([
                  Div("flex justify-between items-center", [
                      Span("", "Saving"),
                      Span(text, "35%")
                  ]),
                  Div("h-2 bg-gray-300 rounded mt-2", [
                      Div("h-2 bg-blue-500 rounded", [])
                  ])
              ], {}, "")
            ]),
            ListItem("mb-2", [
              Card([
                Div("flex justify-between items-center", [
                    Span("", "Investing"),
                    Span(text, "50%")
                ]),
                Div("h-2 bg-gray-300 rounded mt-2", [
                    Div("h-2 bg-blue-500 rounded", [])
                ])
              ], {}, "")
            ]),
        ], {}),
        Button(btn_one_class, "New Goal")
    ])
])

# Final Layout
fintech_layout = Div("flex", [sidebar, main_content, right_sidebar])