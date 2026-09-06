# Reconfiguration of Cortical Processing across Internal States

One of the defining features of human cognition is its continuous dependence on internal variables: the same sensory input, problem, or decision can be processed in qualitatively different ways depending on the state of the individual confronting it.
Far from being a peripheral modulatory detail, this sensitivity to internal state is a fundamental organising principle of cognition.
The systematic study of this phenomenon dates back to some of the earliest work in experimental psychology ([Yerkes & Dodson, 1908](Yerkes1908.pdf)) and remains a very active area of modern neuroscience, which increasingly frames visceral and internal signals as crucial determinants of brain function and behaviour ([Critchley & Harrison, 2013](Critchley2013.pdf)). 
I describe below two such examples, in perception and problem-solving, to illustrate the generality of this principle.

The first example concerns arousal and sensory acuity. Building on the classical observation that performance varies non-monotonically with arousal level ([Yerkes & Dodson, 1908](Yerkes1908.pdf); an increase from *drowsy* to *alert* followed by a decrease from *alert* to *hyper-aroused/stressed*), later work has shown that this relationship is mediated by neuromodulatory systems (most notably the noradrenergic locus coeruleus system) that set a global "gain" on cortical processing, with sensory detection and discrimination performance typically peaking at an intermediate, rather than maximal, level of arousal ([Aston-Jones & Cohen, 2005](AstonJones2005.pdf); [McGinley et al., 2015b](McGinley2015b.pdf)). 

A second example concerns the influence of mood on problem-solving strategy. 
In a now-classic series of experiments, [Isen and colleagues (1987)](Isen1987.pdf) showed that inducing positive affect (even briefly and mildly, via a short comedy film) measurably improved performance on tasks requiring creative insight, without producing comparable benefits on tasks solvable through more effortful, systematic search. 
This effect has since been given a neurobiological grounding: positive affect is associated with increased dopaminergic tone, which broadens the scope of cognitive processing and facilitates more flexible, associative problem-solving strategies, at the potential expense of the narrower, detail-oriented focus better suited to systematic, rule-based tasks ([Ashby et al., 1999](Ashby1999.pdf); see [Baas and colleagues, 2008](Baas2008.pdf) for a meta-analysis and refinements of the mood-creativity relationship).

Taken together, these two examples reveal a common underlying structure: neuromodulatory activity serves as an internal drive that can shift the outcome of cognitive processes ([McCormick et al., 2020](McCormick2020.pdf)). Because perception and problem-solving are, to a large extent, subserved by the neocortex, this implies that internal state must correspond to a modulation of information processing within neocortical circuits themselves. 
The detailed and low-level mechanisms underlying this modulation in the neocortex remain, however, poorly understood. 
My future research therefore aims to address the following question: _what are the circuit-level mechanisms underlying the reconfiguration of information processing in neocortical networks?_

Advances in large-scale recordings, cell-type-specific perturbations, and computational modelling now enable direct and low-level investigations of how internal variables influence neural activity in cortical networks. 
Using mouse vision as an experimental model, my project will leverage these tools to reveal the **computational principles** and **neural mechanisms** underlying **state-dependent processing** in the neocortex.

### Arousal modulation of visual processing in behaving mice

Mouse vision offers an ideal system to address the mechanisms of state-dependent processing in cortical networks ([Niell & Scanziani, 2021](Niell2021.pdf); see also Part \ref{part:intro}). 
Recent work in awake mice has shown that neural dynamics and visual processing in mouse visual cortex (V1) are strongly modulated by internal variables such as arousal, locomotion, and behavioural engagement. 
Early reports showed that locomotion strongly increases visual responses ([Niell & Stryker, 2010](Niell2010.pdf)) while later characterisation revealed a high level of correlation between the rapid fluctuations in arousal levels (quantified by pupil size) and neural dynamics ([McGinley et al., 2015b](McGinley2015b.pdf); [Stringer et al., 2019](Stringer2019.pdf); [De Brito Van Velze et al., 2024](VanVelze2024.pdf)) as well as performance in sensory tasks ([McGinley et al., 2015a](McGinley2015a.pdf); [Musall et al., 2019](Musall2019.pdf)). However, the functional role of those state-dependent neural representations remains controversial. Some studies suggest that increased gain during locomotion or high arousal enhances visual processing ([Dadarlat & Stryker, 2017](Dadarlat2017.pdf); [Akella et al., 2025](Akella2025.pdf)), which could favour stimulus detection. In contrast, others found that this high-gain regime may impair fine-grained encoding, proposing instead that sensory processing is optimal at intermediate arousal levels ([McGinley et al., 2015a](McGinley2015a.pdf); [Neske et al., 2019](Neske2019.pdf)). Importantly, these apparently divergent results may reflect *differences in stimulation protocols* rather than contradiction, pointing toward a broader organising principle of sensory processing.

%%beginFigure%%
![](../Figures/Flex-Prelim.svg)   
**| Preliminary evidence for a qualitative shift in the encoding of information across behavioural states in mouse V1 using 2-photon imaging.**
Top. Firing reliability in quiet and active states (evaluated by cross-correlating pairs of single trial $\Delta$F/F traces, mean ± s.e.m over trial pairs) following the presentation of a natural scene (a natural image with temporal shifts over time). Bottom. Population gain in quiet and active states (quantified as the mean $\Delta$F/F over recorded neurons, mean ± s.e.m over trials) during the presentation of a small faint (low contrast) visual cue. Active and quiet trials were split by a threshold of 0.1cm/s in the mean running speed over the stimulation episode.
Unpublished data (De Brito Van Velze, Rebola & Zerlaut).
%%endFigure%%

Indeed, the debated role of state-dependent modulations might be related to both the type of stimulus used and its associated quantification of neural encoding. If the behavioural state has the ability to change the computational properties of the sensory cortical network, the response to a specific stimulus can be favoured by the computational property of a given state. 

In [Fig.](../Figures/Flex-Prelim.svg), I show preliminary evidence for such a shift in computational properties. In response to a natural scene (a natural image with saccadic shifts, as in 
[Baudot et al., 2013](Baudot2013.pdf)), firing responses are temporally-precise and reliable over trials in the quiet state, indicative of a faithful encoding of this stimulus (in the form of a temporal code), while responses are stronger but more irregular and less reliable in the active states (note the high standard deviation over trials).
On the other hand, for the presentation of a faint (low contrast) transient visual cue, responses display a high-amplitude population response (i.e. averaged over neurons) in the active states, indicative of a robust population encoding (in the form of a rate code), while responses in the quiet state to such a stimulus are much lower and barely detectable. 

Those preliminary observations were a strong motivation for the *flexible computation* hypothesis of this research project: different states are optimal for different stimulus features. They were directly inspired by the theoretical predictions of *Selected Publication \ref{sec:Zerlaut2019}* that predict reliable spatio-temporal sequences in the *quiet-like* state and high-sensitivity population rate code in the *active-like* state.

My research programme below first aims at a systematic investigation of this computational principle.

### Revealing the flexible nature of information processing in mouse V1

%%beginFigure%%
![](../Figures/multi-features-visStim1.svg)   
**| Experimental approach to investigate the interaction between arousal state and visual information features in the mouse visual system.**
**(a)** Design of the stimulus set. A combinatorial set was built by varying 4 core features of visual scenes (with 2 levels each) and 2 sample images thus resulting in $2^5$ =32 different stimuli.
**(b)** Example recording showing 1h of arousal and behavioural monitoring during an experimental session. 
**(c)** Zoom (1min) on the recording period shown in **b** with the simultaneous Neuropixels recording (grey: single units spikes; blue: Multi-Unit Activity; green: Local-Field Potential). Red overlay highlights visual stimulation episodes with their abbreviation (whose meaning is described in **a**).
Unpublished data (Zhang, Rebola & Zerlaut).
%%endFigure%%

The central hypothesis of my project is that *cortical processing is flexible*, adapting dynamically to the animal's current state. 
This framework predicts that different behavioural states may optimise distinct types of sensory computation (for example, favouring fine discrimination in quiet wakefulness versus heightened sensitivity in active/high-arousal states, as suggested in [Fig.](../Figures/Flex-Prelim.svg)).

To capture this flexibility and find what stimulus features are optimally encoded in each state, **we will first characterise the network-level representations of different stimulus types across arousal states**. 

To this end, we have designed an original set of visual stimuli ([Fig.a](../Figures/multi-features-visStim1.svg)). 
This stimulus set is designed to maximise the diversity of neural representations, exploiting differences in the cortical dynamics associated with each stimulus type. 
For example, spatial statistics is assumed to shift sensory-evoked activity from dense (for simple statistics like gratings, "s-") to sparse (for complex statistics like natural images, "s+") representations ([Haider et al., 2010](Haider2010.pdf); [Baudot et al., 2013](Baudot2013.pdf)).
Temporal dynamics will shift sensory-evoked patterns from fixed recruited ensembles (for static images, "t-") to neuronal sequences (for dynamic stimuli, "t+") of neural activity ([Baudot et al., 2013](Baudot2013.pdf)).
Contrast will shift cortical dynamics from vasoactive intestinal peptide (VIP)-dominated (at low contrast, "c-") to somatostatin (SST)-dominated (at high contrast, "c+") regimes ([Millman et al., 2020](Millman2020.pdf)).
Sensory-evoked activity will shift from mostly local processing (small extent, "e-") to strong lateral interactions (large extent, "e+") with increasing stimulus extent ([Angelucci et al., 2002](Angelucci2002.pdf); [Adesnik et al., 2012](Adesnik2012.pdf)).
From those 4 different features, we generate a combinatorial set of stimuli by taking two levels of each and 2 versions of the underlying generating images (useful for later decoding *within one stimulus type*), thus resulting in a set of $2^5$=32 stimuli.

We present this stimulus set with a large number of repetitions (n = 20) in mice that are thoroughly habituated to the recording setup, ensuring that they remain comfortable and are able to freely display transitions across the full range of arousal states. Notably, they should alternate between extended bouts of locomotion and periods of rest and quiet wakefulness over the 1h-long duration of the experimental session (required for this number of repetitions).

Simultaneously, we record neural population activity in V1 using Neuropixels probes ([Jun et al., 2017](Jun2017.pdf)) while monitoring behavioural quantities thanks to video and treadmill rotation recordings (as in [Fig.](../Figures/ephys-awake.svg)). 
The high-density electrophysiological recording will enable single-trial decoding of population responses and the behavioural characterisation will allow classification of arousal/behavioural states. 
This combination will thus allow us to quantify how different states reshape network encoding.

%%beginFigure%%
![](../Figures/multi-features-visStim2.svg)   
**| Firing rate activity (from single units) in response to the 32 stimuli of the combinatorial set.**
The response is shown for all trials (n=20, plain grey curve) as well as for the quiet and active trials (coloured lines, the trials were split with a 0.1cm/s threshold on the running speed). 
Unpublished data (Zhang, Rebola & Zerlaut).
%%endFigure%%

I show a very preliminary analysis of such recordings in 
[Fig.](../Figures/multi-features-visStim2.svg). We computed the firing rate response (i.e. the average of action potentials of spike-sorted single units) and we split states across *active* and *quiet* with a threshold on the running speed. This analysis naturally reveals the strong effect of locomotion on the gain of visually-evoked responses ([Niell & Stryker, 2010](Niell2010.pdf), [Polack et al., 2013](Polack2013.pdf)), but it also hints at more complex effects (e.g. the responses to stimuli with temporal dynamics "t+" are much sharper in the *quiet* state, thus suggesting a potentially more reliable and temporally-precise encoding).

We plan to perform an in-depth analysis of those neural representations. We will develop decoding and information-theoretic analyses ([QuianQuiroga & Panzeri, 2009](QuianQuiroga2009.pdf)) that will infer the state-specific representational subspace itself. This will make it possible to identify which stimulus features are optimally represented in V1 during each arousal/behavioural state, quantify how these representations differ across states, and determine whether gain, shared variability, temporal precision or reliability support these encoding strategies. 

The investigation of the state-dependence will also be refined by defining states of neural activity (e.g. from Local Field Potential dynamics, see [Zerlaut et al., 2022](Zerlaut2022.pdf); [Akella et al., 2025](Akella2025.pdf)).

#### Neural mechanisms of flexible processing

In addition to the unresolved functional role of state-dependent modulation, the underlying **neural mechanism** is still unclear. How can the neural representation of a given stimulus vary across behavioural states? 

At the circuit level, a set of inhibitory interneurons in V1 seems to play a key role during behavioural state transitions. 
Recent studies suggest that these transitions do not modulate all interneuron classes equally ([Bugeon et al., 2022](Bugeon2022.pdf)).
For instance, in V1, parvalbumin-positive (PV+) interneurons are only weakly influenced, or even suppressed, by alert states, whereas SST+ Martinotti cells, VIP+ interneurons, and neuron-derived neurotrophic factor-positive (NDNF)+ interneurons are strongly recruited ([Pakan et al., 2016](Pakan2016.pdf); [Cohen-Kashi Malina et al., 2021](CohenKashiMalina2021.pdf); [De Brito Van Velze et al., 2024](VanVelze2024.pdf)).
Notably, these latter populations share the common feature of modulating apical dendrites of pyramidal neurons through inhibition or disinhibition, placing them in an ideal position to flexibly tune dendritic integration in a state-dependent manner.
This contrasts with soma-targeting PV+ interneurons, which deliver rapid, powerful inhibition of pyramidal neurons and play a central role in stabilising recurrent excitation.
Based on this distinction, we hypothesise that those modulatory interneurons are key circuit elements that enable flexible cortical computations by dynamically modulating integration properties of pyramidal neuron dendrites across behavioural states ([Zerlaut & Tzilivaki, 2025](Zerlaut2025.pdf)).
Supporting this view, optogenetic studies demonstrate that VIP+ activity enhances visual response gain ([Fu et al., 2014](Fu2014.pdf)), SST+ activity improves spike-timing precision ([Rikhye et al., 2021](Rikhye2021.pdf)), and NDNF+ recruitment sharpens feature selectivity ([Cohen-Kashi Malina et al., 2021](CohenKashiMalina2021.pdf)).
Yet, how these modulatory effects align with state-dependent recruitment, and whether they orchestrate shifts in the computational regime of cortical networks, remains unresolved.

To understand the local neural circuits mediating this functional property, we will identify how specific classes of inhibitory interneurons (SST+, VIP+ and NDNF+) contribute to these state-dependent computations. 
Using transgenic Cre-driver lines (SST-Cre, VIP-Cre, NDNF-Cre) combined with targeted transient optogenetic silencing, we will selectively perturb each interneuron class during our neurometric sensory task. 
By assessing how these manipulations alter neural encoding across states, we will determine whether these interneurons serve as circuit-level control points for flexible computation in V1.

### Dysregulations of flexible processing in mouse models of disease

Dysregulations of such state-dependent processing may play a critical role in the pathophysiology of several brain disorders. For example, breakdowns in this flexibility have been linked to schizophrenia ([Saccuzzo & Braff, 1986](Saccuzzo1986.pdf)), where inappropriate coupling between internal state and cortical processing contributes to cognitive dysfunction.
Schizophrenia is a devastating psychiatric condition that affects ~1% of the global population and shortens individuals' lives by ~28 years ([Velligan & Rao, 2023](Velligan2023.pdf)).
Beyond the classical "positive symptoms" associated with the disease (hallucinations, delusions, …), recent research highlighted how impairments in high-order cortex-associated cognitive functions (cognitive flexibility, attention, working memory, cognitive control, …) better predicted the long-term outcome of schizophrenia ([Sohal et al., 2024](Sohal2024.pdf)). 
Such findings thus call for a better understanding of the neurobiological dysregulations affecting cortical computations in schizophrenia. In recent years, the *"GABAergic hypothesis of schizophrenia"* has attracted growing scientific interest ([Lewis et al., 2005](Lewis2005.pdf)). 
As an example, genetic studies showed strong associations between schizophrenia and Neuregulin 1 (Nrg1) as well as its interneuron-specific receptor ErbB4 ([Stefansson et al., 2004](Stefansson2004.pdf)). 
This Nrg1/ErbB4 signalling pathway is essential for the maturation of interneuron circuits critical to normal cortical function ([Rico & Marín, 2011](Rico2011.pdf)). Research efforts initially focused on its impact on PV+ interneurons ([Del Pino et al., 2013](DelPino2013.pdf)). However, the conditional knockout (KO) of ErbB4 on PV+ interneurons only partially recapitulates the schizophrenic-like phenotype of the general ErbB4 knockout, and notably, it fails to account for contextual modulations of behaviour ([Shamir et al., 2012](Shamir2012.pdf)). These findings suggest that higher-order functions, such as context-dependent or flexible computations, may be disrupted in schizophrenia through mechanisms involving interneurons other than PV+ cells (i.e. VIP+, NDNF+ or SST+ interneurons).
Interestingly, the conditional knockout of ErbB4 on VIP+ interneurons leads to a dysregulation of state transitions in primary visual cortex ([Batista-Brito et al., 2017](BatistaBrito2017.pdf)), compatible with their involvement in state-dependent processing.

Therefore, I hypothesise that the dysregulations in the development of inhibitory networks associated with schizophrenia-related mutations impair the proper function of the flexible computation property. 
More specifically, the disease condition corresponds to a setting where the recruitment of inhibitory populations is altered, which impedes the physiological coupling between local cortical network dynamics and behavioural states, thus blocking the ability of the network to change its computational mode to process incoming information. 
Interestingly, alterations in visually evoked potentials in the primary visual cortex (V1), along with deficits in early visual processing, have been observed in patients with schizophrenia ([Butler et al., 2007](Butler2007.pdf)). 

We will test this hypothesis by applying our visual processing characterisation in schizophrenia mouse models. We will start by using the ErbB4 knockout model given its well-documented alterations in cortical interneuron function. We will compare the impact of state-dependent processing in those mice to the results obtained in wild-type mice.


