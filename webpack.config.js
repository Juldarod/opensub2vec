const HtmlWebPackPlugin = require('html-webpack-plugin');
const MiniCssExtractPlugin = require('mini-css-extract-plugin');
const webpack = require('webpack');
const path = require('path');

module.exports = {
    entry: './assets/js/app.js',
    output: {
        path: path.join(__dirname, '/dist'),
        filename: 'app.js',
    },
    module: {
        rules: [
            {
                test: /\.(js|jsx)$/,
                exclude: /node_modules/,
                use: ['babel-loader'],
            },
            {
                test: /\.(sa|sc|c)ss$/,
                use: [MiniCssExtractPlugin.loader, 'css-loader', 'sass-loader'],
            },
            {
                test: /\.(png|jpg)$/,
                use: [
                    {
                        loader: 'file-loader',
                        options: {
                            name: '[name].[ext]',
                            outputPath: 'static/',
                            useRelativePath: true,
                        },
                    },
                ],
            },
            {
                test: /\.ico$/,
                use: [
                    {
                        loader: 'file-loader',
                        options: { name: '[name].[ext]' },
                    },
                ],
            },
        ],
    },
    plugins: [
        new webpack.ProgressPlugin(),
        new HtmlWebPackPlugin({
            template: './assets/index.html',
            favicon: './assets/static/favicon.ico',
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
