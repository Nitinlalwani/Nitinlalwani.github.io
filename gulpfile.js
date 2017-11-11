var gulp = require('gulp');
var imageResize = require('gulp-image-resize');
var del = require('del');

gulp.task('resize', function () {
    return gulp.src('images/*.*')
        .pipe(imageResize({
            width: 1024,
            imageMagick: true
        }))
        .pipe(gulp.dest('images/fulls'))
        .pipe(imageResize({
            width: 512,
            imageMagick: true
        }))
        .pipe(gulp.dest('images/thumbs'));
});

gulp.task('default', ['resize']);