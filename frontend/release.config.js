const path = require('path');

const config = {
  branches: [{ name: 'main' }],
  plugins: [
    [
      '@semantic-release/commit-analyzer',
      {
        preset: 'angular',
        releaseRules: path.resolve(__dirname, './config/releaseRules.cjs'),
        parserOpts: {
          noteKeywords: path.resolve(__dirname, './config/noteKeywords.cjs')
        }
      }
    ],
    [
      '@semantic-release/release-notes-generator',
      {
        preset: 'angular',
        parserOpts: {
          noteKeywords: path.resolve(__dirname, './config/noteKeywords.cjs')
        },
        writerOpts: {
          commitSort: ['subject', 'scope']
        }
      }
    ],
    [
      '@semantic-release/changelog',
      {
        changelogFile: path.resolve(__dirname, '../CHANGELOG.md')
      }
    ],
    [
      '@semantic-release/git',
      {
        assets: [
          path.resolve(__dirname, '../CHANGELOG.md'),
          path.resolve(__dirname, 'package.json')
        ],
        message: 'chore(release): ${nextRelease.version} [skip ci]\n\n${nextRelease.notes}'
      }
    ],
    ['@semantic-release/github']
  ]
};

module.exports = config;
