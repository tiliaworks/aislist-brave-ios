# AiSList – Brave iOS Filters

Automatically converts the community-maintained AiSList YouTube AI-slop channel blocklist into cosmetic filters compatible with **Brave on iOS**.

The generated filter list hides videos from blocked YouTube channels in the mobile YouTube interface.

## Features

- Automatically downloads the latest AiSList blocklist.
- Converts channel handles into Brave-compatible cosmetic filters.
- Ignores comments and empty lines.
- Removes duplicate entries.
- Automatically updates every 6 hours using GitHub Actions.
- No YouTube API key or external services required.

**Subscribe to the generated filter list:**

[aislist_brave.txt](https://raw.githubusercontent.com/tiliaworks/aislist-brave-ios/main/aislist_brave_ios.txt)

## Example

AiSList source entry:


```
@ChannelHandle
```

Generated Brave filter:

```
m.youtube.com##ytm-media-item a:not([class]):is([href="/@ChannelHandle"]):upward(ytm-media-item)
```

## Updating

GitHub Actions automatically checks for changes every 6 hours and updates the generated filter list when necessary.

You can also trigger an update manually through the **Actions** tab.

## Credits

- Original blocklist: [Override92/AiSList](https://github.com/Override92/AiSList)

AiSList is licensed under CC BY-NC 4.0. Please refer to the original project for licensing terms.

This repository is an unofficial conversion project and is not affiliated with Brave or the AiSList maintainers.

## License

The original blocklist is maintained by the AiSList contributors and is licensed under CC BY-NC 4.0. Please credit AiSList and do not use the list for commercial purposes.

This repository converts the original AiSList channel handles into cosmetic filters compatible with Brave Browser on iOS.

The conversion script and GitHub Actions workflow are licensed under the MIT License (see LICENSE).

This is an unofficial community project and is not affiliated with AiSList or Brave.

If AiSList provides an official Brave iOS-compatible filter list in the future, this repository may point to that instead.
