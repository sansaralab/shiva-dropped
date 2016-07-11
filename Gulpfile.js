var gulp = require("gulp");
var gutil = require("gulp-util");
var sourcemaps = require('gulp-sourcemaps');
var runSequence = require('run-sequence');
var webpack = require("webpack");
var path = require("path");

var paths = {
    jsout: "./tracker/templates/tracker/",
    jsin: "./tracker/src/"
};

gulp.task("default", function (cb) {
    runSequence(["webpack"], cb);
});


gulp.task("webpack", function (callback) {
    webpack({
        devtool: 'cheap',
        entry: [
            paths.jsin + "tracker.js"
        ],
        output: {
            path: paths.jsout,
            filename: "tracker.min.js",
            publicPath: "/tracker/"
        },
        plugins: [
            new webpack.optimize.OccurenceOrderPlugin(),
            new webpack.optimize.DedupePlugin(),
            new webpack.optimize.UglifyJsPlugin({
                compress: {
                    warnings: false
                }
            })
        ],
        module: {
            preLoaders: [
                {
                    test: /\.js$/,
                    loaders: ['eslint'],
                    include: [
                        path.resolve(__dirname)
                    ]
                }
            ]
        }
    }, function (err, stats) {
        if (err) throw new gutil.PluginError("webpack", err);
        gutil.log("[webpack]", stats.toString({
            // output options
        }));
        callback();
    });
});

gulp.task("watch", function () {
    runSequence(["default"]);
    gulp.watch(paths.jsin + "**/*", ["webpack"]);
});