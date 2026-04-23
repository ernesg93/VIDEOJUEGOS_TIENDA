document.addEventListener('DOMContentLoaded', function() {
    const btn = document.getElementById('toggle-theme');
    const html = document.documentElement;

    //recuperar el tema guardado en localStorage
    const savedTheme = localStorage.getItem('theme');
    if (savedTheme) {
        html.setAttribute('data-bs-theme', savedTheme);
    }

    if (btn) {
        btn.addEventListener('click', function() {
            const current = html.getAttribute('data-bs-theme');
            const next = current === 'dark' ? 'light' : 'dark';
            html.setAttribute('data-bs-theme', next);

            //guardar el tema seleccionado en localStorage
            localStorage.setItem('theme', next);
        });
    }

    document.querySelectorAll('.password-toggle-button').forEach(function(button) {
        button.addEventListener('click', function() {
            const input = document.getElementById(button.dataset.target);
            const icon = button.querySelector('i');

            if (!input || !icon) {
                return;
            }

            const isPassword = input.type === 'password';
            input.type = isPassword ? 'text' : 'password';
            icon.classList.toggle('fa-eye', !isPassword);
            icon.classList.toggle('fa-eye-slash', isPassword);
        });
    });
});
