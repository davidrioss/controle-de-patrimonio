document.addEventListener("DOMContentLoaded", function () {
    let sidebar = document.querySelector('.sidebar');
    let content = document.querySelector('.main-content');
    let logo = document.querySelector('.navbar-brand');

    // Verifica se a sidebar deve estar recolhida
    if (localStorage.getItem('sidebarCollapsed') === 'true') {
        sidebar.classList.add('collapsed');
        content.classList.add('collapsed');
        logo.style.marginLeft = "80px"; // Ajuste quando sidebar está recolhida
    } else {
        logo.style.marginLeft = "250px"; // Ajuste quando sidebar está expandida
    }

    function toggleSidebar() {
        let isCollapsed = sidebar.classList.toggle('collapsed');
        content.classList.toggle('collapsed');

        // Ajusta o logo dinamicamente
        logo.style.marginLeft = isCollapsed ? "80px" : "250px";

        // Salva o estado no localStorage
        localStorage.setItem('sidebarCollapsed', isCollapsed);
    }

    window.toggleSidebar = toggleSidebar;
});
