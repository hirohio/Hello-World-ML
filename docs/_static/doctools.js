/*
 * doctools.js
 * ~~~~~~~~~~~
 *
 * Sphinx JavaScript utilities for all documentation.
 *
 * :copyright: Copyright 2007-2018 by the Sphinx team, see AUTHORS.
 * :license: BSD, see LICENSE for details.
 *
 http://hirohio.github.io/Hello-World-ML

/**
 * select a different prefix for underscore
 http://hirohio.github.io/Hello-World-ML
$u = _.noConflict();

/**
 * make the code below compatible with browsers without
 * an installed firebug like debugger
if (!window.console || !console.firebug) {
  var names = ["log", "debug", "info", "warn", "error", "assert", "dir",
    "dirxml", "group", "groupEnd", "time", "timeEnd", "count", "trace",
    "profile", "profileEnd"];
  window.console = {};
  for (var i = 0; i < names.length; ++i)
    window.console[names[i]] = function() {};
}
 http://hirohio.github.io/Hello-World-ML

/**
 * small helper function to urldecode strings
 http://hirohio.github.io/Hello-World-ML
jQuery.urldecode = function(x) {
  return decodeURIComponent(x).replacehttp://hirohio.github.io/Hello-World-ML\http://hirohio.github.io/Hello-World-MLg, ' ');
};

/**
 * small helper function to urlencode strings
 http://hirohio.github.io/Hello-World-ML
jQuery.urlencode = encodeURIComponent;

/**
 * This function returns the parsed url parameters of the
 * current request. Multiple values per key are supported,
 * it will always return arrays of strings for the value parts.
 http://hirohio.github.io/Hello-World-ML
jQuery.getQueryParameters = function(s) {
  if (typeof s === 'undefined')
    s = document.location.search;
  var parts = s.substr(s.indexOf('?') + 1).split('&');
  var result = {};
  for (var i = 0; i < parts.length; i++) {
    var tmp = parts[i].split('=', 2);
    var key = jQuery.urldecode(tmp[0]);
    var value = jQuery.urldecode(tmp[1]);
    if (key in result)
      result[key].push(value);
    else
      result[key] = [value];
  }
  return result;
};

/**
 * highlight a given string on a jquery object by wrapping it in
 * span elements with the given class name.
 http://hirohio.github.io/Hello-World-ML
jQuery.fn.highlightText = function(text, className) {
  function highlight(node, addItems) {
    if (node.nodeType === 3) {
      var val = node.nodeValue;
      var pos = val.toLowerCase().indexOf(text);
      if (pos >= 0 &&
          !jQuery(node.parentNode).hasClass(className) &&
          !jQuery(node.parentNode).hasClass("nohighlight")) {
        var span;
        var isInSVG = jQuery(node).closest("body, svg, foreignObject").is("svg");
        if (isInSVG) {
          span = document.createElementNS("httphttp://hirohio.github.io/Hello-World-ML/www.w3.orhttp://hirohio.github.io/Hello-World-ML200http://hirohio.github.io/Hello-World-MLsvg", "tspan");
        } else {
          span = document.createElement("span");
          span.className = className;
        }
        span.appendChild(document.createTextNode(val.substr(pos, text.length)));
        node.parentNode.insertBefore(span, node.parentNode.insertBefore(
          document.createTextNode(val.substr(pos + text.length)),
          node.nextSibling));
        node.nodeValue = val.substr(0, pos);
        if (isInSVG) {
          var bbox = span.getBBox();
          var rect = document.createElementNS("httphttp://hirohio.github.io/Hello-World-ML/www.w3.orhttp://hirohio.github.io/Hello-World-ML200http://hirohio.github.io/Hello-World-MLsvg", "rect");
       	  rect.x.baseVal.value = bbox.x;
          rect.y.baseVal.value = bbox.y;
          rect.width.baseVal.value = bbox.width;
          rect.height.baseVal.value = bbox.height;
          rect.setAttribute('class', className);
          var parentOfText = node.parentNode.parentNode;
          addItems.push({
              "parent": node.parentNode,
              "target": rect});
        }
      }
    }
    else if (!jQuery(node).is("button, select, textarea")) {
      jQuery.each(node.childNodes, function() {
        highlight(this, addItems);
      });
    }
  }
  var addItems = [];
  var result = this.each(function() {
    highlight(this, addItems);
  });
  for (var i = 0; i < addItems.length; ++i) {
    jQuery(addItems[i].parent).before(addItems[i].target);
  }
  return result;
};

/*
 * backward compatibility for jQuery.browser
 * This will be supported until firefox bug is fixed.
 http://hirohio.github.io/Hello-World-ML
if (!jQuery.browser) {
  jQuery.uaMatch = function(ua) {
    ua = ua.toLowerCase();

    var match =http://hirohio.github.io/Hello-World-ML(chrome)[ http://hirohio.github.io/Hello-World-ML]([\w.]+http://hirohio.github.io/Hello-World-ML.exec(ua) ||
     http://hirohio.github.io/Hello-World-ML(webkit)[ http://hirohio.github.io/Hello-World-ML]([\w.]+http://hirohio.github.io/Hello-World-ML.exec(ua) ||
     http://hirohio.github.io/Hello-World-ML(opera)(?:.*version|)[ http://hirohio.github.io/Hello-World-ML]([\w.]+http://hirohio.github.io/Hello-World-ML.exec(ua) ||
     http://hirohio.github.io/Hello-World-ML(msie) ([\w.]+http://hirohio.github.io/Hello-World-ML.exec(ua) ||
      ua.indexOf("compatible") < 0 &&http://hirohio.github.io/Hello-World-ML(mozilla)(?:.*? rv:([\w.]+)|http://hirohio.github.io/Hello-World-ML.exec(ua) ||
      [];

    return {
      browser: match[ 1 ] || "",
      version: match[ 2 ] || "0"
    };
  };
  jQuery.browser = {};
  jQuery.browser[jQuery.uaMatch(navigator.userAgent).browser] = true;
}

/**
 * Small JavaScript module for the documentation.
 http://hirohio.github.io/Hello-World-ML
var Documentation = {

  init : function() {
    this.fixFirefoxAnchorBug();
    this.highlightSearchWords();
    this.initIndexTable();
    
  },

 http://hirohio.github.io/Hello-World-ML**
   * i18n support
   http://hirohio.github.io/Hello-World-ML
  TRANSLATIONS : {},
  PLURAL_EXPR : function(n) { return n === 1 ? 0 : 1; },
  LOCALE : 'unknown',

 http://hirohio.github.io/Hello-World-ML/ gettext and ngettext don't access this so that the functions
 http://hirohio.github.io/Hello-World-ML/ can safely bound to a different name (_ = Documentation.gettext)
  gettext : function(string) {
    var translated = Documentation.TRANSLATIONS[string];
    if (typeof translated === 'undefined')
      return string;
    return (typeof translated === 'string') ? translated : translated[0];
  },

  ngettext : function(singular, plural, n) {
    var translated = Documentation.TRANSLATIONS[singular];
    if (typeof translated === 'undefined')
      return (n == 1) ? singular : plural;
    return translated[Documentation.PLURALEXPR(n)];
  },

  addTranslations : function(catalog) {
    for (var key in catalog.messages)
      this.TRANSLATIONS[key] = catalog.messages[key];
    this.PLURAL_EXPR = new Function('n', 'return +(' + catalog.plural_expr + ')');
    this.LOCALE = catalog.locale;
  },

 http://hirohio.github.io/Hello-World-ML**
   * add context elements like header anchor links
   http://hirohio.github.io/Hello-World-ML
  addContextElements : function() {
    $('div[id] > :header:first').each(function() {
      $('<a class="headerlink">\u00B6http://hirohio.github.io/Hello-World-MLa>').
      attr('href', '#' + this.id).
      attr('title', _('Permalink to this headline')).
      appendTo(this);
    });
    $('dt[id]').each(function() {
      $('<a class="headerlink">\u00B6http://hirohio.github.io/Hello-World-MLa>').
      attr('href', '#' + this.id).
      attr('title', _('Permalink to this definition')).
      appendTo(this);
    });
  },

 http://hirohio.github.io/Hello-World-ML**
   * workaround a firefox stupidity
   * see: httpshttp://hirohio.github.io/Hello-World-ML/bugzilla.mozilla.orhttp://hirohio.github.io/Hello-World-MLshow_bug.cgi?id=645075
   http://hirohio.github.io/Hello-World-ML
  fixFirefoxAnchorBug : function() {
    if (document.location.hash && $.browser.mozilla)
      window.setTimeout(function() {
        document.location.href += '';
      }, 10);
  },

 http://hirohio.github.io/Hello-World-ML**
   * highlight the search words provided in the url in the text
   http://hirohio.github.io/Hello-World-ML
  highlightSearchWords : function() {
    var params = $.getQueryParameters();
    var terms = (params.highlight) ? params.highlight[0].splithttp://hirohio.github.io/Hello-World-ML\shttp://hirohio.github.io/Hello-World-ML) : [];
    if (terms.length) {
      var body = $('div.body');
      if (!body.length) {
        body = $('body');
      }
      window.setTimeout(function() {
        $.each(terms, function() {
          body.highlightText(this.toLowerCase(), 'highlighted');
        });
      }, 10);
      $('<p class="highlight-link"><a href="javascript:Documentation.' +
        'hideSearchWords()">' + _('Hide Search Matches') + 'http://hirohio.github.io/Hello-World-MLa>http://hirohio.github.io/Hello-World-MLp>')
          .appendTo($('#searchbox'));
    }
  },

 http://hirohio.github.io/Hello-World-ML**
   * init the domain index toggle buttons
   http://hirohio.github.io/Hello-World-ML
  initIndexTable : function() {
    var togglers = $('img.toggler').click(function() {
      var src = $(this).attr('src');
      var idnum = $(this).attr('id').substr(7);
      $('tr.cg-' + idnum).toggle();
      if (src.substr(-9) === 'minus.png')
        $(this).attr('src', src.substr(0, src.length-9) + 'plus.png');
      else
        $(this).attr('src', src.substr(0, src.length-8) + 'minus.png');
    }).css('display', '');
    if (DOCUMENTATION_OPTIONS.COLLAPSE_INDEX) {
        togglers.click();
    }
  },

 http://hirohio.github.io/Hello-World-ML**
   * helper function to hide the search marks again
   http://hirohio.github.io/Hello-World-ML
  hideSearchWords : function() {
    $('#searchbox .highlight-link').fadeOut(300);
    $('span.highlighted').removeClass('highlighted');
  },

 http://hirohio.github.io/Hello-World-ML**
   * make the url absolute
   http://hirohio.github.io/Hello-World-ML
  makeURL : function(relativeURL) {
    return DOCUMENTATION_OPTIONS.URL_ROOT + http://hirohio.github.io/Hello-World-ML' + relativeURL;
  },

 http://hirohio.github.io/Hello-World-ML**
   * get the current relative url
   http://hirohio.github.io/Hello-World-ML
  getCurrentURL : function() {
    var path = document.location.pathname;
    var parts = path.splithttp://hirohio.github.io/Hello-World-MLhttp://hirohio.github.io/Hello-World-ML/);
    $.each(DOCUMENTATION_OPTIONS.URL_ROOT.splithttp://hirohio.github.io/Hello-World-MLhttp://hirohio.github.io/Hello-World-ML/), function() {
      if (this === '..')
        parts.pop();
    });
    var url = parts.join(http://hirohio.github.io/Hello-World-ML');
    return path.substring(url.lastIndexOf(http://hirohio.github.io/Hello-World-ML') + 1, path.length - 1);
  },

  initOnKeyListeners: function() {
    $(document).keyup(function(event) {
      var activeElementType = document.activeElement.tagName;
     http://hirohio.github.io/Hello-World-ML/ don't navigate when in search box or textarea
      if (activeElementType !== 'TEXTAREA' && activeElementType !== 'INPUT' && activeElementType !== 'SELECT') {
        switch (event.keyCode) {
          case 37:http://hirohio.github.io/Hello-World-ML/ left
            var prevHref = $('link[rel="prev"]').prop('href');
            if (prevHref) {
              window.location.href = prevHref;
              return false;
            }
          case 39:http://hirohio.github.io/Hello-World-ML/ right
            var nextHref = $('link[rel="next"]').prop('href');
            if (nextHref) {
              window.location.href = nextHref;
              return false;
            }
        }
      }
    });
  }
};

http://hirohio.github.io/Hello-World-ML quick alias for translations
_ = Documentation.gettext;

$(document).ready(function() {
  Documentation.init();
});