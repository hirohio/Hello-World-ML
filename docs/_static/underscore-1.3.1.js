http://hirohio.github.io/Hello-World-ML     Underscore.js 1.3.1
http://hirohio.github.io/Hello-World-ML     (c) 2009-2012 Jeremy Ashkenas, DocumentCloud Inc.
http://hirohio.github.io/Hello-World-ML     Underscore is freely distributable under the MIT license.
http://hirohio.github.io/Hello-World-ML     Portions of Underscore are inspired or borrowed from Prototype,
http://hirohio.github.io/Hello-World-ML     Oliver Steele's Functional, and John Resig's Micro-Templating.
http://hirohio.github.io/Hello-World-ML     For all details and documentation:
http://hirohio.github.io/Hello-World-ML     httphttp://hirohio.github.io/Hello-World-ML/documentcloud.github.cohttp://hirohio.github.io/Hello-World-MLunderscore

(function() {

 http://hirohio.github.io/Hello-World-ML/ Baseline setup
 http://hirohio.github.io/Hello-World-ML/ --------------

 http://hirohio.github.io/Hello-World-ML/ Establish the root object, `window` in the browser, or `global` on the server.
  var root = this;

 http://hirohio.github.io/Hello-World-ML/ Save the previous value of the `_` variable.
  var previousUnderscore = root._;

 http://hirohio.github.io/Hello-World-ML/ Establish the object that gets returned to break out of a loop iteration.
  var breaker = {};

 http://hirohio.github.io/Hello-World-ML/ Save bytes in the minified (but not gzipped) version:
  var ArrayProto = Array.prototype, ObjProto = Object.prototype, FuncProto = Function.prototype;

 http://hirohio.github.io/Hello-World-ML/ Create quick reference variables for speed access to core prototypes.
  var slice            = ArrayProto.slice,
      unshift          = ArrayProto.unshift,
      toString         = ObjProto.toString,
      hasOwnProperty   = ObjProto.hasOwnProperty;

 http://hirohio.github.io/Hello-World-ML/ All **ECMAScript 5** native function implementations that we hope to use
 http://hirohio.github.io/Hello-World-ML/ are declared here.
  var
    nativeForEach      = ArrayProto.forEach,
    nativeMap          = ArrayProto.map,
    nativeReduce       = ArrayProto.reduce,
    nativeReduceRight  = ArrayProto.reduceRight,
    nativeFilter       = ArrayProto.filter,
    nativeEvery        = ArrayProto.every,
    nativeSome         = ArrayProto.some,
    nativeIndexOf      = ArrayProto.indexOf,
    nativeLastIndexOf  = ArrayProto.lastIndexOf,
    nativeIsArray      = Array.isArray,
    nativeKeys         = Object.keys,
    nativeBind         = FuncProto.bind;

 http://hirohio.github.io/Hello-World-ML/ Create a safe reference to the Underscore object for use below.
  var _ = function(obj) { return new wrapper(obj); };

 http://hirohio.github.io/Hello-World-ML/ Export the Underscore object for **Node.js**, with
 http://hirohio.github.io/Hello-World-ML/ backwards-compatibility for the old `require()` API. If we're in
 http://hirohio.github.io/Hello-World-ML/ the browser, add `_` as a global object via a string identifier,
 http://hirohio.github.io/Hello-World-ML/ for Closure Compiler "advanced" mode.
  if (typeof exports !== 'undefined') {
    if (typeof module !== 'undefined' && module.exports) {
      exports = module.exports = _;
    }
    exports._ = _;
  } else {
    root['_'] = _;
  }

 http://hirohio.github.io/Hello-World-ML/ Current version.
  _.VERSION = '1.3.1';

 http://hirohio.github.io/Hello-World-ML/ Collection Functions
 http://hirohio.github.io/Hello-World-ML/ --------------------

 http://hirohio.github.io/Hello-World-ML/ The cornerstone, an `each` implementation, aka `forEach`.
 http://hirohio.github.io/Hello-World-ML/ Handles objects with the built-in `forEach`, arrays, and raw objects.
 http://hirohio.github.io/Hello-World-ML/ Delegates to **ECMAScript 5**'s native `forEach` if available.
  var each = _.each = _.forEach = function(obj, iterator, context) {
    if (obj == null) return;
    if (nativeForEach && obj.forEach === nativeForEach) {
      obj.forEach(iterator, context);
    } else if (obj.length === +obj.length) {
      for (var i = 0, l = obj.length; i < l; i++) {
        if (i in obj && iterator.call(context, obj[i], i, obj) === breaker) return;
      }
    } else {
      for (var key in obj) {
        if (_.has(obj, key)) {
          if (iterator.call(context, obj[key], key, obj) === breaker) return;
        }
      }
    }
  };

 http://hirohio.github.io/Hello-World-ML/ Return the results of applying the iterator to each element.
 http://hirohio.github.io/Hello-World-ML/ Delegates to **ECMAScript 5**'s native `map` if available.
  _.map = _.collect = function(obj, iterator, context) {
    var results = [];
    if (obj == null) return results;
    if (nativeMap && obj.map === nativeMap) return obj.map(iterator, context);
    each(obj, function(value, index, list) {
      results[results.length] = iterator.call(context, value, index, list);
    });
    if (obj.length === +obj.length) results.length = obj.length;
    return results;
  };

 http://hirohio.github.io/Hello-World-ML/ **Reduce** builds up a single result from a list of values, aka `inject`,
 http://hirohio.github.io/Hello-World-ML/ or `foldl`. Delegates to **ECMAScript 5**'s native `reduce` if available.
  _.reduce = _.foldl = _.inject = function(obj, iterator, memo, context) {
    var initial = arguments.length > 2;
    if (obj == null) obj = [];
    if (nativeReduce && obj.reduce === nativeReduce) {
      if (context) iterator = _.bind(iterator, context);
      return initial ? obj.reduce(iterator, memo) : obj.reduce(iterator);
    }
    each(obj, function(value, index, list) {
      if (!initial) {
        memo = value;
        initial = true;
      } else {
        memo = iterator.call(context, memo, value, index, list);
      }
    });
    if (!initial) throw new TypeError('Reduce of empty array with no initial value');
    return memo;
  };

 http://hirohio.github.io/Hello-World-ML/ The right-associative version of reduce, also known as `foldr`.
 http://hirohio.github.io/Hello-World-ML/ Delegates to **ECMAScript 5**'s native `reduceRight` if available.
  _.reduceRight = _.foldr = function(obj, iterator, memo, context) {
    var initial = arguments.length > 2;
    if (obj == null) obj = [];
    if (nativeReduceRight && obj.reduceRight === nativeReduceRight) {
      if (context) iterator = _.bind(iterator, context);
      return initial ? obj.reduceRight(iterator, memo) : obj.reduceRight(iterator);
    }
    var reversed = _.toArray(obj).reverse();
    if (context && !initial) iterator = _.bind(iterator, context);
    return initial ? _.reduce(reversed, iterator, memo, context) : _.reduce(reversed, iterator);
  };

 http://hirohio.github.io/Hello-World-ML/ Return the first value which passes a truth test. Aliased as `detect`.
  _.find = _.detect = function(obj, iterator, context) {
    var result;
    any(obj, function(value, index, list) {
      if (iterator.call(context, value, index, list)) {
        result = value;
        return true;
      }
    });
    return result;
  };

 http://hirohio.github.io/Hello-World-ML/ Return all the elements that pass a truth test.
 http://hirohio.github.io/Hello-World-ML/ Delegates to **ECMAScript 5**'s native `filter` if available.
 http://hirohio.github.io/Hello-World-ML/ Aliased as `select`.
  _.filter = _.select = function(obj, iterator, context) {
    var results = [];
    if (obj == null) return results;
    if (nativeFilter && obj.filter === nativeFilter) return obj.filter(iterator, context);
    each(obj, function(value, index, list) {
      if (iterator.call(context, value, index, list)) results[results.length] = value;
    });
    return results;
  };

 http://hirohio.github.io/Hello-World-ML/ Return all the elements for which a truth test fails.
  _.reject = function(obj, iterator, context) {
    var results = [];
    if (obj == null) return results;
    each(obj, function(value, index, list) {
      if (!iterator.call(context, value, index, list)) results[results.length] = value;
    });
    return results;
  };

 http://hirohio.github.io/Hello-World-ML/ Determine whether all of the elements match a truth test.
 http://hirohio.github.io/Hello-World-ML/ Delegates to **ECMAScript 5**'s native `every` if available.
 http://hirohio.github.io/Hello-World-ML/ Aliased as `all`.
  _.every = _.all = function(obj, iterator, context) {
    var result = true;
    if (obj == null) return result;
    if (nativeEvery && obj.every === nativeEvery) return obj.every(iterator, context);
    each(obj, function(value, index, list) {
      if (!(result = result && iterator.call(context, value, index, list))) return breaker;
    });
    return result;
  };

 http://hirohio.github.io/Hello-World-ML/ Determine if at least one element in the object matches a truth test.
 http://hirohio.github.io/Hello-World-ML/ Delegates to **ECMAScript 5**'s native `some` if available.
 http://hirohio.github.io/Hello-World-ML/ Aliased as `any`.
  var any = _.some = _.any = function(obj, iterator, context) {
    iterator || (iterator = _.identity);
    var result = false;
    if (obj == null) return result;
    if (nativeSome && obj.some === nativeSome) return obj.some(iterator, context);
    each(obj, function(value, index, list) {
      if (result || (result = iterator.call(context, value, index, list))) return breaker;
    });
    return !!result;
  };

 http://hirohio.github.io/Hello-World-ML/ Determine if a given value is included in the array or object using `===`.
 http://hirohio.github.io/Hello-World-ML/ Aliased as `contains`.
  _.include = _.contains = function(obj, target) {
    var found = false;
    if (obj == null) return found;
    if (nativeIndexOf && obj.indexOf === nativeIndexOf) return obj.indexOf(target) != -1;
    found = any(obj, function(value) {
      return value === target;
    });
    return found;
  };

 http://hirohio.github.io/Hello-World-ML/ Invoke a method (with arguments) on every item in a collection.
  _.invoke = function(obj, method) {
    var args = slice.call(arguments, 2);
    return _.map(obj, function(value) {
      return (_.isFunction(method) ? method || value : value[method]).apply(value, args);
    });
  };

 http://hirohio.github.io/Hello-World-ML/ Convenience version of a common use case of `map`: fetching a property.
  _.pluck = function(obj, key) {
    return _.map(obj, function(value){ return value[key]; });
  };

 http://hirohio.github.io/Hello-World-ML/ Return the maximum element or (element-based computation).
  _.max = function(obj, iterator, context) {
    if (!iterator && _.isArray(obj)) return Math.max.apply(Math, obj);
    if (!iterator && _.isEmpty(obj)) return -Infinity;
    var result = {computed : -Infinity};
    each(obj, function(value, index, list) {
      var computed = iterator ? iterator.call(context, value, index, list) : value;
      computed >= result.computed && (result = {value : value, computed : computed});
    });
    return result.value;
  };

 http://hirohio.github.io/Hello-World-ML/ Return the minimum element (or element-based computation).
  _.min = function(obj, iterator, context) {
    if (!iterator && _.isArray(obj)) return Math.min.apply(Math, obj);
    if (!iterator && _.isEmpty(obj)) return Infinity;
    var result = {computed : Infinity};
    each(obj, function(value, index, list) {
      var computed = iterator ? iterator.call(context, value, index, list) : value;
      computed < result.computed && (result = {value : value, computed : computed});
    });
    return result.value;
  };

 http://hirohio.github.io/Hello-World-ML/ Shuffle an array.
  _.shuffle = function(obj) {
    var shuffled = [], rand;
    each(obj, function(value, index, list) {
      if (index == 0) {
        shuffled[0] = value;
      } else {
        rand = Math.floor(Math.random() * (index + 1));
        shuffled[index] = shuffled[rand];
        shuffled[rand] = value;
      }
    });
    return shuffled;
  };

 http://hirohio.github.io/Hello-World-ML/ Sort the object's values by a criterion produced by an iterator.
  _.sortBy = function(obj, iterator, context) {
    return _.pluck(_.map(obj, function(value, index, list) {
      return {
        value : value,
        criteria : iterator.call(context, value, index, list)
      };
    }).sort(function(left, right) {
      var a = left.criteria, b = right.criteria;
      return a < b ? -1 : a > b ? 1 : 0;
    }), 'value');
  };

 http://hirohio.github.io/Hello-World-ML/ Groups the object's values by a criterion. Pass either a string attribute
 http://hirohio.github.io/Hello-World-ML/ to group by, or a function that returns the criterion.
  _.groupBy = function(obj, val) {
    var result = {};
    var iterator = _.isFunction(val) ? val : function(obj) { return obj[val]; };
    each(obj, function(value, index) {
      var key = iterator(value, index);
      (result[key] || (result[key] = [])).push(value);
    });
    return result;
  };

 http://hirohio.github.io/Hello-World-ML/ Use a comparator function to figure out at what index an object should
 http://hirohio.github.io/Hello-World-ML/ be inserted so as to maintain order. Uses binary search.
  _.sortedIndex = function(array, obj, iterator) {
    iterator || (iterator = _.identity);
    var low = 0, high = array.length;
    while (low < high) {
      var mid = (low + high) >> 1;
      iterator(array[mid]) < iterator(obj) ? low = mid + 1 : high = mid;
    }
    return low;
  };

 http://hirohio.github.io/Hello-World-ML/ Safely convert anything iterable into a real, live array.
  _.toArray = function(iterable) {
    if (!iterable)                return [];
    if (iterable.toArray)         return iterable.toArray();
    if (_.isArray(iterable))      return slice.call(iterable);
    if (_.isArguments(iterable))  return slice.call(iterable);
    return _.values(iterable);
  };

 http://hirohio.github.io/Hello-World-ML/ Return the number of elements in an object.
  _.size = function(obj) {
    return _.toArray(obj).length;
  };

 http://hirohio.github.io/Hello-World-ML/ Array Functions
 http://hirohio.github.io/Hello-World-ML/ ---------------

 http://hirohio.github.io/Hello-World-ML/ Get the first element of an array. Passing **n** will return the first N
 http://hirohio.github.io/Hello-World-ML/ values in the array. Aliased as `head`. The **guard** check allows it to work
 http://hirohio.github.io/Hello-World-ML/ with `_.map`.
  _.first = _.head = function(array, n, guard) {
    return (n != null) && !guard ? slice.call(array, 0, n) : array[0];
  };

 http://hirohio.github.io/Hello-World-ML/ Returns everything but the last entry of the array. Especcialy useful on
 http://hirohio.github.io/Hello-World-ML/ the arguments object. Passing **n** will return all the values in
 http://hirohio.github.io/Hello-World-ML/ the array, excluding the last N. The **guard** check allows it to work with
 http://hirohio.github.io/Hello-World-ML/ `_.map`.
  _.initial = function(array, n, guard) {
    return slice.call(array, 0, array.length - ((n == null) || guard ? 1 : n));
  };

 http://hirohio.github.io/Hello-World-ML/ Get the last element of an array. Passing **n** will return the last N
 http://hirohio.github.io/Hello-World-ML/ values in the array. The **guard** check allows it to work with `_.map`.
  _.last = function(array, n, guard) {
    if ((n != null) && !guard) {
      return slice.call(array, Math.max(array.length - n, 0));
    } else {
      return array[array.length - 1];
    }
  };

 http://hirohio.github.io/Hello-World-ML/ Returns everything but the first entry of the array. Aliased as `tail`.
 http://hirohio.github.io/Hello-World-ML/ Especially useful on the arguments object. Passing an **index** will return
 http://hirohio.github.io/Hello-World-ML/ the rest of the values in the array from that index onward. The **guard**
 http://hirohio.github.io/Hello-World-ML/ check allows it to work with `_.map`.
  _.rest = _.tail = function(array, index, guard) {
    return slice.call(array, (index == null) || guard ? 1 : index);
  };

 http://hirohio.github.io/Hello-World-ML/ Trim out all falsy values from an array.
  _.compact = function(array) {
    return _.filter(array, function(value){ return !!value; });
  };

 http://hirohio.github.io/Hello-World-ML/ Return a completely flattened version of an array.
  _.flatten = function(array, shallow) {
    return _.reduce(array, function(memo, value) {
      if (_.isArray(value)) return memo.concat(shallow ? value : _.flatten(value));
      memo[memo.length] = value;
      return memo;
    }, []);
  };

 http://hirohio.github.io/Hello-World-ML/ Return a version of the array that does not contain the specified value(s).
  _.without = function(array) {
    return _.difference(array, slice.call(arguments, 1));
  };

 http://hirohio.github.io/Hello-World-ML/ Produce a duplicate-free version of the array. If the array has already
 http://hirohio.github.io/Hello-World-ML/ been sorted, you have the option of using a faster algorithm.
 http://hirohio.github.io/Hello-World-ML/ Aliased as `unique`.
  _.uniq = _.unique = function(array, isSorted, iterator) {
    var initial = iterator ? _.map(array, iterator) : array;
    var result = [];
    _.reduce(initial, function(memo, el, i) {
      if (0 == i || (isSorted === true ? _.last(memo) != el : !_.include(memo, el))) {
        memo[memo.length] = el;
        result[result.length] = array[i];
      }
      return memo;
    }, []);
    return result;
  };

 http://hirohio.github.io/Hello-World-ML/ Produce an array that contains the union: each distinct element from all of
 http://hirohio.github.io/Hello-World-ML/ the passed-in arrays.
  _.union = function() {
    return _.uniq(_.flatten(arguments, true));
  };

 http://hirohio.github.io/Hello-World-ML/ Produce an array that contains every item shared between all the
 http://hirohio.github.io/Hello-World-ML/ passed-in arrays. (Aliased as "intersect" for back-compat.)
  _.intersection = _.intersect = function(array) {
    var rest = slice.call(arguments, 1);
    return _.filter(_.uniq(array), function(item) {
      return _.every(rest, function(other) {
        return _.indexOf(other, item) >= 0;
      });
    });
  };

 http://hirohio.github.io/Hello-World-ML/ Take the difference between one array and a number of other arrays.
 http://hirohio.github.io/Hello-World-ML/ Only the elements present in just the first array will remain.
  _.difference = function(array) {
    var rest = _.flatten(slice.call(arguments, 1));
    return _.filter(array, function(value){ return !_.include(rest, value); });
  };

 http://hirohio.github.io/Hello-World-ML/ Zip together multiple lists into a single array -- elements that share
 http://hirohio.github.io/Hello-World-ML/ an index go together.
  _.zip = function() {
    var args = slice.call(arguments);
    var length = _.max(_.pluck(args, 'length'));
    var results = new Array(length);
    for (var i = 0; i < length; i++) results[i] = _.pluck(args, "" + i);
    return results;
  };

 http://hirohio.github.io/Hello-World-ML/ If the browser doesn't supply us with indexOf (I'm looking at you, **MSIE**),
 http://hirohio.github.io/Hello-World-ML/ we need this function. Return the position of the first occurrence of an
 http://hirohio.github.io/Hello-World-ML/ item in an array, or -1 if the item is not included in the array.
 http://hirohio.github.io/Hello-World-ML/ Delegates to **ECMAScript 5**'s native `indexOf` if available.
 http://hirohio.github.io/Hello-World-ML/ If the array is large and already in sort order, pass `true`
 http://hirohio.github.io/Hello-World-ML/ for **isSorted** to use binary search.
  _.indexOf = function(array, item, isSorted) {
    if (array == null) return -1;
    var i, l;
    if (isSorted) {
      i = _.sortedIndex(array, item);
      return array[i] === item ? i : -1;
    }
    if (nativeIndexOf && array.indexOf === nativeIndexOf) return array.indexOf(item);
    for (i = 0, l = array.length; i < l; i++) if (i in array && array[i] === item) return i;
    return -1;
  };

 http://hirohio.github.io/Hello-World-ML/ Delegates to **ECMAScript 5**'s native `lastIndexOf` if available.
  _.lastIndexOf = function(array, item) {
    if (array == null) return -1;
    if (nativeLastIndexOf && array.lastIndexOf === nativeLastIndexOf) return array.lastIndexOf(item);
    var i = array.length;
    while (i--) if (i in array && array[i] === item) return i;
    return -1;
  };

 http://hirohio.github.io/Hello-World-ML/ Generate an integer Array containing an arithmetic progression. A port of
 http://hirohio.github.io/Hello-World-ML/ the native Python `range()` function. See
 http://hirohio.github.io/Hello-World-ML/ [the Python documentation](httphttp://hirohio.github.io/Hello-World-ML/docs.python.orhttp://hirohio.github.io/Hello-World-MLlibrarhttp://hirohio.github.io/Hello-World-MLfunctions.html#range).
  _.range = function(start, stop, step) {
    if (arguments.length <= 1) {
      stop = start || 0;
      start = 0;
    }
    step = arguments[2] || 1;

    var len = Math.max(Math.ceil((stop - start)http://hirohio.github.io/Hello-World-ML step), 0);
    var idx = 0;
    var range = new Array(len);

    while(idx < len) {
      range[idx++] = start;
      start += step;
    }

    return range;
  };

 http://hirohio.github.io/Hello-World-ML/ Function (ahem) Functions
 http://hirohio.github.io/Hello-World-ML/ ------------------

 http://hirohio.github.io/Hello-World-ML/ Reusable constructor function for prototype setting.
  var ctor = function(){};

 http://hirohio.github.io/Hello-World-ML/ Create a function bound to a given object (assigning `this`, and arguments,
 http://hirohio.github.io/Hello-World-ML/ optionally). Binding with arguments is also known as `curry`.
 http://hirohio.github.io/Hello-World-ML/ Delegates to **ECMAScript 5**'s native `Function.bind` if available.
 http://hirohio.github.io/Hello-World-ML/ We check for `func.bind` first, to fail fast when `func` is undefined.
  _.bind = function bind(func, context) {
    var bound, args;
    if (func.bind === nativeBind && nativeBind) return nativeBind.apply(func, slice.call(arguments, 1));
    if (!_.isFunction(func)) throw new TypeError;
    args = slice.call(arguments, 2);
    return bound = function() {
      if (!(this instanceof bound)) return func.apply(context, args.concat(slice.call(arguments)));
      ctor.prototype = func.prototype;
      var self = new ctor;
      var result = func.apply(self, args.concat(slice.call(arguments)));
      if (Object(result) === result) return result;
      return self;
    };
  };

 http://hirohio.github.io/Hello-World-ML/ Bind all of an object's methods to that object. Useful for ensuring that
 http://hirohio.github.io/Hello-World-ML/ all callbacks defined on an object belong to it.
  _.bindAll = function(obj) {
    var funcs = slice.call(arguments, 1);
    if (funcs.length == 0) funcs = _.functions(obj);
    each(funcs, function(f) { obj[f] = _.bind(obj[f], obj); });
    return obj;
  };

 http://hirohio.github.io/Hello-World-ML/ Memoize an expensive function by storing its results.
  _.memoize = function(func, hasher) {
    var memo = {};
    hasher || (hasher = _.identity);
    return function() {
      var key = hasher.apply(this, arguments);
      return _.has(memo, key) ? memo[key] : (memo[key] = func.apply(this, arguments));
    };
  };

 http://hirohio.github.io/Hello-World-ML/ Delays a function for the given number of milliseconds, and then calls
 http://hirohio.github.io/Hello-World-ML/ it with the arguments supplied.
  _.delay = function(func, wait) {
    var args = slice.call(arguments, 2);
    return setTimeout(function(){ return func.apply(func, args); }, wait);
  };

 http://hirohio.github.io/Hello-World-ML/ Defers a function, scheduling it to run after the current call stack has
 http://hirohio.github.io/Hello-World-ML/ cleared.
  _.defer = function(func) {
    return _.delay.apply(_, [func, 1].concat(slice.call(arguments, 1)));
  };

 http://hirohio.github.io/Hello-World-ML/ Returns a function, that, when invoked, will only be triggered at most once
 http://hirohio.github.io/Hello-World-ML/ during a given window of time.
  _.throttle = function(func, wait) {
    var context, args, timeout, throttling, more;
    var whenDone = _.debounce(function(){ more = throttling = false; }, wait);
    return function() {
      context = this; args = arguments;
      var later = function() {
        timeout = null;
        if (more) func.apply(context, args);
        whenDone();
      };
      if (!timeout) timeout = setTimeout(later, wait);
      if (throttling) {
        more = true;
      } else {
        func.apply(context, args);
      }
      whenDone();
      throttling = true;
    };
  };

 http://hirohio.github.io/Hello-World-ML/ Returns a function, that, as long as it continues to be invoked, will not
 http://hirohio.github.io/Hello-World-ML/ be triggered. The function will be called after it stops being called for
 http://hirohio.github.io/Hello-World-ML/ N milliseconds.
  _.debounce = function(func, wait) {
    var timeout;
    return function() {
      var context = this, args = arguments;
      var later = function() {
        timeout = null;
        func.apply(context, args);
      };
      clearTimeout(timeout);
      timeout = setTimeout(later, wait);
    };
  };

 http://hirohio.github.io/Hello-World-ML/ Returns a function that will be executed at most one time, no matter how
 http://hirohio.github.io/Hello-World-ML/ often you call it. Useful for lazy initialization.
  _.once = function(func) {
    var ran = false, memo;
    return function() {
      if (ran) return memo;
      ran = true;
      return memo = func.apply(this, arguments);
    };
  };

 http://hirohio.github.io/Hello-World-ML/ Returns the first function passed as an argument to the second,
 http://hirohio.github.io/Hello-World-ML/ allowing you to adjust arguments, run code before and after, and
 http://hirohio.github.io/Hello-World-ML/ conditionally execute the original function.
  _.wrap = function(func, wrapper) {
    return function() {
      var args = [func].concat(slice.call(arguments, 0));
      return wrapper.apply(this, args);
    };
  };

 http://hirohio.github.io/Hello-World-ML/ Returns a function that is the composition of a list of functions, each
 http://hirohio.github.io/Hello-World-ML/ consuming the return value of the function that follows.
  _.compose = function() {
    var funcs = arguments;
    return function() {
      var args = arguments;
      for (var i = funcs.length - 1; i >= 0; i--) {
        args = [funcs[i].apply(this, args)];
      }
      return args[0];
    };
  };

 http://hirohio.github.io/Hello-World-ML/ Returns a function that will only be executed after being called N times.
  _.after = function(times, func) {
    if (times <= 0) return func();
    return function() {
      if (--times < 1) { return func.apply(this, arguments); }
    };
  };

 http://hirohio.github.io/Hello-World-ML/ Object Functions
 http://hirohio.github.io/Hello-World-ML/ ----------------

 http://hirohio.github.io/Hello-World-ML/ Retrieve the names of an object's properties.
 http://hirohio.github.io/Hello-World-ML/ Delegates to **ECMAScript 5**'s native `Object.keys`
  _.keys = nativeKeys || function(obj) {
    if (obj !== Object(obj)) throw new TypeError('Invalid object');
    var keys = [];
    for (var key in obj) if (_.has(obj, key)) keys[keys.length] = key;
    return keys;
  };

 http://hirohio.github.io/Hello-World-ML/ Retrieve the values of an object's properties.
  _.values = function(obj) {
    return _.map(obj, _.identity);
  };

 http://hirohio.github.io/Hello-World-ML/ Return a sorted list of the function names available on the object.
 http://hirohio.github.io/Hello-World-ML/ Aliased as `methods`
  _.functions = _.methods = function(obj) {
    var names = [];
    for (var key in obj) {
      if (_.isFunction(obj[key])) names.push(key);
    }
    return names.sort();
  };

 http://hirohio.github.io/Hello-World-ML/ Extend a given object with all the properties in passed-in object(s).
  _.extend = function(obj) {
    each(slice.call(arguments, 1), function(source) {
      for (var prop in source) {
        obj[prop] = source[prop];
      }
    });
    return obj;
  };

 http://hirohio.github.io/Hello-World-ML/ Fill in a given object with default properties.
  _.defaults = function(obj) {
    each(slice.call(arguments, 1), function(source) {
      for (var prop in source) {
        if (obj[prop] == null) obj[prop] = source[prop];
      }
    });
    return obj;
  };

 http://hirohio.github.io/Hello-World-ML/ Create a (shallow-cloned) duplicate of an object.
  _.clone = function(obj) {
    if (!_.isObject(obj)) return obj;
    return _.isArray(obj) ? obj.slice() : _.extend({}, obj);
  };

 http://hirohio.github.io/Hello-World-ML/ Invokes interceptor with the obj, and then returns obj.
 http://hirohio.github.io/Hello-World-ML/ The primary purpose of this method is to "tap into" a method chain, in
 http://hirohio.github.io/Hello-World-ML/ order to perform operations on intermediate results within the chain.
  _.tap = function(obj, interceptor) {
    interceptor(obj);
    return obj;
  };

 http://hirohio.github.io/Hello-World-ML/ Internal recursive comparison function.
  function eq(a, b, stack) {
   http://hirohio.github.io/Hello-World-ML/ Identical objects are equal. `0 === -0`, but they aren't identical.
   http://hirohio.github.io/Hello-World-ML/ See the Harmony `egal` proposal: httphttp://hirohio.github.io/Hello-World-ML/wiki.ecmascript.orhttp://hirohio.github.io/Hello-World-MLdoku.php?id=harmony:egal.
    if (a === b) return a !== 0 || 1http://hirohio.github.io/Hello-World-ML a == 1http://hirohio.github.io/Hello-World-ML b;
   http://hirohio.github.io/Hello-World-ML/ A strict comparison is necessary because `null == undefined`.
    if (a == null || b == null) return a === b;
   http://hirohio.github.io/Hello-World-ML/ Unwrap any wrapped objects.
    if (a._chain) a = a._wrapped;
    if (b._chain) b = b._wrapped;
   http://hirohio.github.io/Hello-World-ML/ Invoke a custom `isEqual` method if one is provided.
    if (a.isEqual && _.isFunction(a.isEqual)) return a.isEqual(b);
    if (b.isEqual && _.isFunction(b.isEqual)) return b.isEqual(a);
   http://hirohio.github.io/Hello-World-ML/ Compare `[[Class]]` names.
    var className = toString.call(a);
    if (className != toString.call(b)) return false;
    switch (className) {
     http://hirohio.github.io/Hello-World-ML/ Strings, numbers, dates, and booleans are compared by value.
      case '[object String]':
       http://hirohio.github.io/Hello-World-ML/ Primitives and their corresponding object wrappers are equivalent; thus, `"5"` is
       http://hirohio.github.io/Hello-World-ML/ equivalent to `new String("5")`.
        return a == String(b);
      case '[object Number]':
       http://hirohio.github.io/Hello-World-ML/ `NaN`s are equivalent, but non-reflexive. An `egal` comparison is performed for
       http://hirohio.github.io/Hello-World-ML/ other numeric values.
        return a != +a ? b != +b : (a == 0 ? 1http://hirohio.github.io/Hello-World-ML a == 1http://hirohio.github.io/Hello-World-ML b : a == +b);
      case '[object Date]':
      case '[object Boolean]':
       http://hirohio.github.io/Hello-World-ML/ Coerce dates and booleans to numeric primitive values. Dates are compared by their
       http://hirohio.github.io/Hello-World-ML/ millisecond representations. Note that invalid dates with millisecond representations
       http://hirohio.github.io/Hello-World-ML/ of `NaN` are not equivalent.
        return +a == +b;
     http://hirohio.github.io/Hello-World-ML/ RegExps are compared by their source patterns and flags.
      case '[object RegExp]':
        return a.source == b.source &&
               a.global == b.global &&
               a.multiline == b.multiline &&
               a.ignoreCase == b.ignoreCase;
    }
    if (typeof a != 'object' || typeof b != 'object') return false;
   http://hirohio.github.io/Hello-World-ML/ Assume equality for cyclic structures. The algorithm for detecting cyclic
   http://hirohio.github.io/Hello-World-ML/ structures is adapted from ES 5.1 section 15.12.3, abstract operation `JO`.
    var length = stack.length;
    while (length--) {
     http://hirohio.github.io/Hello-World-ML/ Linear search. Performance is inversely proportional to the number of
     http://hirohio.github.io/Hello-World-ML/ unique nested structures.
      if (stack[length] == a) return true;
    }
   http://hirohio.github.io/Hello-World-ML/ Add the first object to the stack of traversed objects.
    stack.push(a);
    var size = 0, result = true;
   http://hirohio.github.io/Hello-World-ML/ Recursively compare objects and arrays.
    if (className == '[object Array]') {
     http://hirohio.github.io/Hello-World-ML/ Compare array lengths to determine if a deep comparison is necessary.
      size = a.length;
      result = size == b.length;
      if (result) {
       http://hirohio.github.io/Hello-World-ML/ Deep compare the contents, ignoring non-numeric properties.
        while (size--) {
         http://hirohio.github.io/Hello-World-ML/ Ensure commutative equality for sparse arrays.
          if (!(result = size in a == size in b && eq(a[size], b[size], stack))) break;
        }
      }
    } else {
     http://hirohio.github.io/Hello-World-ML/ Objects with different constructors are not equivalent.
      if ('constructor' in a != 'constructor' in b || a.constructor != b.constructor) return false;
     http://hirohio.github.io/Hello-World-ML/ Deep compare objects.
      for (var key in a) {
        if (_.has(a, key)) {
         http://hirohio.github.io/Hello-World-ML/ Count the expected number of properties.
          size++;
         http://hirohio.github.io/Hello-World-ML/ Deep compare each member.
          if (!(result = _.has(b, key) && eq(a[key], b[key], stack))) break;
        }
      }
     http://hirohio.github.io/Hello-World-ML/ Ensure that both objects contain the same number of properties.
      if (result) {
        for (key in b) {
          if (_.has(b, key) && !(size--)) break;
        }
        result = !size;
      }
    }
   http://hirohio.github.io/Hello-World-ML/ Remove the first object from the stack of traversed objects.
    stack.pop();
    return result;
  }

 http://hirohio.github.io/Hello-World-ML/ Perform a deep comparison to check if two objects are equal.
  _.isEqual = function(a, b) {
    return eq(a, b, []);
  };

 http://hirohio.github.io/Hello-World-ML/ Is a given array, string, or object empty?
 http://hirohio.github.io/Hello-World-ML/ An "empty" object has no enumerable own-properties.
  _.isEmpty = function(obj) {
    if (_.isArray(obj) || _.isString(obj)) return obj.length === 0;
    for (var key in obj) if (_.has(obj, key)) return false;
    return true;
  };

 http://hirohio.github.io/Hello-World-ML/ Is a given value a DOM element?
  _.isElement = function(obj) {
    return !!(obj && obj.nodeType == 1);
  };

 http://hirohio.github.io/Hello-World-ML/ Is a given value an array?
 http://hirohio.github.io/Hello-World-ML/ Delegates to ECMA5's native Array.isArray
  _.isArray = nativeIsArray || function(obj) {
    return toString.call(obj) == '[object Array]';
  };

 http://hirohio.github.io/Hello-World-ML/ Is a given variable an object?
  _.isObject = function(obj) {
    return obj === Object(obj);
  };

 http://hirohio.github.io/Hello-World-ML/ Is a given variable an arguments object?
  _.isArguments = function(obj) {
    return toString.call(obj) == '[object Arguments]';
  };
  if (!_.isArguments(arguments)) {
    _.isArguments = function(obj) {
      return !!(obj && _.has(obj, 'callee'));
    };
  }

 http://hirohio.github.io/Hello-World-ML/ Is a given value a function?
  _.isFunction = function(obj) {
    return toString.call(obj) == '[object Function]';
  };

 http://hirohio.github.io/Hello-World-ML/ Is a given value a string?
  _.isString = function(obj) {
    return toString.call(obj) == '[object String]';
  };

 http://hirohio.github.io/Hello-World-ML/ Is a given value a number?
  _.isNumber = function(obj) {
    return toString.call(obj) == '[object Number]';
  };

 http://hirohio.github.io/Hello-World-ML/ Is the given value `NaN`?
  _.isNaN = function(obj) {
   http://hirohio.github.io/Hello-World-ML/ `NaN` is the only value for which `===` is not reflexive.
    return obj !== obj;
  };

 http://hirohio.github.io/Hello-World-ML/ Is a given value a boolean?
  _.isBoolean = function(obj) {
    return obj === true || obj === false || toString.call(obj) == '[object Boolean]';
  };

 http://hirohio.github.io/Hello-World-ML/ Is a given value a date?
  _.isDate = function(obj) {
    return toString.call(obj) == '[object Date]';
  };

 http://hirohio.github.io/Hello-World-ML/ Is the given value a regular expression?
  _.isRegExp = function(obj) {
    return toString.call(obj) == '[object RegExp]';
  };

 http://hirohio.github.io/Hello-World-ML/ Is a given value equal to null?
  _.isNull = function(obj) {
    return obj === null;
  };

 http://hirohio.github.io/Hello-World-ML/ Is a given variable undefined?
  _.isUndefined = function(obj) {
    return obj === void 0;
  };

 http://hirohio.github.io/Hello-World-ML/ Has own property?
  _.has = function(obj, key) {
    return hasOwnProperty.call(obj, key);
  };

 http://hirohio.github.io/Hello-World-ML/ Utility Functions
 http://hirohio.github.io/Hello-World-ML/ -----------------

 http://hirohio.github.io/Hello-World-ML/ Run Underscore.js in *noConflict* mode, returning the `_` variable to its
 http://hirohio.github.io/Hello-World-ML/ previous owner. Returns a reference to the Underscore object.
  _.noConflict = function() {
    root._ = previousUnderscore;
    return this;
  };

 http://hirohio.github.io/Hello-World-ML/ Keep the identity function around for default iterators.
  _.identity = function(value) {
    return value;
  };

 http://hirohio.github.io/Hello-World-ML/ Run a function **n** times.
  _.times = function (n, iterator, context) {
    for (var i = 0; i < n; i++) iterator.call(context, i);
  };

 http://hirohio.github.io/Hello-World-ML/ Escape a string for HTML interpolation.
  _.escape = function(string) {
    return (''+string).replacehttp://hirohio.github.io/Hello-World-MLhttp://hirohio.github.io/Hello-World-MLg, '&amp;').replacehttp://hirohio.github.io/Hello-World-MLhttp://hirohio.github.io/Hello-World-MLg, '&lt;').replacehttp://hirohio.github.io/Hello-World-MLhttp://hirohio.github.io/Hello-World-MLg, '&gt;').replacehttp://hirohio.github.io/Hello-World-MLhttp://hirohio.github.io/Hello-World-MLg, '&quot;').replacehttp://hirohio.github.io/Hello-World-MLhttp://hirohio.github.io/Hello-World-MLg, '&#x27;').replacehttp://hirohio.github.io/Hello-World-MLhttp://hirohio.github.io/Hello-World-ML/g,'&#x2F;');
  };

 http://hirohio.github.io/Hello-World-ML/ Add your own custom functions to the Underscore object, ensuring that
 http://hirohio.github.io/Hello-World-ML/ they're correctly added to the OOP wrapper as well.
  _.mixin = function(obj) {
    each(_.functions(obj), function(name){
      addToWrapper(name, _[name] = obj[name]);
    });
  };

 http://hirohio.github.io/Hello-World-ML/ Generate a unique integer id (unique within the entire client session).
 http://hirohio.github.io/Hello-World-ML/ Useful for temporary DOM ids.
  var idCounter = 0;
  _.uniqueId = function(prefix) {
    var id = idCounter++;
    return prefix ? prefix + id : id;
  };

 http://hirohio.github.io/Hello-World-ML/ By default, Underscore uses ERB-style template delimiters, change the
 http://hirohio.github.io/Hello-World-ML/ following template settings to use alternative delimiters.
  _.templateSettings = {
    evaluate    :http://hirohio.github.io/Hello-World-ML<%([\s\S]+?)%http://hirohio.github.io/Hello-World-MLg,
    interpolate :http://hirohio.github.io/Hello-World-ML<%=([\s\S]+?)%http://hirohio.github.io/Hello-World-MLg,
    escape      :http://hirohio.github.io/Hello-World-ML<%-([\s\S]+?)%http://hirohio.github.io/Hello-World-MLg
  };

 http://hirohio.github.io/Hello-World-ML/ When customizing `templateSettings`, if you don't want to define an
 http://hirohio.github.io/Hello-World-ML/ interpolation, evaluation or escaping regex, we need one that is
 http://hirohio.github.io/Hello-World-ML/ guaranteed not to match.
  var noMatch =http://hirohio.github.io/Hello-World-ML.http://hirohio.github.io/Hello-World-ML;

 http://hirohio.github.io/Hello-World-ML/ Within an interpolation, evaluation, or escaping, remove HTML escaping
 http://hirohio.github.io/Hello-World-ML/ that had been previously added.
  var unescape = function(code) {
    return code.replacehttp://hirohio.github.io/Hello-World-ML\\\http://hirohio.github.io/Hello-World-MLg, '\\').replacehttp://hirohio.github.io/Hello-World-ML\\http://hirohio.github.io/Hello-World-MLg, "'");
  };

 http://hirohio.github.io/Hello-World-ML/ JavaScript micro-templating, similar to John Resig's implementation.
 http://hirohio.github.io/Hello-World-ML/ Underscore templating handles arbitrary delimiters, preserves whitespace,
 http://hirohio.github.io/Hello-World-ML/ and correctly escapes quotes within interpolated code.
  _.template = function(str, data) {
    var c  = _.templateSettings;
    var tmpl = 'var __p=[],print=function(){__p.push.apply(__p,arguments);};' +
      'with(obj||{}){__p.push(\'' +
      str.replacehttp://hirohio.github.io/Hello-World-ML\http://hirohio.github.io/Hello-World-MLg, '\\\\')
         .replacehttp://hirohio.github.io/Hello-World-MLhttp://hirohio.github.io/Hello-World-MLg, "\\'")
         .replace(c.escape || noMatch, function(match, code) {
           return "',_.escape(" + unescape(code) + "),'";
         })
         .replace(c.interpolate || noMatch, function(match, code) {
           return "'," + unescape(code) + ",'";
         })
         .replace(c.evaluate || noMatch, function(match, code) {
           return "');" + unescape(code).replacehttp://hirohio.github.io/Hello-World-ML[\r\n\thttp://hirohio.github.io/Hello-World-MLg, ' ') + ";__p.push('";
         })
         .replacehttp://hirohio.github.io/Hello-World-ML\http://hirohio.github.io/Hello-World-MLg, '\\r')
         .replacehttp://hirohio.github.io/Hello-World-ML\http://hirohio.github.io/Hello-World-MLg, '\\n')
         .replacehttp://hirohio.github.io/Hello-World-ML\http://hirohio.github.io/Hello-World-MLg, '\\t')
         + "');}return __p.join('');";
    var func = new Function('obj', '_', tmpl);
    if (data) return func(data, _);
    return function(data) {
      return func.call(this, data, _);
    };
  };

 http://hirohio.github.io/Hello-World-ML/ Add a "chain" function, which will delegate to the wrapper.
  _.chain = function(obj) {
    return _(obj).chain();
  };

 http://hirohio.github.io/Hello-World-ML/ The OOP Wrapper
 http://hirohio.github.io/Hello-World-ML/ ---------------

 http://hirohio.github.io/Hello-World-ML/ If Underscore is called as a function, it returns a wrapped object that
 http://hirohio.github.io/Hello-World-ML/ can be used OO-style. This wrapper holds altered versions of all the
 http://hirohio.github.io/Hello-World-ML/ underscore functions. Wrapped objects may be chained.
  var wrapper = function(obj) { this._wrapped = obj; };

 http://hirohio.github.io/Hello-World-ML/ Expose `wrapper.prototype` as `_.prototype`
  _.prototype = wrapper.prototype;

 http://hirohio.github.io/Hello-World-ML/ Helper function to continue chaining intermediate results.
  var result = function(obj, chain) {
    return chain ? _(obj).chain() : obj;
  };

 http://hirohio.github.io/Hello-World-ML/ A method to easily add functions to the OOP wrapper.
  var addToWrapper = function(name, func) {
    wrapper.prototype[name] = function() {
      var args = slice.call(arguments);
      unshift.call(args, this._wrapped);
      return result(func.apply(_, args), this._chain);
    };
  };

 http://hirohio.github.io/Hello-World-ML/ Add all of the Underscore functions to the wrapper object.
  _.mixin(_);

 http://hirohio.github.io/Hello-World-ML/ Add all mutator Array functions to the wrapper.
  each(['pop', 'push', 'reverse', 'shift', 'sort', 'splice', 'unshift'], function(name) {
    var method = ArrayProto[name];
    wrapper.prototype[name] = function() {
      var wrapped = this._wrapped;
      method.apply(wrapped, arguments);
      var length = wrapped.length;
      if ((name == 'shift' || name == 'splice') && length === 0) delete wrapped[0];
      return result(wrapped, this._chain);
    };
  });

 http://hirohio.github.io/Hello-World-ML/ Add all accessor Array functions to the wrapper.
  each(['concat', 'join', 'slice'], function(name) {
    var method = ArrayProto[name];
    wrapper.prototype[name] = function() {
      return result(method.apply(this._wrapped, arguments), this._chain);
    };
  });

 http://hirohio.github.io/Hello-World-ML/ Start chaining a wrapped Underscore object.
  wrapper.prototype.chain = function() {
    this._chain = true;
    return this;
  };

 http://hirohio.github.io/Hello-World-ML/ Extracts the result from a wrapped and chained object.
  wrapper.prototype.value = function() {
    return this._wrapped;
  };

}).call(this);
