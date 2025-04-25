# components/athkar_page.py
import flet as ft
import json

def load_athkar(period):
    try:
        with open(f"assets/athkar/{period}.json", encoding="utf-8") as f:
            return json.load(f)
    except Exception as e:
        print("Error loading athkar:", e)
        return []

def athkar_page(page: ft.Page):
    page.title = "Athkar - أذكار"
    page.rtl = True
    page.theme_mode = ft.ThemeMode.DARK
    page.scroll = ft.ScrollMode.AUTO
    page.clean()

    heading = ft.Text("Morning Athkar", size=24, weight=ft.FontWeight.BOLD)
    content_column = ft.Column(scroll=ft.ScrollMode.ALWAYS)

    def update_athkar(e=None, period="morning"):
        content_column.controls.clear()
        athkar_list = load_athkar(period)
        heading.value = "Morning Athkar" if period == "morning" else "Evening Athkar"

        for dhikr in athkar_list:
            content_column.controls.append(
                ft.Card(
                    content=ft.Container(
                        alignment=ft.alignment.top_right,
                        content=ft.Column([
                            ft.Text(
                                dhikr["text"],
                                selectable=True,
                                text_align=ft.TextAlign.RIGHT,
                                rtl=True,
                            ),
                            ft.Text(
                                f"🔁 التكرار: {dhikr['repeat']}",
                                text_align=ft.TextAlign.RIGHT,
                                rtl=True,
                            ),
                            ft.Text(
                                f"📚 المصدر: {dhikr.get('reference', 'غير معروف')}",
                                italic=True,
                                size=12,
                                text_align=ft.TextAlign.RIGHT,
                                rtl=True,
                            )
                        ]),
                        padding=15
                    )
                )
            )
        page.update()

    tabs = ft.Row([
        ft.ElevatedButton("Morning", on_click=lambda e: update_athkar(period="morning")),
        ft.ElevatedButton("Evening", on_click=lambda e: update_athkar(period="evening")),
        ft.TextButton("⬅ Back", on_click=lambda e: page.go("/")),
    ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN)

    page.add(tabs, heading, content_column)
    update_athkar()  # Load default
