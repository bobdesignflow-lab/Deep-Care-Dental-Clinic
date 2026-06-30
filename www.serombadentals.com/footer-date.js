(function() {
  function setFooterDate() {
    var tz = 'Africa/Nairobi';
    var now = new Date();
    var month = new Intl.DateTimeFormat('en-GB', { timeZone: tz, month: '2-digit' }).format(now);
    var year = new Intl.DateTimeFormat('en-GB', { timeZone: tz, year: 'numeric' }).format(now);
    var value = month + ' - ' + year;

    var nodes = document.querySelectorAll('[data-footer-date]');
    for (var i = 0; i < nodes.length; i++) {
      nodes[i].textContent = value;
    }
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', setFooterDate);
  } else {
    setFooterDate();
  }
})();
