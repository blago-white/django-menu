# django-menu
<p>В панели администратора можно создать как главное меню, так и подменю внутри основного.<br><b>Главное меню</b> создается в таблице <code>Menues</code>, содержит в себе несколько полей:</p><ul><li><b>Title</b> - Название меню</li><li><b>Slug</b> - <b>Уникальный идентификатор</b>, по нему можно будет увидеть содержимое вашего меню, а так же на него ссылается поле <code>parent_menu</code> в таблице <code>Menu Items</code></li></ul>В таблице <code>Menu Items</code> можно создать субменю или простой элемент основного меню*<br><sup>*любой элемент вышеупомянутой таблицы фактически является субменю, ведь имеет уникальный идентификатор (<b>slug</b>)</sup><br><code>Menu Items</code> содержит 4 поля:<ul><li><b>Title</b> - Название субменю</li><li><b>Slug</b> - Вышеупомянутый идентификатор, на который могут ссылаться другие подменю, такие ссылающиеся элементы будут считаться элементами ссылаемого субменю</li><li><b>Parent menu</b> - Ссылка на <b>slug</b> родительского <i><b>Главного</b></i> меню</li><li><b>Parent sub-menu</b> - Соответственно ссылка на <b>slug</b> родительского подменю</li></ul>В элементе таблицы <code>Menu Items</code> можно указать только 1 родительское меню, то есть заполнен должен быть только один родительский <b>slug</b> (либо на основное меню либо на подменю)<br><b>Доступ ко всем сущностям древовидного меню осуществляется по url: </b><code>http://127.0.0.1:8000/<b><ins>SLUG</ins></b></code><br><br><ins>Модуль под названием <b><code>highlighted.py</code></b> и все связанное с ним  отвечает только за выделение развернутых элементов красным цветом.</ins><br><br>Все скриншоты приложения есть в папке <code>Screenshots</code>
