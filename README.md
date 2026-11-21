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

This repository is an unofficial conversion project and is not affiliated with Brave or the AiSList maintainers.

AiSList is licensed under CC BY-NC 4.0. Please refer to the original project for licensing terms.

## License

The conversion script and workflow are provided under the MIT License. The original AiSList data retains its original license and attribution requirements.
