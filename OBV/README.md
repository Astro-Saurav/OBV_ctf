# 📁 OBV — Operation Black Vault: Competition Data

This folder contains the **official exported data** from the *Operation Black Vault (OBV)* Capture The Flag competition hosted on **CTFd**. It serves as a permanent archive of the event's results, team registrations, user accounts, and a full platform backup.

---

## 📅 Event Details

| Field          | Value                                |
|----------------|--------------------------------------|
| **Event Name** | Operation Black Vault (OBV) CTF      |
| **Platform**   | CTFd                                 |
| **Export Date**| 2026-08-01 (13:55:52 UTC)            |
| **Flag Format**| `BVAULT{...}`                        |

---

## 📂 Folder Contents

```
OBV/
├── Operation Black Vault-scoreboard.csv       # Final scoreboard with team rankings & scores
├── Operation Black Vault-teams.csv            # All registered team data
├── Operation Black Vault-users.csv            # All registered user/participant data
└── Operation Black Vault.2026-08-01_13_55_52.zip  # Full CTFd platform backup (export)
```

---

## 📄 File Descriptions

### 1. `Operation Black Vault-scoreboard.csv`
> **Size:** ~17.7 KB &nbsp;|&nbsp; **Rows:** ~369

The **final leaderboard** export from CTFd. Contains a hierarchical view of all ranked teams and their member-level score breakdowns.

**Columns:**

| Column             | Description                                      |
|--------------------|--------------------------------------------------|
| `place`            | Final rank of the team in the competition        |
| `team`             | Team name                                        |
| `team id`          | Unique CTFd ID for the team                      |
| `score`            | Total team score (aggregated from all members)   |
| `member name`      | Individual participant name (nested under team)  |
| `member id`        | Unique CTFd ID for the participant               |
| `member email`     | Participant's registered email address           |
| `member score`     | Individual score contribution from that member   |
| `team bracket id`  | Bracket category ID assigned to the team         |
| `team bracket name`| Name of the bracket (if brackets were used)      |
| `member bracket id`| Bracket ID for the individual member             |
| `member bracket name` | Bracket name for the individual member        |

**Example Row:**
```
1, Binary Sharks, 54, 35400, dev, 103, jrdevadattan2006@gmail.com, 23700, ...
```
> Team **Binary Sharks** ranked **1st** with a total score of **35,400 points**. Member *dev* individually scored **23,700 points**.

---

### 2. `Operation Black Vault-teams.csv`
> **Size:** ~21.4 KB &nbsp;|&nbsp; **Rows:** ~141

The **team registry** export from CTFd. Contains all registered teams and their configuration details.

**Columns:**

| Column        | Description                                              |
|---------------|----------------------------------------------------------|
| `id`          | Unique CTFd team ID                                      |
| `oauth_id`    | OAuth provider ID (if SSO was used)                      |
| `name`        | Team name                                                |
| `email`       | Team contact email                                       |
| `password`    | Hashed team password (`bcrypt-sha256`)                   |
| `secret`      | Team secret/invite code                                  |
| `website`     | Team website (if provided)                               |
| `affiliation` | Team's organization or college affiliation               |
| `country`     | Team's country                                           |
| `bracket_id`  | Assigned competition bracket ID                          |
| `hidden`      | Whether the team is hidden from the scoreboard           |
| `banned`      | Whether the team was banned                              |
| `captain_id`  | CTFd user ID of the team captain                         |
| `created`     | Timestamp of team registration                           |

> **Note:** Passwords are stored as **bcrypt-sha256** hashes and are not recoverable. This is for archival reference only.

---

### 3. `Operation Black Vault-users.csv`
> **Size:** ~66 KB &nbsp;|&nbsp; **Rows:** ~344

The **full user registry** export from CTFd. Contains every individual participant who registered on the platform, including admins.

**Columns:**

| Column            | Description                                              |
|-------------------|----------------------------------------------------------|
| `id`              | Unique CTFd user ID                                      |
| `oauth_id`        | OAuth provider ID (if SSO was used)                      |
| `name`            | Username / display name                                  |
| `password`        | Hashed password (`bcrypt-sha256`)                        |
| `email`           | Registered email address                                 |
| `type`            | Account type: `admin` or `user`                          |
| `secret`          | User secret                                              |
| `website`         | User's personal website (if provided)                    |
| `affiliation`     | User's organization or institution                       |
| `country`         | User's country                                           |
| `bracket_id`      | Assigned bracket ID                                      |
| `hidden`          | Whether the user is hidden from the scoreboard           |
| `banned`          | Whether the user was banned from the platform            |
| `verified`        | Whether the user's email is verified                     |
| `language`        | Preferred language setting                               |
| `change_password` | Flag for forced password change on next login            |
| `team_id`         | CTFd ID of the team the user belongs to                  |
| `created`         | Timestamp of account creation                            |

> **Note:** User `OBV` (ID: 1) is the **admin account** used to manage the platform.

---

### 4. `Operation Black Vault.2026-08-01_13_55_52.zip`
> **Size:** ~41.4 MB

A **complete CTFd platform backup** exported directly from the admin panel. This ZIP archive contains the full state of the CTFd instance at the time of export, including:

- ✅ All **challenge data** (titles, descriptions, point values, flag answers, hints)
- ✅ All **team and user** records
- ✅ All **submission logs** (correct and incorrect attempts)
- ✅ All **scoreboard history** and solve timelines
- ✅ All **files and attachments** uploaded to challenges
- ✅ **Configuration and settings** of the CTFd instance

> **Usage:** This file can be imported into a fresh CTFd instance using **Admin → Config → Import** to fully restore the competition environment.

---

## 🔒 Privacy & Security Notes

> [!CAUTION]
> This folder contains **personally identifiable information (PII)** including participant email addresses. Handle with care and do not share publicly with unauthorized individuals.

> [!WARNING]
> All passwords in the CSV files are **hashed** using `bcrypt-sha256` and cannot be reversed. However, treat these files as sensitive — do not expose them in public-facing environments.

---

## 📊 Competition Summary

| Metric                | Value         |
|-----------------------|---------------|
| Total Registered Users | ~344         |
| Total Registered Teams | ~141         |
| Scoreboard Entries    | ~369          |
| 1st Place Team        | Binary Sharks |
| Top Score             | 35,400 pts    |
| Platform              | CTFd          |

---

## 🔗 Related

- [Main Repository README](../README.md) — Full challenge suite overview
- [Cryptography Challenges](../cryptography/) — Challenge files and writeups
- [All Challenge Categories](../) — Root of the CTF repository
