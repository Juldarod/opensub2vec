const HtmlWebPackPlugin = require('html-webpack-plugin');
const MiniCssExtractPlugin = require('mini-css-extract-plugin');
const webpack = require('webpack');
const path = require('path');

module.exports = {
    mode: 'development',
    entry: './assets/js/app.js',
    // output: {
    //     path: path.join(__dirname, '/dist'),
    //     filename: 'app.js',
    // },
    module: {
        rules: [
            {
                test: /\.(js|jsx)$/,
                exclude: /node_modules/,
                use: ['babel-loader'],
            },
            {
                test: /\.s?css$/,
                use: [MiniCssExtractPlugin.loader, 'css-loader', 'sass-loader'],
            },
            {
                test: /\.(png|jpg)$/,
                // options: {
                //     name: '[name].[ext]',
                //     outputPath: 'static/',
                //     useRelativePath: true,
                // },
                type: 'asset/resource',
                generator: { filename: 'static/[name].[ext]' },
                // use: [
                //     {
                //         loader: 'file-loader',
                //         options: {
                //             name: '[name].[ext]',
                //             outputPath: 'static/',
                //             useRelativePath: true,
                //         },
                //     },
                // ],
            },
            {
                test: /\.ico$/,
                // options: { name: '[name].[ext]' },
                type: 'asset/resource',
                generator: { filename: '[name].[ext]' },
                // use: [
                //     {
                //         loader: 'file-loader',
                //         options: { name: '[name].[ext]' },
                //     },
                // ],
            },
        ],
    },
    plugins: [
        new webpack.ProgressPlugin(),
        new HtmlWebPackPlugin({
            template: './assets/index.html',
            favicon: './favicon.ico',
            minify: {
                collapseWhitespace: true,
                removeComments: true,
                removeRedundantAttributes: true,
                removeScriptTypeAttributes: true,
                removeStyleLinkTypeAttributes: true,
                useShortDoctype: true,
            },
        }),
        new MiniCssExtractPlugin({
            filename: 'app.css',
        }),
    ],
};
