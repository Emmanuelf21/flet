import flet as ft

class Todo(ft.Column):
    # application's root control is a Column containing all other controls
    def __init__(self):
        super().__init__()
        self.nova_tarefa = ft.TextField(hint_text="Digite uma nova tarefa...", expand=True)
        self.tarefas = ft.Column()
        self.width = 600
        self.controls = [
            ft.Row(
                controls=[
                    self.nova_tarefa,
                    ft.FloatingActionButton(
                        icon=ft.Icons.ADD, on_click=self.add_click
                    ),
                ],
            ),
            self.tarefas,
        ]

    def add_click(self, e):
        tarefa = Tarefa(self.nova_tarefa.value, self.tarefa_deletar)
        self.tarefas.controls.append(tarefa)
        self.nova_tarefa.value = ""
        self.update()
    
    def tarefa_deletar(self, tarefa):
        self.tarefas.controls.remove(tarefa)
        self.update()

class Tarefa(ft.Column):
    def __init__(self, tarefa_nome, tarefa_deletar):
        super().__init__()
        self.tarefa_nome = tarefa_nome
        self.tarefa_deletar = tarefa_deletar
        self.display_tarefa = ft.Checkbox(value=False, label=self.tarefa_nome)
        self.edit_nome = ft.TextField(expand=1)
        
        self.display_visualizar = ft.Row(
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[
                self.display_tarefa,
                ft.Row(
                    spacing=0,
                    controls=[
                        ft.IconButton(
                            icon=ft.Icons.CREATE_OUTLINED,
                            tooltip="Edit To-Do",
                            on_click=self.edit_click,
                        ),
                        ft.IconButton(
                            ft.Icons.DELETE_OUTLINE,
                            tooltip="Delete To-Do",
                            on_click=self.delete_click,
                        ),
                    ],
                ),
            ],
        )
        self.edit_visualizar = ft.Row(
            visible=False,
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[
                self.edit_nome,
                ft.IconButton(
                    icon=ft.Icons.DONE_OUTLINE_OUTLINED,
                    icon_color=ft.Colors.GREEN,
                    tooltip="Update To-Do",
                    on_click=self.save_click,
                ),
            ],
        )
        self.controls = [self.display_visualizar, self.edit_visualizar]
        
    def edit_click(self, e):
        self.edit_nome.value = self.display_tarefa.label
        self.display_visualizar.visible = False
        self.edit_visualizar.visible = True
        self.update()

    def save_click(self, e):
        self.display_tarefa.label = self.edit_nome.value
        self.display_visualizar.visible = True
        self.edit_visualizar.visible = False
        self.update()

    def delete_click(self, e):
        self.tarefa_deletar(self)

def main(page: ft.Page):
    page.title = "To-Do App"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.update()

    todo = Todo()

    page.add(todo)

ft.app(main)