const config = {
    branches: [{ name: 'main' }],
    plugins: [
      [
        '@semantic-release/commit-analyzer',
        {
          preset: 'angular',
          releaseRules: './frontend/config/releaseRules.cjs',
          parserOpts: {
            noteKeywords: './frontend/config/noteKeywords.cjs'
          }
        }
      ],
      [
        '@semantic-release/release-notes-generator',
        {
          preset: 'angular',
          parserOpts: {
            noteKeywords: './frontend/config/noteKeywords.cjs'
          },
          writerOpts: {
            commitSort: ['subject', 'scope']
          }
        }
      ],
      [
        '@semantic-release/changelog',
        {
          changelogFile: 'CHANGELOG.md'
        }
      ],
      [
        '@semantic-release/git',
        {
          assets: ['CHANGELOG.md', './frontend/package.json'],
          message: 'chore(release): ${nextRelease.version} [skip ci]\n\n${nextRelease.notes}'
        }
      ],
      ['@semantic-release/github']
    ]
  };
  
  module.exports = config;