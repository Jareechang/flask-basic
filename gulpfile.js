var gulp = require('gulp');
var sass = require('gulp-ruby-sass');
var bower = require('gulp-bower');

var _styleRootDir =  './app/assets/scss';

var paths = {    
    styles: {
        watch: _styleRootDir + '/**/*.scss',
        src: _styleRootDir + '/main.scss',
        dest: './static/css'
    }
};

/**
 *  Bower packages
 */
gulp.task('bower', function(){
    return bower('./bower_components')
            .pipe(gulp.dest('static/'));
}) 

/*
*  Task - Styles 
*/
gulp.task('styles',function(){
    return sass(paths.styles.src, {
        style: 'compressed'
    })    
    .pipe(gulp.dest(paths.styles.dest))    
})

/*
*  Task - Watch 
*/
gulp.task('watch',function(){    
    gulp.watch(paths.styles.watch, ['styles'] );
})

/*
*   Default Runner
*/
gulp.task('watch',['watch']);
gulp.task('buildStyles',['styles']);
gulp.task('buildBower', ['bower']);
