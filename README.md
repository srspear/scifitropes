# scifitropes

## Exploring Science Fiction works and tropes with data from TVTropes.org.

These datasets are a jumping off point for exploring 1) trope density (see "Tropes Count" column) among science fiction works and 2) trope frequency across different subsets of tropes, and 3) each trope's associated works.

The driving idea is that by quantifying different images of the future that appear in science fiction and other media, we can begin to explore different relationships between images of the future and society.

For example, we could try to explore:

* Adding metadata about year of original release in order to explore trope frequencies over time and detect trends in both narrative and speculative fiction tropes across decades, media, etc.
* Analyzing the tropes used in the highest grossing science fiction movies on the list by combining the films list with box office data from another source.
* Identifying works across different media with high trope density but low influence versus low trope density but high influence (cult classics or seminal works)
* Analyzing differences in speculative trope frequencies between Anime and Western Animation in order to explore different cultural perspectives of the future.


## Initial Release

***Note: TVTropes is licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License, so please respect said license when creating any derivative works.***

These top level csv files are each sorted in descending order by the # of tropes listed with that work. 

The main speculative fiction and futuristic tech lists are derived from the [Speculative Fiction Tropes](https://tvtropes.org/pmwiki/pmwiki.php/Main/SpeculativeFictionTropes) and [Futuristic Tech Index](https://tvtropes.org/pmwiki/pmwiki.php/Main/FuturisticTechIndex).
 
The project currently contains:
* **mainscifiworkstropesdb.csv** - The works listed on the media subpages of the [Science Fiction](https://tvtropes.org/pmwiki/pmwiki.php/Main/ScienceFiction) page on TVTropes.org in one file. Contains: 
    * title of the work
    * the number of tropes listed with the work
    * link to the work's page on TVTropes.org
    * list of tropes associated with the works
* **mainspecficandfuturetechtropesdb.csv** - List of tropes from the sites linked above for speculative fiction and futuristic tech tropes
* **examples folder** - code samples
* **media** - smaller csv files broken down by media type (film, tv series, video games, etc)
* **scifisubgenres** - each csv contains a list of works and their urls on TVTropes.org, can be used to filter the main sci-fi works csv to only titles within each subgenre
* **trope_lists** - each csv contains lists of works associated with each trope or group of tropes
