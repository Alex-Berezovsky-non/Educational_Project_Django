// Получаем данные из data-атрибутов при загрузке страницы
document.addEventListener('DOMContentLoaded', function() {
    const dataContainer = document.getElementById('order-form-data');
    const servicesUrl = dataContainer ? dataContainer.dataset.servicesUrl : '/barbershop/masters_services/';
    const csrfToken = dataContainer ? dataContainer.dataset.csrfToken : '';
    
    // Инициализация функций с полученными данными
    initOrderForm(servicesUrl, csrfToken);
});