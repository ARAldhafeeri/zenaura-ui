from zenaura.ui.common import A, Image, OL, LI, Header1, Header2, Paragraph, Div, Span, NavItemText, NavItemIcon
from zenaura.client.tags.builder import Builder
from zenaura.ui.input import Input
from zenaura.ui.button import Button
from zenaura.ui.card import Card
from zenaura.ui.badge import Badge

from zenaura.ui.select import Select, Option
from public.styles import with_theme_colors, with_theme_colors_text_no_hover, btn_one_class

left_side_bar = with_theme_colors("text-light-white")
text = with_theme_colors_text_no_hover("")

def Header2(text, class_name):
    return Builder('h3').with_text(text).with_attribute('class', class_name).build()

def ListItem(class_name, children):
    return Builder("li").with_children(*children).with_class(class_name).build()

# Sidebar
sidebar = Div("flex flex-col w-2/5 ", [
    Header2("Filter By", text + " mb-4 text-2xl"),
    Div("h-fit py-10	 bg-light-gray2 dark:bg-dark-gray2 rounded  text-white p-4", [
    OL([
      LI(
          Input("Search", {"placeholder": "search products"},        default_label_class= "block mb-2 text-light-white dark:text-dark-page1"), {"class": "mb-2"}
      ),
      LI(
          Select(
              "Origin", {}, [
              Option("All Origin", {},),
              Option("Yamen", {}),
              Option("Saudi", {}),
              Option("Brazil", {}),
          ],
          default_label_class= "block mb-2 text-light-white dark:text-dark-page1"
          ),
          {"class": "mb-2"},
      ),
      LI(
          Select("Process", {}, [
              Option("Washed", {},),
              Option("Natural", {}),
              Option("Pulped natural", {}),
              Option("Semi-Wshed", {}),
          ],        default_label_class= "block mb-2 text-light-white dark:text-dark-page1"),
          {"class": "mb-2"}
      ),
      LI(
        Select("Quality", {}, [
            Option("High", {},),
            Option("Mid", {}),
            Option("Okay", {}),
        ], default_label_class= "block mb-2 text-light-white dark:text-dark-page1"),
        {"class": "mb-2"}
      ),
      LI(
        Select("Prices", {}, [
            Option("100$ per 1KG", {},),
            Option("200$ per 1KG", {}),
            Option("500$ per 1 KG", {}),
        ],        default_label_class= "block mb-2 text-light-white dark:text-dark-page1"),
        {"class": "mb-2"}
      ),
    ], {})
])
])

def CoffeeCard(image_src, flag_src, title, tags, price, shipping, stock):
    return Card([
          Div("grid grid-cols-[40%,60%]", [
            Image(image_src, "", "", "", "w-40 h-40 bg-gray-200 rounded"),
            Div("grid grid-rows-5", [
                Div("flex justify-between", [
                    title, 
                    Image(flag_src, "", "", "", "w-8 h-8 bg-gray-200 rounded-full"),
                ]),
                Div("flex space-between h-fit", tags),
                Div("flex justify-between", [
                    shipping,
                    stock
                ]),
                price, 
                Button(btn_one_class, "View Offer")
            ])
          ])
        ], {}, "shadow w-full me-2 px-2.5 py-2.5")


# Main Content
main_content = Div("w-3/5 p-6", [
    Header2("Featured Products", text + " mb-4 text-2xl"),
    Div("grid grid-cols-1 gap-6 h-3/4 overflow-y-auto", [
      CoffeeCard(
        "./public/imgs/Ethiopia Yirgacheffe.png",
        "./public/imgs/ethopia.png", 
        Header2("Ethiopia Yirgacheffe", text + " text-3xl bold"), 
        [
            Badge("Citrusy", {}), 
            Badge("Balanced", {}),
            Badge("Nutty", {}), 

        ], 
        Span(text, "$20 per 1KG"),
        Span(text, "Shipping: 3-7 days"),
        Span(text, "Stock: 500 bag "),
      ),
      CoffeeCard(
        "./public/imgs/Colombia Supremo.png",
        "./public/imgs/colm.png", 
        Header2("Colombia Supremo", text + " text-3xl bold"), 
        [
            Badge("Arabica", {}), 
            Badge("washed", {}), 
            Badge("Floral", {}), 
        ], 
        Span(text, "$22 per 1KG"),
        Span(text, "Shipping: 5-7 days"),
        Span(text, "Stock: 230 bag "),
      ),
      CoffeeCard(
        "./public/imgs/Guatemala Antigua.png",
        "./public/imgs/Guatemala.png", 
        Header2("Guatemala Antigua", text + " text-3xl bold"), 
        [
            Badge("Balanced", {}), 
            Badge("Nutty", {}), 
        ], 
        Span(text, "$20 per 1KG"),
        Span(text, "Shipping: 1-2 days"),
        Span(text, "Stock: 2321 bag "),
      ),
      CoffeeCard(
        "./public/imgs/Kenya AA.png",
        "./public/imgs/Kenya.png", 
        Header2("Kenya AA", text + " text-3xl bold"), 
        [
            Badge("Chocolatey", {}), 
            Badge("Fruity", {}), 
            Badge("Complex", {}), 
        ], 
        Span(text, "$60 per 1KG"),
        Span(text, "Shipping: 1-2 days"),
        Span(text, "Stock: 5231 bag "),
      ),
      CoffeeCard(
        "./public/imgs/Costa Rica Tarrazu.png",
        "./public/imgs/Costa Rica.png", 
        Header2("Costa Rica Tarrazu", text + " text-3xl bold"), 
        [
            Badge("Citrusy", {}), 
            Badge("Complex", {}), 
        ], 
        Span(text, "$35 per 1KG"),
        Span(text, "Shipping: 3-9 days"),
        Span(text, "Stock: 230 bag "),
      ),
      CoffeeCard(
        "./public/imgs/Panama Geisha.png",
        "./public/imgs/Panama.png", 
        Header2("Panama Geisha", text + " text-3xl bold"), 
        [
            Badge("Arabica", {}), 
            Badge("washed", {}),
            Badge("Complex", {}), 
        ], 
        Span(text, "$55 per 1KG"),
        Span(text, "Shipping: 7-14 days"),
        Span(text, "Stock: 330 bag "),
      )
    ])
])

# Final Layout
ecommerce_layout = Div("flex h-screen", [sidebar, main_content])
