{% extends 'base.html' %}

{% block title %}
Новости
{% endblock title %}

{% block content %}

{% if page_num %}
<div class="card my-2">
  <div class="card-body">
    <p class="card-text">Текущая страница: {{ page_num }}</p>
  </div>
</div>
{% endif %}

<div class="row">
  <div class="col-lg-8">

    {% for item in object_list %}
    <div class="card my-2">
      <div class="card-body">
        <h5 class="card-title">{{ item.title }}</h5>
        <h6 class="card-subtitle mb-2 text-muted">
          {{ item.created|date:"Y-m-d h-i-s" }}
        </h6>
        <p class="card-text">{{ item.preambule }}</p>
        <div class="row">
          <div class="col">
            <a href="{% url 'mainapp:news_detail' pk=item.pk %}"
              class="card-link">Подробнее</a>
          </div>
          {% if perms.mainapp.change_news %}
          <div class="col-1 text-center">
            <a href="{% url 'mainapp:news_update' pk=item.pk %}">
              <i class="far fa-edit"></i>
            </a>
          </div>
          {% endif %}
          {% if perms.mainapp.delete_news %}
          <div class="col-1 text-center">
            <a href="{% url 'mainapp:news_delete' pk=item.pk %}">
              <i class="far fa-trash-alt"></i>
            </a>
          </div>
          {% endif %}
        </div>
      </div>
    </div>
    {% endfor %}

  </div>

  <div class="col-lg-4">
    <div class="card my-2 sticky-top">
      <div class="card-header">
        Фильтры
      </div>
      <div class="card-body">
        <form action="">
          <div class="input-group mb-3">
            <div class="input-group-prepend">
              <span class="input-group-text" id="basic-addon1">Дата от...</span>
            </div>
            <input type="date" class="form-control" name="dateFrom">
          </div>
          <div class="input-group mb-3">
            <div class="input-group-prepend">
              <span class="input-group-text" id="basic-addon1">Дата до...</span>
            </div>
            <input type="date" class="form-control" name="dateTo">
          </div>

          <button type="submit"
            class="btn btn-primary btn-block">Фильтровать</button>
        </form>
      </div>
    </div>

    {% if perms.mainapp.add_news %}
    <a class="btn btn-primary btn-block" role="button"
      href="{% url 'mainapp:news_create' %}">Добавить новость</a>
    {% endif %}

  </div>

</div>

<div class="row justify-content-center align-items-center mt-3 mb-n3">
  <nav aria-label="Page navigation example">
    <ul class="pagination">
      <li class="page-item"><a class="page-link" href="#">Previous</a></li>
      <li class="page-item"><a class="page-link" href="#">1</a></li>
      <li class="page-item"><a class="page-link" href="#">2</a></li>
      {# <li class="page-item"><a class="page-link" href="#">3</a></li> #}
      <li class="page-item"><a class="page-link" href="#">Next</a></li>
    </ul>
  </nav>
</div>

{% endblock content %}