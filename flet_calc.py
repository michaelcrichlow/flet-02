import flet as ft
from flet import ControlEvent


def main(page: ft.Page) -> None:
    # setup (and setup functions)
    page.title = "Flet Calculator Example"
    page.theme_mode = "dark"
    page.vertical_alignment = ft. MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    # this is mostly for the native app
    # web version seems to be fine without this line
    # page.window_resizable = False

    # variables
    top_number = ft.Ref[ft.Text]()
    # ----
    ac = ft.Ref[ft.ElevatedButton]()
    pos_neg = ft.Ref[ft.ElevatedButton]()
    modulus = ft.Ref[ft.ElevatedButton]()
    divide = ft.Ref[ft.ElevatedButton]()
    # ----
    seven = ft.Ref[ft.ElevatedButton]()
    eight = ft.Ref[ft.ElevatedButton]()
    nine = ft.Ref[ft.ElevatedButton]()
    multiply = ft.Ref[ft.ElevatedButton]()
    # ----
    four = ft.Ref[ft.ElevatedButton]()
    five = ft.Ref[ft.ElevatedButton]()
    six = ft.Ref[ft.ElevatedButton]()
    minus = ft.Ref[ft.ElevatedButton]()
    # ----
    one = ft.Ref[ft.ElevatedButton]()
    two = ft.Ref[ft.ElevatedButton]()
    three = ft.Ref[ft.ElevatedButton]()
    addition = ft.Ref[ft.ElevatedButton]()
    # ----
    zero = ft.Ref[ft.ElevatedButton]()
    point = ft.Ref[ft.ElevatedButton]()
    equals = ft.Ref[ft.ElevatedButton]()

    # functions
    def reset_value_to_zero(e):
        top_number.current.value = "0"
        top_number.current.color = "#F5F5F5"    # white
        page.update()

    def make_positive_or_negative(e):
        if top_number.current.color == "#F5F5F5":
            if len(top_number.current.value) < 6:
                if top_number.current.value[0] != "-":
                    top_number.current.value = "-" + top_number.current.value
                elif top_number.current.value[0] == "-":
                    top_number.current.value = top_number.current.value[1:]
        page.update()

    def place_modulus(e):
        if top_number.current.color == "#F5F5F5":
            if len(top_number.current.value) < 6:
                if top_number.current.value[-1] != "%":
                    top_number.current.value = top_number.current.value + "%"
                elif top_number.current.value[-1] == "%":
                    top_number.current.value = top_number.current.value[:-1]
        page.update()

    def place_division_symbol(e):
        if top_number.current.color == "#F5F5F5":
            if len(top_number.current.value) < 6:
                if top_number.current.value[-1] == "×" or top_number.current.value[-1] == "+" or top_number.current.value[-1] == "-":
                    top_number.current.value = top_number.current.value[:-1] + "÷"
                elif top_number.current.value[-1] != "÷":
                    top_number.current.value = top_number.current.value + "÷"
                elif top_number.current.value[-1] == "÷":
                    top_number.current.value = top_number.current.value[:-1]
        page.update()

    def place_seven(e):
        if top_number.current.color == "#F5F5F5":
            if len(top_number.current.value) < 6:
                if top_number.current.value == "0" or top_number.current.value == "-0":
                    top_number.current.value = "7"
                else:
                    top_number.current.value = top_number.current.value + "7"
        page.update()

    def place_eight(e):
        if top_number.current.color == "#F5F5F5":
            if len(top_number.current.value) < 6:
                if top_number.current.value == "0" or top_number.current.value == "-0":
                    top_number.current.value = "8"
                else:
                    top_number.current.value = top_number.current.value + "8"
        page.update()

    def place_nine(e):
        if top_number.current.color == "#F5F5F5":
            if len(top_number.current.value) < 6:
                if top_number.current.value == "0" or top_number.current.value == "-0":
                    top_number.current.value = "9"
                else:
                    top_number.current.value = top_number.current.value + "9"
        page.update()

    def place_multiplication_symbol(e):
        if top_number.current.color == "#F5F5F5":
            if len(top_number.current.value) < 6:
                if top_number.current.value[-1] == "÷" or top_number.current.value[-1] == "+" or top_number.current.value[-1] == "-":
                    top_number.current.value = top_number.current.value[:-1] + "×"
                elif top_number.current.value[-1] != "×":
                    top_number.current.value = top_number.current.value + "×"
                elif top_number.current.value[-1] == "×":
                    top_number.current.value = top_number.current.value[:-1]
        page.update()

    def place_four(e):
        if top_number.current.color == "#F5F5F5":
            if len(top_number.current.value) < 6:
                if top_number.current.value == "0" or top_number.current.value == "-0":
                    top_number.current.value = "4"
                else:
                    top_number.current.value = top_number.current.value + "4"
        page.update()

    def place_five(e):
        if top_number.current.color == "#F5F5F5":
            if len(top_number.current.value) < 6:
                if top_number.current.value == "0" or top_number.current.value == "-0":
                    top_number.current.value = "5"
                else:
                    top_number.current.value = top_number.current.value + "5"
        page.update()

    def place_six(e):
        if top_number.current.color == "#F5F5F5":
            if len(top_number.current.value) < 6:
                if top_number.current.value == "0" or top_number.current.value == "-0":
                    top_number.current.value = "6"
                else:
                    top_number.current.value = top_number.current.value + "6"
        page.update()

    def place_minus(e):
        if top_number.current.color == "#F5F5F5":
            if len(top_number.current.value) < 6:
                if top_number.current.value[-1] == "÷" or top_number.current.value[-1] == "+" or top_number.current.value[-1] == "×":
                    top_number.current.value = top_number.current.value[:-1] + "-"
                elif top_number.current.value[-1] != "-":
                    top_number.current.value = top_number.current.value + "-"
                elif top_number.current.value[-1] == "-":
                    top_number.current.value = top_number.current.value[:-1]
        page.update()

    def place_one(e):
        if top_number.current.color == "#F5F5F5":
            if len(top_number.current.value) < 6:
                if top_number.current.value == "0" or top_number.current.value == "-0":
                    top_number.current.value = "1"
                else:
                    top_number.current.value = top_number.current.value + "1"
        page.update()

    def place_two(e):
        if top_number.current.color == "#F5F5F5":
            if len(top_number.current.value) < 6:
                if top_number.current.value == "0" or top_number.current.value == "-0":
                    top_number.current.value = "2"
                else:
                    top_number.current.value = top_number.current.value + "2"
        page.update()

    def place_three(e):
        if top_number.current.color == "#F5F5F5":
            if len(top_number.current.value) < 6:
                if top_number.current.value == "0" or top_number.current.value == "-0":
                    top_number.current.value = "3"
                else:
                    top_number.current.value = top_number.current.value + "3"
        page.update()

    def place_addition_symbol(e):
        if top_number.current.color == "#F5F5F5":
            if len(top_number.current.value) < 6:
                if top_number.current.value[-1] == "÷" or top_number.current.value[-1] == "-" or top_number.current.value[-1] == "×":
                    top_number.current.value = top_number.current.value[:-1] + "+"
                elif top_number.current.value[-1] != "+":
                    top_number.current.value = top_number.current.value + "+"
                elif top_number.current.value[-1] == "+":
                    top_number.current.value = top_number.current.value[:-1]
        page.update()

    def place_zero(e):
        if top_number.current.color == "#F5F5F5":
            if len(top_number.current.value) < 6:
                if top_number.current.value == "0" or top_number.current.value == "-0":
                    # do nothing
                    pass
                else:
                    top_number.current.value = top_number.current.value + "0"
        page.update()

    def place_point(e):
        if top_number.current.color == "#F5F5F5":
            if len(top_number.current.value) < 6:
                if top_number.current.value[-1] != "." and "." not in top_number.current.value:
                    top_number.current.value = top_number.current.value + "."
                elif top_number.current.value[-1] == ".":
                    top_number.current.value = top_number.current.value[:-1]
        page.update()

    def calculate_result(e):
        if top_number.current.color == "#F5F5F5":
            res = top_number.current.value.replace("×", "*")
            res = res.replace("÷", "/")
            try:
                top_number.current.value = str(eval(res))
                if len(top_number.current.value) > 6:
                    top_number.current.value = top_number.current.value[:6]
            except Exception:
                top_number.current.value = "Error"
                top_number.current.color = "#FF0000"    # red
        page.update()

    # build the page
    page.add(

        ft.Container(width=300, bgcolor="#000000", border_radius=ft.border_radius.all(20), padding=20,
                     content=ft.Column(controls=[
                         ft.Row([
                             ft.Text(ref=top_number, value="0",
                                     color="#F5F5F5", size=70)
                         ], alignment=ft.MainAxisAlignment.END),
                         ft.Row([
                             ft.ElevatedButton(ref=ac, text="C",
                                               bgcolor="#A0A0A0", color="#000000", expand=1, style=ft.ButtonStyle(shape=ft.CircleBorder(), padding=20),
                                               on_click=reset_value_to_zero),
                             ft.ElevatedButton(ref=pos_neg, text="±",
                                               bgcolor="#A0A0A0", color="#000000", expand=1, style=ft.ButtonStyle(shape=ft.CircleBorder(), padding=20),
                                               on_click=make_positive_or_negative),
                             ft.ElevatedButton(ref=modulus, text="%",
                                               bgcolor="#A0A0A0", color="#000000", expand=1, style=ft.ButtonStyle(shape=ft.CircleBorder(), padding=20),
                                               on_click=place_modulus),
                             ft.ElevatedButton(ref=divide, text="÷",
                                               bgcolor="#F69906", color="#F5F5F5", expand=1, style=ft.ButtonStyle(shape=ft.CircleBorder(), padding=20),
                                               on_click=place_division_symbol),
                         ]),
                         ft.Row([
                             ft.ElevatedButton(ref=seven, text="7",
                                               bgcolor="#313131", color="#F5F5F5", expand=1, style=ft.ButtonStyle(shape=ft.CircleBorder(), padding=20),
                                               on_click=place_seven),
                             ft.ElevatedButton(ref=eight, text="8",
                                               bgcolor="#313131", color="#F5F5F5", expand=1, style=ft.ButtonStyle(shape=ft.CircleBorder(), padding=20),
                                               on_click=place_eight),
                             ft.ElevatedButton(ref=nine, text="9",
                                               bgcolor="#313131", color="#F5F5F5", expand=1, style=ft.ButtonStyle(shape=ft.CircleBorder(), padding=20),
                                               on_click=place_nine),
                             ft.ElevatedButton(ref=multiply, text="×",
                                               bgcolor="#F69906", color="#F5F5F5", expand=1, style=ft.ButtonStyle(shape=ft.CircleBorder(), padding=20),
                                               on_click=place_multiplication_symbol),
                         ]),
                         ft.Row([
                             ft.ElevatedButton(ref=four, text="4",
                                               bgcolor="#313131", color="#F5F5F5", expand=1, style=ft.ButtonStyle(shape=ft.CircleBorder(), padding=20),
                                               on_click=place_four),
                             ft.ElevatedButton(ref=five, text="5",
                                               bgcolor="#313131", color="#F5F5F5", expand=1, style=ft.ButtonStyle(shape=ft.CircleBorder(), padding=20),
                                               on_click=place_five),
                             ft.ElevatedButton(ref=six, text="6",
                                               bgcolor="#313131", color="#F5F5F5", expand=1, style=ft.ButtonStyle(shape=ft.CircleBorder(), padding=20),
                                               on_click=place_six),
                             ft.ElevatedButton(ref=minus, text="-",
                                               bgcolor="#F69906", color="#F5F5F5", expand=1, style=ft.ButtonStyle(shape=ft.CircleBorder(), padding=20),
                                               on_click=place_minus),
                         ]),
                         ft.Row([
                             ft.ElevatedButton(ref=one, text="1",
                                               bgcolor="#313131", color="#F5F5F5", expand=1, style=ft.ButtonStyle(shape=ft.CircleBorder(), padding=20),
                                               on_click=place_one),
                             ft.ElevatedButton(ref=two, text="2",
                                               bgcolor="#313131", color="#F5F5F5", expand=1, style=ft.ButtonStyle(shape=ft.CircleBorder(), padding=20),
                                               on_click=place_two),
                             ft.ElevatedButton(ref=three, text="3",
                                               bgcolor="#313131", color="#F5F5F5", expand=1, style=ft.ButtonStyle(shape=ft.CircleBorder(), padding=20),
                                               on_click=place_three),
                             ft.ElevatedButton(ref=addition, text="+",
                                               bgcolor="#F69906", color="#F5F5F5", expand=1, style=ft.ButtonStyle(shape=ft.CircleBorder(), padding=20),
                                               on_click=place_addition_symbol),
                         ]),
                         ft.Row([
                             ft.ElevatedButton(ref=zero, text="0",
                                               bgcolor="#313131", color="#F5F5F5", expand=2,
                                               on_click=place_zero),
                             ft.ElevatedButton(ref=point, text=".",
                                               bgcolor="#313131", color="#F5F5F5", expand=1, style=ft.ButtonStyle(shape=ft.CircleBorder(), padding=20),
                                               on_click=place_point),
                             ft.ElevatedButton(ref=equals, text="=",
                                               bgcolor="#F69906", color="#F5F5F5", expand=1, style=ft.ButtonStyle(shape=ft.CircleBorder(), padding=20),
                                               on_click=calculate_result),
                         ]),
                     ], alignment=ft.MainAxisAlignment.CENTER))
    )


if __name__ == '__main__':
    ft.app(target=main, view=ft.AppView.WEB_BROWSER)
