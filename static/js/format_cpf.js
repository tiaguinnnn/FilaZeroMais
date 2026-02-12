// static/js/format_cpf.js
document.addEventListener('DOMContentLoaded', function () {
  // ===== CPF =====
  const cpfInput = document.getElementById('cpf');
  if (cpfInput) {
    cpfInput.setAttribute('inputmode', 'numeric');
    // maxlength 14 por causa da máscara 000.000.000-00
    cpfInput.setAttribute('maxlength', '14');

    cpfInput.addEventListener('input', (e) => {
      // mantém apenas dígitos e limita a 11
      let digits = e.target.value.replace(/\D/g, '').slice(0, 11);

      // aplica a máscara 000.000.000-00
      let masked = digits;
      if (digits.length > 3) masked = digits.replace(/^(\d{3})(\d+)/, '$1.$2');
      if (digits.length > 6) masked = masked.replace(/^(\d{3})\.(\d{3})(\d+)/, '$1.$2.$3');
      if (digits.length > 9) masked = masked.replace(/^(\d{3})\.(\d{3})\.(\d{3})(\d{1,2})$/, '$1.$2.$3-$4');

      e.target.value = masked;
    });

    // Evita colar mais de 11 dígitos
    cpfInput.addEventListener('paste', (e) => {
      e.preventDefault();
      const text = (e.clipboardData || window.clipboardData).getData('text');
      let digits = text.replace(/\D/g, '').slice(0, 11);
      // força a mesma lógica de máscara
      let masked = digits;
      if (digits.length > 3) masked = digits.replace(/^(\d{3})(\d+)/, '$1.$2');
      if (digits.length > 6) masked = masked.replace(/^(\d{3})\.(\d{3})(\d+)/, '$1.$2.$3');
      if (digits.length > 9) masked = masked.replace(/^(\d{3})\.(\d{3})\.(\d{3})(\d{1,2})$/, '$1.$2.$3-$4');
      cpfInput.value = masked;
    });
  }

  // ===== Telefone =====
  const telInput = document.getElementById('telefone');
  if (telInput) {
    telInput.setAttribute('inputmode', 'tel');
    // 15 com máscara de celular (11 dígitos) => (00) 00000-0000
    telInput.setAttribute('maxlength', '15');

    telInput.addEventListener('input', (e) => {
      let digits = e.target.value.replace(/\D/g, '');

      // limita a no máximo 11 dígitos (celular). Se vier 10, vira fixo.
      if (digits.length > 11) digits = digits.slice(0, 11);

      if (digits.length <= 10) {
        // Fixo: (00) 0000-0000
        digits = digits
          .replace(/^(\d{0,2})(\d{0,4})(\d{0,4}).*/, function (_, d1, d2, d3) {
            if (d3) return `(${d1}) ${d2}-${d3}`;
            if (d2) return `(${d1}) ${d2}`;
            if (d1) return `(${d1}`;
            return '';
          });
      } else {
        // Celular: (00) 00000-0000
        digits = digits
          .replace(/^(\d{0,2})(\d{0,5})(\d{0,4}).*/, function (_, d1, d2, d3) {
            if (d3) return `(${d1}) ${d2}-${d3}`;
            if (d2) return `(${d1}) ${d2}`;
            if (d1) return `(${d1}`;
            return '';
          });
      }

      e.target.value = digits;
    });

    telInput.addEventListener('paste', (e) => {
      e.preventDefault();
      const text = (e.clipboardData || window.clipboardData).getData('text');
      let digits = text.replace(/\D/g, '').slice(0, 11);
      // força reprocessamento pelo 'input'
      telInput.value = digits;
      telInput.dispatchEvent(new Event('input'));
    });
  }
});