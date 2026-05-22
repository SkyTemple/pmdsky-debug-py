from typing import Protocol, Optional, TypeVar, Generic, no_type_check
from dataclasses import dataclass

A = TypeVar("A")
B = TypeVar("B")


@dataclass
class Symbol(Generic[A, B]):
    # Either a list of at least one address or None if not defined for the region.
    addresses: A
    # Like addresses but memory-absolute
    absolute_addresses: A
    # None for most functions. Data fields should generally have a length defined.
    length: B
    name: str
    description: str
    # C type of this symbol. Empty string if unknown. None for functions.
    c_type: Optional[str]

    @property
    @no_type_check
    def address(self) -> int:
        """First / main address. Raises an IndexError/TypeError if no address is defined."""
        return self.addresses[0]

    @property
    @no_type_check
    def absolute_address(self) -> int:
        """First / main address (absolute). Raises an IndexError/TypeError if no address is defined."""
        return self.absolute_addresses[0]


T = TypeVar("T")
U = TypeVar("U")
L = TypeVar("L")


class SectionProtocol(Protocol[T, U, L]):
    name: str
    description: str
    loadaddress: L
    length: int
    functions: T
    data: U


class Arm7FunctionsProtocol(Protocol):

    _start_arm7: Symbol[
        Optional[list[int]],
        None,
    ]

    do_autoload_arm7: Symbol[
        Optional[list[int]],
        None,
    ]

    StartAutoloadDoneCallbackArm7: Symbol[
        Optional[list[int]],
        None,
    ]

    NitroSpMain: Symbol[
        Optional[list[int]],
        None,
    ]

    HardwareInterrupt: Symbol[
        Optional[list[int]],
        None,
    ]

    ReturnFromInterrupt: Symbol[
        Optional[list[int]],
        None,
    ]

    AudioInterrupt: Symbol[
        Optional[list[int]],
        None,
    ]

    ClearImeFlag: Symbol[
        Optional[list[int]],
        None,
    ]

    ClearIeFlag: Symbol[
        Optional[list[int]],
        None,
    ]

    GetCurrentPlaybackTime: Symbol[
        Optional[list[int]],
        None,
    ]

    ClearIrqFlag: Symbol[
        Optional[list[int]],
        None,
    ]

    EnableIrqFlag: Symbol[
        Optional[list[int]],
        None,
    ]

    SetIrqFlag: Symbol[
        Optional[list[int]],
        None,
    ]

    EnableIrqFiqFlags: Symbol[
        Optional[list[int]],
        None,
    ]

    SetIrqFiqFlags: Symbol[
        Optional[list[int]],
        None,
    ]

    GetProcessorMode: Symbol[
        Optional[list[int]],
        None,
    ]

    _s32_div_f: Symbol[
        Optional[list[int]],
        None,
    ]

    _u32_div_f: Symbol[
        Optional[list[int]],
        None,
    ]

    _u32_div_not_0_f: Symbol[
        Optional[list[int]],
        None,
    ]


class Arm7DataProtocol(Protocol):

    pass


Arm7Protocol = SectionProtocol[
    Arm7FunctionsProtocol,
    Arm7DataProtocol,
    Optional[int],
]


class Arm9FunctionsProtocol(Protocol):

    Svc_SoftReset: Symbol[
        Optional[list[int]],
        None,
    ]

    Svc_WaitByLoop: Symbol[
        Optional[list[int]],
        None,
    ]

    Svc_CpuSet: Symbol[
        Optional[list[int]],
        None,
    ]

    _start: Symbol[
        Optional[list[int]],
        None,
    ]

    InitI_CpuClear32: Symbol[
        Optional[list[int]],
        None,
    ]

    MIi_UncompressBackward: Symbol[
        Optional[list[int]],
        None,
    ]

    do_autoload: Symbol[
        Optional[list[int]],
        None,
    ]

    StartAutoloadDoneCallback: Symbol[
        Optional[list[int]],
        None,
    ]

    init_cp15: Symbol[
        Optional[list[int]],
        None,
    ]

    OSi_ReferSymbol: Symbol[
        Optional[list[int]],
        None,
    ]

    NitroMain: Symbol[
        Optional[list[int]],
        None,
    ]

    InitMemAllocTable: Symbol[
        Optional[list[int]],
        None,
    ]

    SetMemAllocatorParams: Symbol[
        Optional[list[int]],
        None,
    ]

    GetAllocArenaDefault: Symbol[
        Optional[list[int]],
        None,
    ]

    GetFreeArenaDefault: Symbol[
        Optional[list[int]],
        None,
    ]

    InitMemArena: Symbol[
        Optional[list[int]],
        None,
    ]

    MemAllocFlagsToBlockType: Symbol[
        Optional[list[int]],
        None,
    ]

    FindAvailableMemBlock: Symbol[
        Optional[list[int]],
        None,
    ]

    SplitMemBlock: Symbol[
        Optional[list[int]],
        None,
    ]

    MemAlloc: Symbol[
        Optional[list[int]],
        None,
    ]

    MemFree: Symbol[
        Optional[list[int]],
        None,
    ]

    MemArenaAlloc: Symbol[
        Optional[list[int]],
        None,
    ]

    CreateMemArena: Symbol[
        Optional[list[int]],
        None,
    ]

    MemLocateSet: Symbol[
        Optional[list[int]],
        None,
    ]

    MemLocateUnset: Symbol[
        Optional[list[int]],
        None,
    ]

    RoundUpDiv256: Symbol[
        Optional[list[int]],
        None,
    ]

    SinAbs4096: Symbol[
        Optional[list[int]],
        None,
    ]

    CosAbs4096: Symbol[
        Optional[list[int]],
        None,
    ]

    UFixedPoint64CmpLt: Symbol[
        Optional[list[int]],
        None,
    ]

    MultiplyByFixedPoint: Symbol[
        Optional[list[int]],
        None,
    ]

    UMultiplyByFixedPoint: Symbol[
        Optional[list[int]],
        None,
    ]

    IntToFixedPoint64: Symbol[
        Optional[list[int]],
        None,
    ]

    FixedPoint64ToInt: Symbol[
        Optional[list[int]],
        None,
    ]

    FixedPoint32To64: Symbol[
        Optional[list[int]],
        None,
    ]

    NegateFixedPoint64: Symbol[
        Optional[list[int]],
        None,
    ]

    FixedPoint64IsZero: Symbol[
        Optional[list[int]],
        None,
    ]

    FixedPoint64IsNegative: Symbol[
        Optional[list[int]],
        None,
    ]

    FixedPoint64CmpLt: Symbol[
        Optional[list[int]],
        None,
    ]

    MultiplyFixedPoint64: Symbol[
        Optional[list[int]],
        None,
    ]

    DivideFixedPoint64: Symbol[
        Optional[list[int]],
        None,
    ]

    UMultiplyFixedPoint64: Symbol[
        Optional[list[int]],
        None,
    ]

    UDivideFixedPoint64: Symbol[
        Optional[list[int]],
        None,
    ]

    AddFixedPoint64: Symbol[
        Optional[list[int]],
        None,
    ]

    ClampedLn: Symbol[
        Optional[list[int]],
        None,
    ]

    GetRngSeed: Symbol[
        Optional[list[int]],
        None,
    ]

    SetRngSeed: Symbol[
        Optional[list[int]],
        None,
    ]

    Rand16Bit: Symbol[
        Optional[list[int]],
        None,
    ]

    RandInt: Symbol[
        Optional[list[int]],
        None,
    ]

    RandRange: Symbol[
        Optional[list[int]],
        None,
    ]

    Rand32Bit: Symbol[
        Optional[list[int]],
        None,
    ]

    RandIntSafe: Symbol[
        Optional[list[int]],
        None,
    ]

    RandRangeSafe: Symbol[
        Optional[list[int]],
        None,
    ]

    WaitForever: Symbol[
        Optional[list[int]],
        None,
    ]

    InterruptMasterDisable: Symbol[
        Optional[list[int]],
        None,
    ]

    InterruptMasterEnable: Symbol[
        Optional[list[int]],
        None,
    ]

    InitMemAllocTableVeneer: Symbol[
        Optional[list[int]],
        None,
    ]

    ZInit8: Symbol[
        Optional[list[int]],
        None,
    ]

    PointsToZero: Symbol[
        Optional[list[int]],
        None,
    ]

    MemZero: Symbol[
        Optional[list[int]],
        None,
    ]

    MemZero16: Symbol[
        Optional[list[int]],
        None,
    ]

    MemZero32: Symbol[
        Optional[list[int]],
        None,
    ]

    MemsetSimple: Symbol[
        Optional[list[int]],
        None,
    ]

    Memset32: Symbol[
        Optional[list[int]],
        None,
    ]

    MemcpySimple: Symbol[
        Optional[list[int]],
        None,
    ]

    Memcpy16: Symbol[
        Optional[list[int]],
        None,
    ]

    Memcpy32: Symbol[
        Optional[list[int]],
        None,
    ]

    TaskProcBoot: Symbol[
        Optional[list[int]],
        None,
    ]

    EnableAllInterrupts: Symbol[
        Optional[list[int]],
        None,
    ]

    GetTime: Symbol[
        Optional[list[int]],
        None,
    ]

    DisableAllInterrupts: Symbol[
        Optional[list[int]],
        None,
    ]

    SoundResume: Symbol[
        Optional[list[int]],
        None,
    ]

    CardPullOutWithStatus: Symbol[
        Optional[list[int]],
        None,
    ]

    CardPullOut: Symbol[
        Optional[list[int]],
        None,
    ]

    CardBackupError: Symbol[
        Optional[list[int]],
        None,
    ]

    HaltProcessDisp: Symbol[
        Optional[list[int]],
        None,
    ]

    OverlayIsLoaded: Symbol[
        Optional[list[int]],
        None,
    ]

    LoadOverlay: Symbol[
        Optional[list[int]],
        None,
    ]

    UnloadOverlay: Symbol[
        Optional[list[int]],
        None,
    ]

    GetDsFirmwareUserSettingsVeneer: Symbol[
        Optional[list[int]],
        None,
    ]

    Rgb8ToRgb5: Symbol[
        Optional[list[int]],
        None,
    ]

    EuclideanNorm: Symbol[
        Optional[list[int]],
        None,
    ]

    ClampComponentAbs: Symbol[
        Optional[list[int]],
        None,
    ]

    GetHeldButtons: Symbol[
        Optional[list[int]],
        None,
    ]

    GetPressedButtons: Symbol[
        Optional[list[int]],
        None,
    ]

    GetReleasedStylus: Symbol[
        Optional[list[int]],
        None,
    ]

    KeyWaitInit: Symbol[
        Optional[list[int]],
        None,
    ]

    DebugPrintSystemClock: Symbol[
        Optional[list[int]],
        None,
    ]

    GetSystemClock: Symbol[
        Optional[list[int]],
        None,
    ]

    SprintfSystemClock: Symbol[
        Optional[list[int]],
        None,
    ]

    DataTransferInit: Symbol[
        Optional[list[int]],
        None,
    ]

    DataTransferStop: Symbol[
        Optional[list[int]],
        None,
    ]

    FileInitVeneer: Symbol[
        Optional[list[int]],
        None,
    ]

    FileOpen: Symbol[
        Optional[list[int]],
        None,
    ]

    FileGetSize: Symbol[
        Optional[list[int]],
        None,
    ]

    FileRead: Symbol[
        Optional[list[int]],
        None,
    ]

    FileSeek: Symbol[
        Optional[list[int]],
        None,
    ]

    FileClose: Symbol[
        Optional[list[int]],
        None,
    ]

    UnloadFile: Symbol[
        Optional[list[int]],
        None,
    ]

    LoadFileFromRom: Symbol[
        Optional[list[int]],
        None,
    ]

    TransformPaletteDataWithFlushDivideFade: Symbol[
        Optional[list[int]],
        None,
    ]

    UpdateFadeStatus: Symbol[
        Optional[list[int]],
        None,
    ]

    HandleFades: Symbol[
        Optional[list[int]],
        None,
    ]

    HandleFadesVeneer: Symbol[
        Optional[list[int]],
        None,
    ]

    GetFadeStatus: Symbol[
        Optional[list[int]],
        None,
    ]

    InitDebug: Symbol[
        Optional[list[int]],
        None,
    ]

    InitDebugFlag: Symbol[
        Optional[list[int]],
        None,
    ]

    GetDebugFlag: Symbol[
        Optional[list[int]],
        None,
    ]

    SetDebugFlag: Symbol[
        Optional[list[int]],
        None,
    ]

    InitDebugStripped6: Symbol[
        Optional[list[int]],
        None,
    ]

    AppendProgPos: Symbol[
        Optional[list[int]],
        None,
    ]

    InitDebugStripped5: Symbol[
        Optional[list[int]],
        None,
    ]

    DebugPrintTrace: Symbol[
        Optional[list[int]],
        None,
    ]

    DebugDisplay: Symbol[
        Optional[list[int]],
        None,
    ]

    DebugPrint0: Symbol[
        Optional[list[int]],
        None,
    ]

    InitDebugLogFlag: Symbol[
        Optional[list[int]],
        None,
    ]

    GetDebugLogFlag: Symbol[
        Optional[list[int]],
        None,
    ]

    SetDebugLogFlag: Symbol[
        Optional[list[int]],
        None,
    ]

    DebugPrint: Symbol[
        Optional[list[int]],
        None,
    ]

    InitDebugStripped4: Symbol[
        Optional[list[int]],
        None,
    ]

    InitDebugStripped3: Symbol[
        Optional[list[int]],
        None,
    ]

    InitDebugStripped2: Symbol[
        Optional[list[int]],
        None,
    ]

    InitDebugStripped1: Symbol[
        Optional[list[int]],
        None,
    ]

    FatalError: Symbol[
        Optional[list[int]],
        None,
    ]

    OpenAllPackFiles: Symbol[
        Optional[list[int]],
        None,
    ]

    GetFileLengthInPackWithPackNb: Symbol[
        Optional[list[int]],
        None,
    ]

    LoadFileInPackWithPackId: Symbol[
        Optional[list[int]],
        None,
    ]

    AllocAndLoadFileInPack: Symbol[
        Optional[list[int]],
        None,
    ]

    OpenPackFile: Symbol[
        Optional[list[int]],
        None,
    ]

    GetFileLengthInPack: Symbol[
        Optional[list[int]],
        None,
    ]

    LoadFileInPack: Symbol[
        Optional[list[int]],
        None,
    ]

    GetDungeonResultMsg: Symbol[
        Optional[list[int]],
        None,
    ]

    GetDamageSource: Symbol[
        Optional[list[int]],
        None,
    ]

    GetItemCategoryVeneer: Symbol[
        Optional[list[int]],
        None,
    ]

    GetItemMoveId16: Symbol[
        Optional[list[int]],
        None,
    ]

    IsThrownItem: Symbol[
        Optional[list[int]],
        None,
    ]

    IsNotMoney: Symbol[
        Optional[list[int]],
        None,
    ]

    IsEdible: Symbol[
        Optional[list[int]],
        None,
    ]

    IsHM: Symbol[
        Optional[list[int]],
        None,
    ]

    IsGummi: Symbol[
        Optional[list[int]],
        None,
    ]

    IsAuraBow: Symbol[
        Optional[list[int]],
        None,
    ]

    IsLosableItem: Symbol[
        Optional[list[int]],
        None,
    ]

    IsTreasureBox: Symbol[
        Optional[list[int]],
        None,
    ]

    IsStorableItem: Symbol[
        Optional[list[int]],
        None,
    ]

    IsShoppableItem: Symbol[
        Optional[list[int]],
        None,
    ]

    IsValidTargetItem: Symbol[
        Optional[list[int]],
        None,
    ]

    IsItemUsableNow: Symbol[
        Optional[list[int]],
        None,
    ]

    IsTicketItem: Symbol[
        Optional[list[int]],
        None,
    ]

    InitItem: Symbol[
        Optional[list[int]],
        None,
    ]

    InitStandardItem: Symbol[
        Optional[list[int]],
        None,
    ]

    InitBulkItem: Symbol[
        Optional[list[int]],
        None,
    ]

    BulkItemToItem: Symbol[
        Optional[list[int]],
        None,
    ]

    ItemToBulkItem: Symbol[
        Optional[list[int]],
        None,
    ]

    GetDisplayedBuyPrice: Symbol[
        Optional[list[int]],
        None,
    ]

    GetDisplayedSellPrice: Symbol[
        Optional[list[int]],
        None,
    ]

    GetActualBuyPrice: Symbol[
        Optional[list[int]],
        None,
    ]

    GetActualSellPrice: Symbol[
        Optional[list[int]],
        None,
    ]

    FindItemInInventory: Symbol[
        Optional[list[int]],
        None,
    ]

    SprintfStatic: Symbol[
        Optional[list[int]],
        None,
    ]

    ItemZInit: Symbol[
        Optional[list[int]],
        None,
    ]

    AreItemsEquivalent: Symbol[
        Optional[list[int]],
        None,
    ]

    GetItemsForSave: Symbol[
        Optional[list[int]],
        None,
    ]

    ReadItemsFromSave: Symbol[
        Optional[list[int]],
        None,
    ]

    IsItemAvailableInDungeonGroup: Symbol[
        Optional[list[int]],
        None,
    ]

    GetItemIdFromList: Symbol[
        Optional[list[int]],
        None,
    ]

    NormalizeTreasureBox: Symbol[
        Optional[list[int]],
        None,
    ]

    SortItemList: Symbol[
        Optional[list[int]],
        None,
    ]

    RemoveEmptyItems: Symbol[
        Optional[list[int]],
        None,
    ]

    LoadItemPspi2n: Symbol[
        Optional[list[int]],
        None,
    ]

    GetExclusiveItemType: Symbol[
        Optional[list[int]],
        None,
    ]

    GetExclusiveItemOffsetEnsureValid: Symbol[
        Optional[list[int]],
        None,
    ]

    IsItemValid: Symbol[
        Optional[list[int]],
        None,
    ]

    GetExclusiveItemParameter: Symbol[
        Optional[list[int]],
        None,
    ]

    GetItemCategory: Symbol[
        Optional[list[int]],
        None,
    ]

    EnsureValidItem: Symbol[
        Optional[list[int]],
        None,
    ]

    GetItemName: Symbol[
        Optional[list[int]],
        None,
    ]

    GetItemNameFormatted: Symbol[
        Optional[list[int]],
        None,
    ]

    GetItemBuyPrice: Symbol[
        Optional[list[int]],
        None,
    ]

    GetItemSellPrice: Symbol[
        Optional[list[int]],
        None,
    ]

    GetItemSpriteId: Symbol[
        Optional[list[int]],
        None,
    ]

    GetItemPaletteId: Symbol[
        Optional[list[int]],
        None,
    ]

    GetItemActionName: Symbol[
        Optional[list[int]],
        None,
    ]

    GetThrownItemQuantityLimit: Symbol[
        Optional[list[int]],
        None,
    ]

    GetItemMoveId: Symbol[
        Optional[list[int]],
        None,
    ]

    TestItemAiFlag: Symbol[
        Optional[list[int]],
        None,
    ]

    IsItemInTimeDarkness: Symbol[
        Optional[list[int]],
        None,
    ]

    IsItemValidVeneer: Symbol[
        Optional[list[int]],
        None,
    ]

    ReturnEggExclusiveItem: Symbol[
        Optional[list[int]],
        None,
    ]

    SetActiveInventoryToMain: Symbol[
        Optional[list[int]],
        None,
    ]

    AllInventoriesZInit: Symbol[
        Optional[list[int]],
        None,
    ]

    SpecialEpisodeInventoryZInit: Symbol[
        Optional[list[int]],
        None,
    ]

    RescueInventoryZInit: Symbol[
        Optional[list[int]],
        None,
    ]

    SetActiveInventory: Symbol[
        Optional[list[int]],
        None,
    ]

    GetMoneyCarried: Symbol[
        Optional[list[int]],
        None,
    ]

    SetMoneyCarried: Symbol[
        Optional[list[int]],
        None,
    ]

    AddMoneyCarried: Symbol[
        Optional[list[int]],
        None,
    ]

    GetCurrentBagCapacity: Symbol[
        Optional[list[int]],
        None,
    ]

    IsBagFull: Symbol[
        Optional[list[int]],
        None,
    ]

    GetNbItemsInBag: Symbol[
        Optional[list[int]],
        None,
    ]

    CountNbItemsOfTypeInBag: Symbol[
        Optional[list[int]],
        None,
    ]

    CountItemTypeInBag: Symbol[
        Optional[list[int]],
        None,
    ]

    IsItemInBag: Symbol[
        Optional[list[int]],
        None,
    ]

    IsItemWithFlagsInBag: Symbol[
        Optional[list[int]],
        None,
    ]

    IsItemInTreasureBoxes: Symbol[
        Optional[list[int]],
        None,
    ]

    IsHeldItemInBag: Symbol[
        Optional[list[int]],
        None,
    ]

    IsItemForSpecialSpawnInBag: Symbol[
        Optional[list[int]],
        None,
    ]

    HasStorableItems: Symbol[
        Optional[list[int]],
        None,
    ]

    GetItemIndex: Symbol[
        Optional[list[int]],
        None,
    ]

    GetEquivItemIndex: Symbol[
        Optional[list[int]],
        None,
    ]

    GetEquippedThrowableItem: Symbol[
        Optional[list[int]],
        None,
    ]

    GetFirstUnequippedItemOfType: Symbol[
        Optional[list[int]],
        None,
    ]

    CopyItemAtIdx: Symbol[
        Optional[list[int]],
        None,
    ]

    GetItemAtIdx: Symbol[
        Optional[list[int]],
        None,
    ]

    RemoveEmptyItemsInBag: Symbol[
        Optional[list[int]],
        None,
    ]

    RemoveItemNoHole: Symbol[
        Optional[list[int]],
        None,
    ]

    RemoveItem: Symbol[
        Optional[list[int]],
        None,
    ]

    RemoveHeldItemNoHole: Symbol[
        Optional[list[int]],
        None,
    ]

    RemoveItemByIdAndStackNoHole: Symbol[
        Optional[list[int]],
        None,
    ]

    RemoveEquivItem: Symbol[
        Optional[list[int]],
        None,
    ]

    RemoveEquivItemNoHole: Symbol[
        Optional[list[int]],
        None,
    ]

    DecrementStackItem: Symbol[
        Optional[list[int]],
        None,
    ]

    RemoveItemNoHoleCheck: Symbol[
        Optional[list[int]],
        None,
    ]

    RemoveFirstUnequippedItemOfType: Symbol[
        Optional[list[int]],
        None,
    ]

    RemoveAllItems: Symbol[
        Optional[list[int]],
        None,
    ]

    RemoveAllItemsStartingAt: Symbol[
        Optional[list[int]],
        None,
    ]

    SpecialProcAddItemToBag: Symbol[
        Optional[list[int]],
        None,
    ]

    AddItemToBagNoHeld: Symbol[
        Optional[list[int]],
        None,
    ]

    AddItemToBag: Symbol[
        Optional[list[int]],
        None,
    ]

    CleanStickyItemsInBag: Symbol[
        Optional[list[int]],
        None,
    ]

    CountStickyItemsInBag: Symbol[
        Optional[list[int]],
        None,
    ]

    TransmuteHeldItemInBag: Symbol[
        Optional[list[int]],
        None,
    ]

    SetFlagsForHeldItemInBag: Symbol[
        Optional[list[int]],
        None,
    ]

    RemoveHolderForItemInBag: Symbol[
        Optional[list[int]],
        None,
    ]

    SetHolderForItemInBag: Symbol[
        Optional[list[int]],
        None,
    ]

    SortItemsInBag: Symbol[
        Optional[list[int]],
        None,
    ]

    RemovePokeItemsInBag: Symbol[
        Optional[list[int]],
        None,
    ]

    IsStorageFull: Symbol[
        Optional[list[int]],
        None,
    ]

    CountNbOfItemsInStorage: Symbol[
        Optional[list[int]],
        None,
    ]

    CountNbOfValidItemsInStorage: Symbol[
        Optional[list[int]],
        None,
    ]

    CountNbOfValidItemsInTimeDarknessInStorage: Symbol[
        Optional[list[int]],
        None,
    ]

    CountNbItemsOfTypeInStorage: Symbol[
        Optional[list[int]],
        None,
    ]

    CountItemTypeInStorage: Symbol[
        Optional[list[int]],
        None,
    ]

    GetEquivBulkItemIdxInStorage: Symbol[
        Optional[list[int]],
        None,
    ]

    ConvertStorageItemAtIdxToBulkItem: Symbol[
        Optional[list[int]],
        None,
    ]

    ConvertStorageItemAtIdxToItem: Symbol[
        Optional[list[int]],
        None,
    ]

    RemoveItemAtIdxInStorage: Symbol[
        Optional[list[int]],
        None,
    ]

    RemoveBulkItemInStorage: Symbol[
        Optional[list[int]],
        None,
    ]

    RemoveItemInStorage: Symbol[
        Optional[list[int]],
        None,
    ]

    StorageZInit: Symbol[
        Optional[list[int]],
        None,
    ]

    AddBulkItemToStorage: Symbol[
        Optional[list[int]],
        None,
    ]

    AddItemToStorage: Symbol[
        Optional[list[int]],
        None,
    ]

    SortItemsInStorage: Symbol[
        Optional[list[int]],
        None,
    ]

    AllKecleonShopsZInit: Symbol[
        Optional[list[int]],
        None,
    ]

    SpecialEpisodeKecleonShopZInit: Symbol[
        Optional[list[int]],
        None,
    ]

    SetActiveKecleonShop: Symbol[
        Optional[list[int]],
        None,
    ]

    GetMoneyStored: Symbol[
        Optional[list[int]],
        None,
    ]

    SetMoneyStored: Symbol[
        Optional[list[int]],
        None,
    ]

    AddMoneyStored: Symbol[
        Optional[list[int]],
        None,
    ]

    RemoveItemFromKecleonShop1: Symbol[
        Optional[list[int]],
        None,
    ]

    SortKecleonItems1: Symbol[
        Optional[list[int]],
        None,
    ]

    GenerateKecleonItems1: Symbol[
        Optional[list[int]],
        None,
    ]

    AddItemToKecleonShop1: Symbol[
        Optional[list[int]],
        None,
    ]

    RemoveItemFromKecleonShop2: Symbol[
        Optional[list[int]],
        None,
    ]

    SortKecleonItems2: Symbol[
        Optional[list[int]],
        None,
    ]

    GenerateKecleonItems2: Symbol[
        Optional[list[int]],
        None,
    ]

    AddItemToKecleonShop2: Symbol[
        Optional[list[int]],
        None,
    ]

    GetExclusiveItemOffset: Symbol[
        Optional[list[int]],
        None,
    ]

    ApplyExclusiveItemStatBoosts: Symbol[
        Optional[list[int]],
        None,
    ]

    SetExclusiveItemEffect: Symbol[
        Optional[list[int]],
        None,
    ]

    ExclusiveItemEffectFlagTest: Symbol[
        Optional[list[int]],
        None,
    ]

    IsExclusiveItemIdForMonster: Symbol[
        Optional[list[int]],
        None,
    ]

    IsExclusiveItemForMonster: Symbol[
        Optional[list[int]],
        None,
    ]

    BagHasExclusiveItemTypeForMonster: Symbol[
        Optional[list[int]],
        None,
    ]

    GetExclusiveItemForMonsterFromBag: Symbol[
        Optional[list[int]],
        None,
    ]

    GetHpBoostFromExclusiveItems: Symbol[
        Optional[list[int]],
        None,
    ]

    ApplyGummiBoostsToGroundMonster: Symbol[
        Optional[list[int]],
        None,
    ]

    ApplyGummiBoostsToTeamMember: Symbol[
        Optional[list[int]],
        None,
    ]

    ApplySitrusBerryBoostToGroundMonster: Symbol[
        Optional[list[int]],
        None,
    ]

    ApplyLifeSeedBoostToGroundMonster: Symbol[
        Optional[list[int]],
        None,
    ]

    ApplyGinsengToGroundMonster: Symbol[
        Optional[list[int]],
        None,
    ]

    ApplyProteinBoostToGroundMonster: Symbol[
        Optional[list[int]],
        None,
    ]

    ApplyCalciumBoostToGroundMonster: Symbol[
        Optional[list[int]],
        None,
    ]

    ApplyIronBoostToGroundMonster: Symbol[
        Optional[list[int]],
        None,
    ]

    ApplyZincBoostToGroundMonster: Symbol[
        Optional[list[int]],
        None,
    ]

    ApplyNectarBoostToGroundMonster: Symbol[
        Optional[list[int]],
        None,
    ]

    IsMonsterAffectedByGravelyrockGroundMode: Symbol[
        Optional[list[int]],
        None,
    ]

    ApplyGravelyrockBoostToGroundMonster: Symbol[
        Optional[list[int]],
        None,
    ]

    ApplyGummiBoostsGroundMode: Symbol[
        Optional[list[int]],
        None,
    ]

    LoadSynthBin: Symbol[
        Optional[list[int]],
        None,
    ]

    CloseSynthBin: Symbol[
        Optional[list[int]],
        None,
    ]

    GenerateCroagunkItems: Symbol[
        Optional[list[int]],
        None,
    ]

    GetSynthItem: Symbol[
        Optional[list[int]],
        None,
    ]

    GetValidSynthsForSpecies: Symbol[
        Optional[list[int]],
        None,
    ]

    LoadWazaP: Symbol[
        Optional[list[int]],
        None,
    ]

    LoadWazaP2: Symbol[
        Optional[list[int]],
        None,
    ]

    UnloadCurrentWazaP: Symbol[
        Optional[list[int]],
        None,
    ]

    GetMoveName: Symbol[
        Optional[list[int]],
        None,
    ]

    FormatMoveString: Symbol[
        Optional[list[int]],
        None,
    ]

    FormatMoveStringMore: Symbol[
        Optional[list[int]],
        None,
    ]

    InitMove: Symbol[
        Optional[list[int]],
        None,
    ]

    InitMoveCheckId: Symbol[
        Optional[list[int]],
        None,
    ]

    GetInfoMoveGround: Symbol[
        Optional[list[int]],
        None,
    ]

    GetMoveTargetAndRange: Symbol[
        Optional[list[int]],
        None,
    ]

    GetMoveType: Symbol[
        Optional[list[int]],
        None,
    ]

    GetMovesetLevelUpPtr: Symbol[
        Optional[list[int]],
        None,
    ]

    IsInvalidMoveset: Symbol[
        Optional[list[int]],
        None,
    ]

    GetMovesetHmTmPtr: Symbol[
        Optional[list[int]],
        None,
    ]

    GetMovesetEggPtr: Symbol[
        Optional[list[int]],
        None,
    ]

    GetMoveAiWeight: Symbol[
        Optional[list[int]],
        None,
    ]

    GetMoveNbStrikes: Symbol[
        Optional[list[int]],
        None,
    ]

    GetMoveBasePower: Symbol[
        Optional[list[int]],
        None,
    ]

    GetMoveBasePowerGround: Symbol[
        Optional[list[int]],
        None,
    ]

    GetMoveAccuracyOrAiChance: Symbol[
        Optional[list[int]],
        None,
    ]

    GetMoveBasePp: Symbol[
        Optional[list[int]],
        None,
    ]

    GetMaxPp: Symbol[
        Optional[list[int]],
        None,
    ]

    GetMoveMaxGinsengBoost: Symbol[
        Optional[list[int]],
        None,
    ]

    GetMoveMaxGinsengBoostGround: Symbol[
        Optional[list[int]],
        None,
    ]

    GetMoveCritChance: Symbol[
        Optional[list[int]],
        None,
    ]

    IsThawingMove: Symbol[
        Optional[list[int]],
        None,
    ]

    IsUsableWhileTaunted: Symbol[
        Optional[list[int]],
        None,
    ]

    GetMoveRangeId: Symbol[
        Optional[list[int]],
        None,
    ]

    GetMoveActualAccuracy: Symbol[
        Optional[list[int]],
        None,
    ]

    GetMoveBasePowerFromId: Symbol[
        Optional[list[int]],
        None,
    ]

    IsMoveRangeStringUser: Symbol[
        Optional[list[int]],
        None,
    ]

    GetMoveMessageFromId: Symbol[
        Optional[list[int]],
        None,
    ]

    GetNbMoves: Symbol[
        Optional[list[int]],
        None,
    ]

    GetMovesetIdx: Symbol[
        Optional[list[int]],
        None,
    ]

    IsReflectedByMagicCoat: Symbol[
        Optional[list[int]],
        None,
    ]

    CanBeSnatched: Symbol[
        Optional[list[int]],
        None,
    ]

    FailsWhileMuzzled: Symbol[
        Optional[list[int]],
        None,
    ]

    IsSoundMove: Symbol[
        Optional[list[int]],
        None,
    ]

    IsRecoilMove: Symbol[
        Optional[list[int]],
        None,
    ]

    AllManip1: Symbol[
        Optional[list[int]],
        None,
    ]

    AllManip2: Symbol[
        Optional[list[int]],
        None,
    ]

    ManipMoves1v1: Symbol[
        Optional[list[int]],
        None,
    ]

    ManipMoves1v2: Symbol[
        Optional[list[int]],
        None,
    ]

    ManipMoves2v1: Symbol[
        Optional[list[int]],
        None,
    ]

    ManipMoves2v2: Symbol[
        Optional[list[int]],
        None,
    ]

    DungeonMoveToGroundMove: Symbol[
        Optional[list[int]],
        None,
    ]

    GroundToDungeonMoveset: Symbol[
        Optional[list[int]],
        None,
    ]

    DungeonToGroundMoveset: Symbol[
        Optional[list[int]],
        None,
    ]

    GetInfoGroundMoveset: Symbol[
        Optional[list[int]],
        None,
    ]

    FindFirstFreeMovesetIdx: Symbol[
        Optional[list[int]],
        None,
    ]

    LearnMoves: Symbol[
        Optional[list[int]],
        None,
    ]

    CopyMoveToStream: Symbol[
        Optional[list[int]],
        None,
    ]

    CopyMoveFromStream: Symbol[
        Optional[list[int]],
        None,
    ]

    CopyMovesetToStream: Symbol[
        Optional[list[int]],
        None,
    ]

    CopyMovesetFromStream: Symbol[
        Optional[list[int]],
        None,
    ]

    Is2TurnsMove: Symbol[
        Optional[list[int]],
        None,
    ]

    IsRegularAttackOrProjectile: Symbol[
        Optional[list[int]],
        None,
    ]

    IsPunchMove: Symbol[
        Optional[list[int]],
        None,
    ]

    IsHealingWishOrLunarDance: Symbol[
        Optional[list[int]],
        None,
    ]

    IsCopyingMove: Symbol[
        Optional[list[int]],
        None,
    ]

    IsTrappingMove: Symbol[
        Optional[list[int]],
        None,
    ]

    IsOneHitKoMove: Symbol[
        Optional[list[int]],
        None,
    ]

    IsNot2TurnsMoveOrSketch: Symbol[
        Optional[list[int]],
        None,
    ]

    IsRealMove: Symbol[
        Optional[list[int]],
        None,
    ]

    IsMovesetValid: Symbol[
        Optional[list[int]],
        None,
    ]

    IsRealMoveInTimeDarkness: Symbol[
        Optional[list[int]],
        None,
    ]

    IsMovesetValidInTimeDarkness: Symbol[
        Optional[list[int]],
        None,
    ]

    GetFirstNotRealMoveInTimeDarkness: Symbol[
        Optional[list[int]],
        None,
    ]

    IsSameMove: Symbol[
        Optional[list[int]],
        None,
    ]

    GetMoveCategory: Symbol[
        Optional[list[int]],
        None,
    ]

    GetPpIncrease: Symbol[
        Optional[list[int]],
        None,
    ]

    OpenWaza: Symbol[
        Optional[list[int]],
        None,
    ]

    SelectWaza: Symbol[
        Optional[list[int]],
        None,
    ]

    PlayBgmByIdVeneer: Symbol[
        Optional[list[int]],
        None,
    ]

    PlayBgmByIdVolumeVeneer: Symbol[
        Optional[list[int]],
        None,
    ]

    PlaySeByIdVolumeWrapper: Symbol[
        Optional[list[int]],
        None,
    ]

    PlaySeVolumeWrapper: Symbol[
        Optional[list[int]],
        None,
    ]

    PlayBgmById: Symbol[
        Optional[list[int]],
        None,
    ]

    PlayBgmByIdVolume: Symbol[
        Optional[list[int]],
        None,
    ]

    StopBgmCommand: Symbol[
        Optional[list[int]],
        None,
    ]

    PlayMeById: Symbol[
        Optional[list[int]],
        None,
    ]

    PlaySeByIdVolume: Symbol[
        Optional[list[int]],
        None,
    ]

    SendAudioCommand2: Symbol[
        Optional[list[int]],
        None,
    ]

    AllocAudioCommand: Symbol[
        Optional[list[int]],
        None,
    ]

    SendAudioCommand: Symbol[
        Optional[list[int]],
        None,
    ]

    InitSoundSystem: Symbol[
        Optional[list[int]],
        None,
    ]

    ManipBgmPlayback: Symbol[
        Optional[list[int]],
        None,
    ]

    SoundDriverReset: Symbol[
        Optional[list[int]],
        None,
    ]

    LoadDseFile: Symbol[
        Optional[list[int]],
        None,
    ]

    PlaySeLoad: Symbol[
        Optional[list[int]],
        None,
    ]

    IsSongOver: Symbol[
        Optional[list[int]],
        None,
    ]

    PlayBgm: Symbol[
        Optional[list[int]],
        None,
    ]

    StopBgm: Symbol[
        Optional[list[int]],
        None,
    ]

    ChangeBgm: Symbol[
        Optional[list[int]],
        None,
    ]

    PlayBgm2: Symbol[
        Optional[list[int]],
        None,
    ]

    StopBgm2: Symbol[
        Optional[list[int]],
        None,
    ]

    ChangeBgm2: Symbol[
        Optional[list[int]],
        None,
    ]

    PlayME: Symbol[
        Optional[list[int]],
        None,
    ]

    StopME: Symbol[
        Optional[list[int]],
        None,
    ]

    PlaySe: Symbol[
        Optional[list[int]],
        None,
    ]

    PlaySeFullSpec: Symbol[
        Optional[list[int]],
        None,
    ]

    SeChangeVolume: Symbol[
        Optional[list[int]],
        None,
    ]

    SeChangePan: Symbol[
        Optional[list[int]],
        None,
    ]

    StopSe: Symbol[
        Optional[list[int]],
        None,
    ]

    ExecuteCopyToFlatVramCommand: Symbol[
        Optional[list[int]],
        None,
    ]

    DecodeFragmentByteAssemblyTable: Symbol[
        Optional[list[int]],
        None,
    ]

    CopyAndInterleaveWrapper: Symbol[
        Optional[list[int]],
        None,
    ]

    InitAnimationControl: Symbol[
        Optional[list[int]],
        None,
    ]

    InitAnimationControlWithSet: Symbol[
        Optional[list[int]],
        None,
    ]

    SetSpriteIdForAnimationControl: Symbol[
        Optional[list[int]],
        None,
    ]

    SetAnimationForAnimationControlInternal: Symbol[
        Optional[list[int]],
        None,
    ]

    SetAnimationForAnimationControl: Symbol[
        Optional[list[int]],
        None,
    ]

    GetWanForAnimationControl: Symbol[
        Optional[list[int]],
        None,
    ]

    SetAndPlayAnimationForAnimationControl: Symbol[
        Optional[list[int]],
        None,
    ]

    SwitchAnimationControlToNextFrame: Symbol[
        Optional[list[int]],
        None,
    ]

    LoadAnimationFrameAndIncrementInAnimationControl: Symbol[
        Optional[list[int]],
        None,
    ]

    FillOamAttributeInfo: Symbol[
        Optional[list[int]],
        None,
    ]

    AnimationControlGetAllocForMaxFrame: Symbol[
        Optional[list[int]],
        None,
    ]

    DeleteWanTableEntry: Symbol[
        Optional[list[int]],
        None,
    ]

    AllocateWanTableEntry: Symbol[
        Optional[list[int]],
        None,
    ]

    FindWanTableEntry: Symbol[
        Optional[list[int]],
        None,
    ]

    GetLoadedWanTableEntry: Symbol[
        Optional[list[int]],
        None,
    ]

    InitWanTable: Symbol[
        Optional[list[int]],
        None,
    ]

    LoadWanTableEntry: Symbol[
        Optional[list[int]],
        None,
    ]

    LoadWanTableEntryFromPack: Symbol[
        Optional[list[int]],
        None,
    ]

    LoadWanTableEntryFromPackUseProvidedMemory: Symbol[
        Optional[list[int]],
        None,
    ]

    ReplaceWanFromBinFile: Symbol[
        Optional[list[int]],
        None,
    ]

    DeleteWanTableEntryVeneer: Symbol[
        Optional[list[int]],
        None,
    ]

    WanHasAnimationGroup: Symbol[
        Optional[list[int]],
        None,
    ]

    WanTableSpriteHasAnimationGroup: Symbol[
        Optional[list[int]],
        None,
    ]

    SpriteTypeInWanTable: Symbol[
        Optional[list[int]],
        None,
    ]

    LoadWteFromRom: Symbol[
        Optional[list[int]],
        None,
    ]

    LoadWteFromFileDirectory: Symbol[
        Optional[list[int]],
        None,
    ]

    UnloadWte: Symbol[
        Optional[list[int]],
        None,
    ]

    LoadWtuFromBin: Symbol[
        Optional[list[int]],
        None,
    ]

    ProcessWte: Symbol[
        Optional[list[int]],
        None,
    ]

    DelayWteFree: Symbol[
        Optional[list[int]],
        None,
    ]

    ResetPlannedVramTransfer: Symbol[
        Optional[list[int]],
        None,
    ]

    PlanCopyTextureToTextureVram: Symbol[
        Optional[list[int]],
        None,
    ]

    PerformPlannedTextureVramTransfer: Symbol[
        Optional[list[int]],
        None,
    ]

    GeomSetTexImageParam: Symbol[
        Optional[list[int]],
        None,
    ]

    GeomSetVertexCoord16: Symbol[
        Optional[list[int]],
        None,
    ]

    InitRender3dData: Symbol[
        Optional[list[int]],
        None,
    ]

    GeomSwapBuffers: Symbol[
        Optional[list[int]],
        None,
    ]

    InitRender3dElement64: Symbol[
        Optional[list[int]],
        None,
    ]

    Render3d64Texture0x7: Symbol[
        Optional[list[int]],
        None,
    ]

    Render3d64WindowFrame: Symbol[
        Optional[list[int]],
        None,
    ]

    EnqueueRender3d64Tiling: Symbol[
        Optional[list[int]],
        None,
    ]

    Render3d64Tiling: Symbol[
        Optional[list[int]],
        None,
    ]

    Render3d64Quadrilateral: Symbol[
        Optional[list[int]],
        None,
    ]

    Render3d64RectangleMulticolor: Symbol[
        Optional[list[int]],
        None,
    ]

    Render3d64Rectangle: Symbol[
        Optional[list[int]],
        None,
    ]

    Render3d64Nothing: Symbol[
        Optional[list[int]],
        None,
    ]

    Render3d64Texture: Symbol[
        Optional[list[int]],
        None,
    ]

    Render3dElement64: Symbol[
        Optional[list[int]],
        None,
    ]

    HandleSir0Translation: Symbol[
        Optional[list[int]],
        None,
    ]

    ConvertPointersSir0: Symbol[
        Optional[list[int]],
        None,
    ]

    HandleSir0TranslationVeneer: Symbol[
        Optional[list[int]],
        None,
    ]

    DecompressAtNormalVeneer: Symbol[
        Optional[list[int]],
        None,
    ]

    DecompressAtNormal: Symbol[
        Optional[list[int]],
        None,
    ]

    DecompressAtHalf: Symbol[
        Optional[list[int]],
        None,
    ]

    DecompressAtFromMemoryPointerVeneer: Symbol[
        Optional[list[int]],
        None,
    ]

    DecompressAtFromMemoryPointer: Symbol[
        Optional[list[int]],
        None,
    ]

    WriteByteFromMemoryPointer: Symbol[
        Optional[list[int]],
        None,
    ]

    GetAtSize: Symbol[
        Optional[list[int]],
        None,
    ]

    GetLanguageType: Symbol[
        Optional[list[int]],
        None,
    ]

    GetLanguage: Symbol[
        Optional[list[int]],
        None,
    ]

    StrcmpTag: Symbol[
        Optional[list[int]],
        None,
    ]

    AtoiTag: Symbol[
        Optional[list[int]],
        None,
    ]

    AnalyzeText: Symbol[
        Optional[list[int]],
        None,
    ]

    PreprocessString: Symbol[
        Optional[list[int]],
        None,
    ]

    PreprocessStringFromId: Symbol[
        Optional[list[int]],
        None,
    ]

    StrcmpTagVeneer: Symbol[
        Optional[list[int]],
        None,
    ]

    AtoiTagVeneer: Symbol[
        Optional[list[int]],
        None,
    ]

    InitPreprocessorArgs: Symbol[
        Optional[list[int]],
        None,
    ]

    SetStringAccuracy: Symbol[
        Optional[list[int]],
        None,
    ]

    SetStringPower: Symbol[
        Optional[list[int]],
        None,
    ]

    GetRankString: Symbol[
        Optional[list[int]],
        None,
    ]

    GetCurrentTeamNameString: Symbol[
        Optional[list[int]],
        None,
    ]

    GetBagNameString: Symbol[
        Optional[list[int]],
        None,
    ]

    GetSize0x80Buffer: Symbol[
        Optional[list[int]],
        None,
    ]

    GetSize0x80Buffer2: Symbol[
        Optional[list[int]],
        None,
    ]

    GetDungeonResultString: Symbol[
        Optional[list[int]],
        None,
    ]

    SubstitutePlaceholderItemTags: Symbol[
        Optional[list[int]],
        None,
    ]

    SetQuestionMarks: Symbol[
        Optional[list[int]],
        None,
    ]

    StrcpySimple: Symbol[
        Optional[list[int]],
        None,
    ]

    StrncpySimple: Symbol[
        Optional[list[int]],
        None,
    ]

    StrncpySimpleNoPad: Symbol[
        Optional[list[int]],
        None,
    ]

    StrncmpSimple: Symbol[
        Optional[list[int]],
        None,
    ]

    StrncpySimpleNoPadSafe: Symbol[
        Optional[list[int]],
        None,
    ]

    StrcpyName: Symbol[
        Optional[list[int]],
        None,
    ]

    StrncpyName: Symbol[
        Optional[list[int]],
        None,
    ]

    GetStringFromFile: Symbol[
        Optional[list[int]],
        None,
    ]

    LoadStringFile: Symbol[
        Optional[list[int]],
        None,
    ]

    AllocateTemp1024ByteBufferFromPool: Symbol[
        Optional[list[int]],
        None,
    ]

    GetStringFromFileVeneer: Symbol[
        Optional[list[int]],
        None,
    ]

    StringFromId: Symbol[
        Optional[list[int]],
        None,
    ]

    CopyStringFromId: Symbol[
        Optional[list[int]],
        None,
    ]

    CopyNStringFromId: Symbol[
        Optional[list[int]],
        None,
    ]

    LoadTblTalk: Symbol[
        Optional[list[int]],
        None,
    ]

    GetTalkLine: Symbol[
        Optional[list[int]],
        None,
    ]

    IsAOrBPressed: Symbol[
        Optional[list[int]],
        None,
    ]

    DrawTextInWindow: Symbol[
        Optional[list[int]],
        None,
    ]

    GetCharWidth: Symbol[
        Optional[list[int]],
        None,
    ]

    GetColorCodePaletteOffset: Symbol[
        Optional[list[int]],
        None,
    ]

    DrawChar: Symbol[
        Optional[list[int]],
        None,
    ]

    GetWindow: Symbol[
        Optional[list[int]],
        None,
    ]

    NewWindowScreenCheck: Symbol[
        Optional[list[int]],
        None,
    ]

    NewWindow: Symbol[
        Optional[list[int]],
        None,
    ]

    SetScreenWindowsColor: Symbol[
        Optional[list[int]],
        None,
    ]

    SetBothScreensWindowsColor: Symbol[
        Optional[list[int]],
        None,
    ]

    UpdateWindow: Symbol[
        Optional[list[int]],
        None,
    ]

    ClearWindow: Symbol[
        Optional[list[int]],
        None,
    ]

    DeleteWindow: Symbol[
        Optional[list[int]],
        None,
    ]

    GetWindowRectangle: Symbol[
        Optional[list[int]],
        None,
    ]

    GetWindowContents: Symbol[
        Optional[list[int]],
        None,
    ]

    LoadCursors: Symbol[
        Optional[list[int]],
        None,
    ]

    InitWindowTrailer: Symbol[
        Optional[list[int]],
        None,
    ]

    Arm9LoadUnkFieldNa0x2029EC8: Symbol[
        Optional[list[int]],
        None,
    ]

    Arm9StoreUnkFieldNa0x2029ED8: Symbol[
        Optional[list[int]],
        None,
    ]

    LoadAlert: Symbol[
        Optional[list[int]],
        None,
    ]

    PrintClearMark: Symbol[
        Optional[list[int]],
        None,
    ]

    PrintSpecialEpisodeClearMark: Symbol[
        Optional[list[int]],
        None,
    ]

    PrintBadgeMark: Symbol[
        Optional[list[int]],
        None,
    ]

    PrintMark: Symbol[
        Optional[list[int]],
        None,
    ]

    CreateParentMenuFromStringIds: Symbol[
        Optional[list[int]],
        None,
    ]

    IsEmptyString: Symbol[
        Optional[list[int]],
        None,
    ]

    CreateParentMenu: Symbol[
        Optional[list[int]],
        None,
    ]

    CreateParentMenuWrapper: Symbol[
        Optional[list[int]],
        None,
    ]

    CreateParentMenuInternal: Symbol[
        Optional[list[int]],
        None,
    ]

    ResumeParentMenu: Symbol[
        Optional[list[int]],
        None,
    ]

    SetParentMenuState7: Symbol[
        Optional[list[int]],
        None,
    ]

    CloseParentMenu: Symbol[
        Optional[list[int]],
        None,
    ]

    IsParentMenuActive: Symbol[
        Optional[list[int]],
        None,
    ]

    CheckParentMenuField0x1A0: Symbol[
        Optional[list[int]],
        None,
    ]

    GetWindowIdSelectedItemOnPage: Symbol[
        Optional[list[int]],
        None,
    ]

    GetSimpleMenuResult: Symbol[
        Optional[list[int]],
        None,
    ]

    UpdateParentMenu: Symbol[
        Optional[list[int]],
        None,
    ]

    CreateSimpleMenuFromStringIds: Symbol[
        Optional[list[int]],
        None,
    ]

    CreateSimpleMenu: Symbol[
        Optional[list[int]],
        None,
    ]

    CreateSimpleMenuInternal: Symbol[
        Optional[list[int]],
        None,
    ]

    ResumeSimpleMenu: Symbol[
        Optional[list[int]],
        None,
    ]

    CloseSimpleMenu: Symbol[
        Optional[list[int]],
        None,
    ]

    IsSimpleMenuActive: Symbol[
        Optional[list[int]],
        None,
    ]

    CheckSimpleMenuField0x1A0: Symbol[
        Optional[list[int]],
        None,
    ]

    GetSimpleMenuField0x1A4: Symbol[
        Optional[list[int]],
        None,
    ]

    UpdateSimpleMenu: Symbol[
        Optional[list[int]],
        None,
    ]

    SetSimpleMenuField0x1AC: Symbol[
        Optional[list[int]],
        None,
    ]

    CreateAdvancedMenu: Symbol[
        Optional[list[int]],
        None,
    ]

    ResumeAdvancedMenu: Symbol[
        Optional[list[int]],
        None,
    ]

    CloseAdvancedMenu: Symbol[
        Optional[list[int]],
        None,
    ]

    IsAdvancedMenuActive2: Symbol[
        Optional[list[int]],
        None,
    ]

    IsAdvancedMenuActive: Symbol[
        Optional[list[int]],
        None,
    ]

    GetAdvancedMenuCurrentOption: Symbol[
        Optional[list[int]],
        None,
    ]

    GetAdvancedMenuResult: Symbol[
        Optional[list[int]],
        None,
    ]

    UpdateAdvancedMenu: Symbol[
        Optional[list[int]],
        None,
    ]

    DrawAdvancedMenu: Symbol[
        Optional[list[int]],
        None,
    ]

    CreateCollectionMenu: Symbol[
        Optional[list[int]],
        None,
    ]

    SetCollectionMenuField0x1BC: Symbol[
        Optional[list[int]],
        None,
    ]

    SetCollectionMenuWidth: Symbol[
        Optional[list[int]],
        None,
    ]

    CloseCollectionMenu: Symbol[
        Optional[list[int]],
        None,
    ]

    IsCollectionMenuActive: Symbol[
        Optional[list[int]],
        None,
    ]

    SetCollectionMenuField0x1C8: Symbol[
        Optional[list[int]],
        None,
    ]

    SetCollectionMenuField0x1A0: Symbol[
        Optional[list[int]],
        None,
    ]

    SetCollectionMenuField0x1A4: Symbol[
        Optional[list[int]],
        None,
    ]

    SetCollectionMenuVoidFn: Symbol[
        Optional[list[int]],
        None,
    ]

    UpdateCollectionMenu: Symbol[
        Optional[list[int]],
        None,
    ]

    SetCollectionMenuField0x1B2: Symbol[
        Optional[list[int]],
        None,
    ]

    IsCollectionMenuState3: Symbol[
        Optional[list[int]],
        None,
    ]

    CreateOptionsMenu: Symbol[
        Optional[list[int]],
        None,
    ]

    CloseOptionsMenu: Symbol[
        Optional[list[int]],
        None,
    ]

    IsOptionsMenuActive: Symbol[
        Optional[list[int]],
        None,
    ]

    CheckOptionsMenuField0x1A4: Symbol[
        Optional[list[int]],
        None,
    ]

    GetOptionsMenuStates: Symbol[
        Optional[list[int]],
        None,
    ]

    GetOptionsMenuResult: Symbol[
        Optional[list[int]],
        None,
    ]

    UpdateOptionsMenu: Symbol[
        Optional[list[int]],
        None,
    ]

    CreateDebugMenu: Symbol[
        Optional[list[int]],
        None,
    ]

    CloseDebugMenu: Symbol[
        Optional[list[int]],
        None,
    ]

    IsDebugMenuActive: Symbol[
        Optional[list[int]],
        None,
    ]

    CheckDebugMenuField0x1A4: Symbol[
        Optional[list[int]],
        None,
    ]

    UpdateDebugMenu: Symbol[
        Optional[list[int]],
        None,
    ]

    CreateScrollBoxSingle: Symbol[
        Optional[list[int]],
        None,
    ]

    CreateScrollBoxMulti: Symbol[
        Optional[list[int]],
        None,
    ]

    SetScrollBoxState7: Symbol[
        Optional[list[int]],
        None,
    ]

    CloseScrollBox: Symbol[
        Optional[list[int]],
        None,
    ]

    IsScrollBoxActive: Symbol[
        Optional[list[int]],
        None,
    ]

    UpdateScrollBox: Symbol[
        Optional[list[int]],
        None,
    ]

    CreateDialogueBox: Symbol[
        Optional[list[int]],
        None,
    ]

    CloseDialogueBox: Symbol[
        Optional[list[int]],
        None,
    ]

    IsDialogueBoxActive: Symbol[
        Optional[list[int]],
        None,
    ]

    ShowStringIdInDialogueBox: Symbol[
        Optional[list[int]],
        None,
    ]

    ShowStringInDialogueBox: Symbol[
        Optional[list[int]],
        None,
    ]

    ShowDialogueBox: Symbol[
        Optional[list[int]],
        None,
    ]

    ReadStringFromDialogueBox: Symbol[
        Optional[list[int]],
        None,
    ]

    UpdateDialogueBox: Symbol[
        Optional[list[int]],
        None,
    ]

    CreatePortraitBox: Symbol[
        Optional[list[int]],
        None,
    ]

    ClosePortraitBox: Symbol[
        Optional[list[int]],
        None,
    ]

    PortraitBoxNeedsUpdate: Symbol[
        Optional[list[int]],
        None,
    ]

    ShowPortraitInPortraitBox: Symbol[
        Optional[list[int]],
        None,
    ]

    HidePortraitBox: Symbol[
        Optional[list[int]],
        None,
    ]

    UpdatePortraitBox: Symbol[
        Optional[list[int]],
        None,
    ]

    CreateTextBox: Symbol[
        Optional[list[int]],
        None,
    ]

    CreateTextBoxWithArg: Symbol[
        Optional[list[int]],
        None,
    ]

    CloseTextBox: Symbol[
        Optional[list[int]],
        None,
    ]

    CloseTextBox2: Symbol[
        Optional[list[int]],
        None,
    ]

    CreateTextBoxInternal: Symbol[
        Optional[list[int]],
        None,
    ]

    UpdateTextBox: Symbol[
        Optional[list[int]],
        None,
    ]

    IsTextBoxActive: Symbol[
        Optional[list[int]],
        None,
    ]

    CreateAreaNameBox: Symbol[
        Optional[list[int]],
        None,
    ]

    SetAreaNameBoxState3: Symbol[
        Optional[list[int]],
        None,
    ]

    CloseAreaNameBox: Symbol[
        Optional[list[int]],
        None,
    ]

    IsAreaNameBoxActive: Symbol[
        Optional[list[int]],
        None,
    ]

    UpdateAreaNameBox: Symbol[
        Optional[list[int]],
        None,
    ]

    CreateControlsChart: Symbol[
        Optional[list[int]],
        None,
    ]

    CloseControlsChart: Symbol[
        Optional[list[int]],
        None,
    ]

    IsControlsChartActive: Symbol[
        Optional[list[int]],
        None,
    ]

    UpdateControlsChart: Symbol[
        Optional[list[int]],
        None,
    ]

    CreateAlertBox: Symbol[
        Optional[list[int]],
        None,
    ]

    CloseAlertBox: Symbol[
        Optional[list[int]],
        None,
    ]

    AddMessageToAlertBox: Symbol[
        Optional[list[int]],
        None,
    ]

    IsAlertBoxActive: Symbol[
        Optional[list[int]],
        None,
    ]

    UpdateAlertBox: Symbol[
        Optional[list[int]],
        None,
    ]

    CreateAdvancedTextBox: Symbol[
        Optional[list[int]],
        None,
    ]

    CreateAdvancedTextBoxWithArg: Symbol[
        Optional[list[int]],
        None,
    ]

    CreateAdvancedTextBoxInternal: Symbol[
        Optional[list[int]],
        None,
    ]

    SetAdvancedTextBoxPartialMenu: Symbol[
        Optional[list[int]],
        None,
    ]

    SetAdvancedTextBoxField0x1C4: Symbol[
        Optional[list[int]],
        None,
    ]

    SetAdvancedTextBoxField0x1C2: Symbol[
        Optional[list[int]],
        None,
    ]

    CloseAdvancedTextBox2: Symbol[
        Optional[list[int]],
        None,
    ]

    SetAdvancedTextBoxState5: Symbol[
        Optional[list[int]],
        None,
    ]

    CloseAdvancedTextBox: Symbol[
        Optional[list[int]],
        None,
    ]

    IsAdvancedTextBoxActive: Symbol[
        Optional[list[int]],
        None,
    ]

    GetWindowIdPageStart: Symbol[
        Optional[list[int]],
        None,
    ]

    GetAdvancedTextBoxFlags2: Symbol[
        Optional[list[int]],
        None,
    ]

    SetUnkAdvancedTextBoxFn: Symbol[
        Optional[list[int]],
        None,
    ]

    SetUnkAdvancedTextBoxWindowFn: Symbol[
        Optional[list[int]],
        None,
    ]

    UpdateAdvancedTextBox: Symbol[
        Optional[list[int]],
        None,
    ]

    PlayAdvancedTextBoxInputSound: Symbol[
        Optional[list[int]],
        None,
    ]

    CreateTeamSelectionMenu: Symbol[
        Optional[list[int]],
        None,
    ]

    CloseTeamSelectionMenu: Symbol[
        Optional[list[int]],
        None,
    ]

    IsTeamSelectionMenuActive: Symbol[
        Optional[list[int]],
        None,
    ]

    UpdateTeamSelectionMenu: Symbol[
        Optional[list[int]],
        None,
    ]

    IsTeamSelectionMenuState3: Symbol[
        Optional[list[int]],
        None,
    ]

    CalcMenuHeightDiv8: Symbol[
        Optional[list[int]],
        None,
    ]

    InitWindowInput: Symbol[
        Optional[list[int]],
        None,
    ]

    IsMenuOptionActive: Symbol[
        Optional[list[int]],
        None,
    ]

    GetSelectedItemOnPage: Symbol[
        Optional[list[int]],
        None,
    ]

    GetCurrentPage: Symbol[
        Optional[list[int]],
        None,
    ]

    GetPageStart: Symbol[
        Optional[list[int]],
        None,
    ]

    GetSelectedMenuItemIdx: Symbol[
        Optional[list[int]],
        None,
    ]

    GetTotalNumMenuItems: Symbol[
        Optional[list[int]],
        None,
    ]

    GetNumItemsOnPage: Symbol[
        Optional[list[int]],
        None,
    ]

    GetMaxItemsOnPage: Symbol[
        Optional[list[int]],
        None,
    ]

    GetTotalNumPages: Symbol[
        Optional[list[int]],
        None,
    ]

    GetPageItemYOffset: Symbol[
        Optional[list[int]],
        None,
    ]

    PlayWindowInputSound: Symbol[
        Optional[list[int]],
        None,
    ]

    InitInventoryMenuInput: Symbol[
        Optional[list[int]],
        None,
    ]

    OverlayLoadEntriesEqual: Symbol[
        Optional[list[int]],
        None,
    ]

    FreeActiveMenu: Symbol[
        Optional[list[int]],
        None,
    ]

    InitMenu: Symbol[
        Optional[list[int]],
        None,
    ]

    InitMenuWithWindowExtraInfo: Symbol[
        Optional[list[int]],
        None,
    ]

    CopyMenuControlWindowExtraInfo: Symbol[
        Optional[list[int]],
        None,
    ]

    HandleMenus: Symbol[
        Optional[list[int]],
        None,
    ]

    SetupAndShowKeyboard: Symbol[
        Optional[list[int]],
        None,
    ]

    ShowKeyboard: Symbol[
        Optional[list[int]],
        None,
    ]

    GetKeyboardStatus: Symbol[
        Optional[list[int]],
        None,
    ]

    GetKeyboardStringResult: Symbol[
        Optional[list[int]],
        None,
    ]

    TeamSelectionMenuGetItem: Symbol[
        Optional[list[int]],
        None,
    ]

    PrintMoveOptionMenu: Symbol[
        Optional[list[int]],
        None,
    ]

    PrintIqSkillsMenu: Symbol[
        Optional[list[int]],
        None,
    ]

    GetCheckIqMenuSkillString: Symbol[
        Optional[list[int]],
        None,
    ]

    GetNotifyNote: Symbol[
        Optional[list[int]],
        None,
    ]

    SetNotifyNote: Symbol[
        Optional[list[int]],
        None,
    ]

    InitSpecialEpisodeHero: Symbol[
        Optional[list[int]],
        None,
    ]

    EventFlagBackupVeneer: Symbol[
        Optional[list[int]],
        None,
    ]

    InitMainTeamAfterQuiz: Symbol[
        Optional[list[int]],
        None,
    ]

    InitSpecialEpisodePartners: Symbol[
        Optional[list[int]],
        None,
    ]

    InitSpecialEpisodeExtraPartner: Symbol[
        Optional[list[int]],
        None,
    ]

    ReadStringSave: Symbol[
        Optional[list[int]],
        None,
    ]

    CheckStringSave: Symbol[
        Optional[list[int]],
        None,
    ]

    WriteSaveFile: Symbol[
        Optional[list[int]],
        None,
    ]

    ReadSaveFile: Symbol[
        Optional[list[int]],
        None,
    ]

    CalcChecksum: Symbol[
        Optional[list[int]],
        None,
    ]

    CheckChecksumInvalid: Symbol[
        Optional[list[int]],
        None,
    ]

    NoteSaveBase: Symbol[
        Optional[list[int]],
        None,
    ]

    WriteQuickSaveInfo: Symbol[
        Optional[list[int]],
        None,
    ]

    ReadSaveHeader: Symbol[
        Optional[list[int]],
        None,
    ]

    NoteLoadBase: Symbol[
        Optional[list[int]],
        None,
    ]

    ReadQuickSaveInfo: Symbol[
        Optional[list[int]],
        None,
    ]

    InitOptionsVeneer: Symbol[
        Optional[list[int]],
        None,
    ]

    InitOptions: Symbol[
        Optional[list[int]],
        None,
    ]

    GetOptions: Symbol[
        Optional[list[int]],
        None,
    ]

    SetOptions: Symbol[
        Optional[list[int]],
        None,
    ]

    SaveOptionsToCtx: Symbol[
        Optional[list[int]],
        None,
    ]

    LoadOptionsFromCtx: Symbol[
        Optional[list[int]],
        None,
    ]

    IsTouchScreenNotOff: Symbol[
        Optional[list[int]],
        None,
    ]

    IsTouchScreenUseAnywhere: Symbol[
        Optional[list[int]],
        None,
    ]

    GetTopScreenOption: Symbol[
        Optional[list[int]],
        None,
    ]

    SetTopScreenOption: Symbol[
        Optional[list[int]],
        None,
    ]

    GetBottomScreenOption: Symbol[
        Optional[list[int]],
        None,
    ]

    GetGridsOption: Symbol[
        Optional[list[int]],
        None,
    ]

    GetSpeedOption: Symbol[
        Optional[list[int]],
        None,
    ]

    GetFarOffPalsOption: Symbol[
        Optional[list[int]],
        None,
    ]

    GetDamageTurnOption: Symbol[
        Optional[list[int]],
        None,
    ]

    GetDPadAttackOption: Symbol[
        Optional[list[int]],
        None,
    ]

    GetCheckDirectionOption: Symbol[
        Optional[list[int]],
        None,
    ]

    IsMapShownOnEitherScreen: Symbol[
        Optional[list[int]],
        None,
    ]

    IsTeamStatsOnTopScreen: Symbol[
        Optional[list[int]],
        None,
    ]

    IsTextLogOnTopScreen: Symbol[
        Optional[list[int]],
        None,
    ]

    CopyFrameTypeOption: Symbol[
        Optional[list[int]],
        None,
    ]

    SetFrameTypeOption: Symbol[
        Optional[list[int]],
        None,
    ]

    GetGameMode: Symbol[
        Optional[list[int]],
        None,
    ]

    IsGameModeRescue: Symbol[
        Optional[list[int]],
        None,
    ]

    SetGameMode: Symbol[
        Optional[list[int]],
        None,
    ]

    DebugPrintEventFlagSize: Symbol[
        Optional[list[int]],
        None,
    ]

    InitScriptVariableValues: Symbol[
        Optional[list[int]],
        None,
    ]

    InitEventFlagScriptVars: Symbol[
        Optional[list[int]],
        None,
    ]

    DefaultInitScriptVariable: Symbol[
        Optional[list[int]],
        None,
    ]

    ZinitScriptVariable: Symbol[
        Optional[list[int]],
        None,
    ]

    LoadScriptVariableRaw: Symbol[
        Optional[list[int]],
        None,
    ]

    LoadScriptVariableValue: Symbol[
        Optional[list[int]],
        None,
    ]

    LoadScriptVariableValueAtIndex: Symbol[
        Optional[list[int]],
        None,
    ]

    SaveScriptVariableValue: Symbol[
        Optional[list[int]],
        None,
    ]

    SaveScriptVariableValueAtIndex: Symbol[
        Optional[list[int]],
        None,
    ]

    LoadScriptVariableValueSum: Symbol[
        Optional[list[int]],
        None,
    ]

    LoadScriptVariableValueBytes: Symbol[
        Optional[list[int]],
        None,
    ]

    LoadScriptVariableValueString: Symbol[
        Optional[list[int]],
        None,
    ]

    SaveScriptVariableValueBytes: Symbol[
        Optional[list[int]],
        None,
    ]

    ScriptVariablesEqual: Symbol[
        Optional[list[int]],
        None,
    ]

    CalcScriptVariables: Symbol[
        Optional[list[int]],
        None,
    ]

    CompareScriptVariables: Symbol[
        Optional[list[int]],
        None,
    ]

    CalcScriptVariablesVeneer: Symbol[
        Optional[list[int]],
        None,
    ]

    CalcAndUpdateScriptVarWithOtherValue: Symbol[
        Optional[list[int]],
        None,
    ]

    CalcAndUpdateScriptVarWithOtherScriptVar: Symbol[
        Optional[list[int]],
        None,
    ]

    CompareScriptVariablesVeneer: Symbol[
        Optional[list[int]],
        None,
    ]

    LoadAndCompareScriptVarAndValue: Symbol[
        Optional[list[int]],
        None,
    ]

    LoadAndCompareScriptVars: Symbol[
        Optional[list[int]],
        None,
    ]

    EventFlagResume: Symbol[
        Optional[list[int]],
        None,
    ]

    EventFlagBackup: Symbol[
        Optional[list[int]],
        None,
    ]

    DumpScriptVariableValues: Symbol[
        Optional[list[int]],
        None,
    ]

    RestoreScriptVariableValues: Symbol[
        Optional[list[int]],
        None,
    ]

    InitScenarioScriptVars: Symbol[
        Optional[list[int]],
        None,
    ]

    LoadScriptVarValuePair: Symbol[
        Optional[list[int]],
        None,
    ]

    SetScenarioScriptVar: Symbol[
        Optional[list[int]],
        None,
    ]

    IsStoryBeforePoint: Symbol[
        Optional[list[int]],
        None,
    ]

    IsStoryBeforeOrAtPoint: Symbol[
        Optional[list[int]],
        None,
    ]

    IsStoryAtPoint: Symbol[
        Optional[list[int]],
        None,
    ]

    IsStoryAtOrAfterPoint: Symbol[
        Optional[list[int]],
        None,
    ]

    IsStoryAfterPoint: Symbol[
        Optional[list[int]],
        None,
    ]

    GetSpecialEpisodeType: Symbol[
        Optional[list[int]],
        None,
    ]

    SetSpecialEpisodeType: Symbol[
        Optional[list[int]],
        None,
    ]

    GetDebugSpecialEpisodeNumber: Symbol[
        Optional[list[int]],
        None,
    ]

    SetDebugSpecialEpisodeNumber: Symbol[
        Optional[list[int]],
        None,
    ]

    GetExecuteSpecialEpisodeType: Symbol[
        Optional[list[int]],
        None,
    ]

    IsSpecialEpisodeOpen: Symbol[
        Optional[list[int]],
        None,
    ]

    SetSpecialEpisodeOpen: Symbol[
        Optional[list[int]],
        None,
    ]

    IsSpecialEpisodeOpenMismatch: Symbol[
        Optional[list[int]],
        None,
    ]

    IsSpecialEpisodeOpenOld: Symbol[
        Optional[list[int]],
        None,
    ]

    SetSpecialEpisodeOpenOld: Symbol[
        Optional[list[int]],
        None,
    ]

    IsSpecialEpisodeBeaten: Symbol[
        Optional[list[int]],
        None,
    ]

    SetSpecialEpisodeBeaten: Symbol[
        Optional[list[int]],
        None,
    ]

    HasPlayedOldGame: Symbol[
        Optional[list[int]],
        None,
    ]

    GetPerformanceFlagWithChecks: Symbol[
        Optional[list[int]],
        None,
    ]

    SetPerformanceFlagWithChecks: Symbol[
        Optional[list[int]],
        None,
    ]

    GetScenarioBalance: Symbol[
        Optional[list[int]],
        None,
    ]

    ScenarioFlagRestore: Symbol[
        Optional[list[int]],
        None,
    ]

    ScenarioFlagBackup: Symbol[
        Optional[list[int]],
        None,
    ]

    InitWorldMapScriptVars: Symbol[
        Optional[list[int]],
        None,
    ]

    InitDungeonListScriptVars: Symbol[
        Optional[list[int]],
        None,
    ]

    SetDungeonConquest: Symbol[
        Optional[list[int]],
        None,
    ]

    GetDungeonMode: Symbol[
        Optional[list[int]],
        None,
    ]

    GlobalProgressAlloc: Symbol[
        Optional[list[int]],
        None,
    ]

    ResetGlobalProgress: Symbol[
        Optional[list[int]],
        None,
    ]

    SetMonsterFlag1: Symbol[
        Optional[list[int]],
        None,
    ]

    GetMonsterFlag1: Symbol[
        Optional[list[int]],
        None,
    ]

    SetMonsterFlag2: Symbol[
        Optional[list[int]],
        None,
    ]

    HasMonsterBeenAttackedInDungeons: Symbol[
        Optional[list[int]],
        None,
    ]

    SetDungeonTipShown: Symbol[
        Optional[list[int]],
        None,
    ]

    GetDungeonTipShown: Symbol[
        Optional[list[int]],
        None,
    ]

    SetMaxReachedFloor: Symbol[
        Optional[list[int]],
        None,
    ]

    GetMaxReachedFloor: Symbol[
        Optional[list[int]],
        None,
    ]

    IncrementNbAdventures: Symbol[
        Optional[list[int]],
        None,
    ]

    GetNbAdventures: Symbol[
        Optional[list[int]],
        None,
    ]

    CanMonsterSpawn: Symbol[
        Optional[list[int]],
        None,
    ]

    IncrementExclusiveMonsterCounts: Symbol[
        Optional[list[int]],
        None,
    ]

    CopyProgressInfoToStream: Symbol[
        Optional[list[int]],
        None,
    ]

    GetProgressInfoForSave: Symbol[
        Optional[list[int]],
        None,
    ]

    CopyProgressInfoFromStream: Symbol[
        Optional[list[int]],
        None,
    ]

    ReadProgressInfoFromSave: Symbol[
        Optional[list[int]],
        None,
    ]

    InitKaomadoStream: Symbol[
        Optional[list[int]],
        None,
    ]

    InitPortraitParams: Symbol[
        Optional[list[int]],
        None,
    ]

    InitPortraitParamsWithMonsterId: Symbol[
        Optional[list[int]],
        None,
    ]

    SetPortraitEmotion: Symbol[
        Optional[list[int]],
        None,
    ]

    SetPortraitLayout: Symbol[
        Optional[list[int]],
        None,
    ]

    SetPortraitOffset: Symbol[
        Optional[list[int]],
        None,
    ]

    AllowPortraitDefault: Symbol[
        Optional[list[int]],
        None,
    ]

    IsValidPortrait: Symbol[
        Optional[list[int]],
        None,
    ]

    LoadPortrait: Symbol[
        Optional[list[int]],
        None,
    ]

    WonderMailPasswordToMission: Symbol[
        Optional[list[int]],
        None,
    ]

    MissionToWonderMailPassword: Symbol[
        Optional[list[int]],
        None,
    ]

    SetEnterDungeon: Symbol[
        Optional[list[int]],
        None,
    ]

    InitDungeonInit: Symbol[
        Optional[list[int]],
        None,
    ]

    IsNoLossPenaltyDungeon: Symbol[
        Optional[list[int]],
        None,
    ]

    CheckMissionRestrictions: Symbol[
        Optional[list[int]],
        None,
    ]

    TilesetSecondaryTerrainIsChasm: Symbol[
        Optional[list[int]],
        None,
    ]

    GetNbFloors: Symbol[
        Optional[list[int]],
        None,
    ]

    GetNbFloorsPlusOne: Symbol[
        Optional[list[int]],
        None,
    ]

    GetDungeonGroup: Symbol[
        Optional[list[int]],
        None,
    ]

    GetNbPrecedingFloors: Symbol[
        Optional[list[int]],
        None,
    ]

    GetNbFloorsDungeonGroup: Symbol[
        Optional[list[int]],
        None,
    ]

    DungeonFloorToGroupFloor: Symbol[
        Optional[list[int]],
        None,
    ]

    GetMissionRank: Symbol[
        Optional[list[int]],
        None,
    ]

    GetOutlawLevel: Symbol[
        Optional[list[int]],
        None,
    ]

    GetOutlawLeaderLevel: Symbol[
        Optional[list[int]],
        None,
    ]

    GetOutlawMinionLevel: Symbol[
        Optional[list[int]],
        None,
    ]

    AddGuestMonster: Symbol[
        Optional[list[int]],
        None,
    ]

    GetGroundNameId: Symbol[
        Optional[list[int]],
        None,
    ]

    SetAdventureLogStructLocation: Symbol[
        Optional[list[int]],
        None,
    ]

    SetAdventureLogDungeonFloor: Symbol[
        Optional[list[int]],
        None,
    ]

    GetAdventureLogDungeonFloor: Symbol[
        Optional[list[int]],
        None,
    ]

    ClearAdventureLogStruct: Symbol[
        Optional[list[int]],
        None,
    ]

    SetAdventureLogCompleted: Symbol[
        Optional[list[int]],
        None,
    ]

    IsAdventureLogNotEmpty: Symbol[
        Optional[list[int]],
        None,
    ]

    GetAdventureLogCompleted: Symbol[
        Optional[list[int]],
        None,
    ]

    IncrementNbDungeonsCleared: Symbol[
        Optional[list[int]],
        None,
    ]

    GetNbDungeonsCleared: Symbol[
        Optional[list[int]],
        None,
    ]

    IncrementNbFriendRescues: Symbol[
        Optional[list[int]],
        None,
    ]

    GetNbFriendRescues: Symbol[
        Optional[list[int]],
        None,
    ]

    IncrementNbEvolutions: Symbol[
        Optional[list[int]],
        None,
    ]

    GetNbEvolutions: Symbol[
        Optional[list[int]],
        None,
    ]

    IncrementNbSteals: Symbol[
        Optional[list[int]],
        None,
    ]

    IncrementNbEggsHatched: Symbol[
        Optional[list[int]],
        None,
    ]

    GetNbEggsHatched: Symbol[
        Optional[list[int]],
        None,
    ]

    GetNbPokemonJoined: Symbol[
        Optional[list[int]],
        None,
    ]

    GetNbMovesLearned: Symbol[
        Optional[list[int]],
        None,
    ]

    SetVictoriesOnOneFloor: Symbol[
        Optional[list[int]],
        None,
    ]

    GetVictoriesOnOneFloor: Symbol[
        Optional[list[int]],
        None,
    ]

    SetPokemonJoined: Symbol[
        Optional[list[int]],
        None,
    ]

    SetPokemonBattled: Symbol[
        Optional[list[int]],
        None,
    ]

    GetNbPokemonBattled: Symbol[
        Optional[list[int]],
        None,
    ]

    IncrementNbBigTreasureWins: Symbol[
        Optional[list[int]],
        None,
    ]

    SetNbBigTreasureWins: Symbol[
        Optional[list[int]],
        None,
    ]

    GetNbBigTreasureWins: Symbol[
        Optional[list[int]],
        None,
    ]

    SetNbRecycled: Symbol[
        Optional[list[int]],
        None,
    ]

    GetNbRecycled: Symbol[
        Optional[list[int]],
        None,
    ]

    IncrementNbSkyGiftsSent: Symbol[
        Optional[list[int]],
        None,
    ]

    SetNbSkyGiftsSent: Symbol[
        Optional[list[int]],
        None,
    ]

    GetNbSkyGiftsSent: Symbol[
        Optional[list[int]],
        None,
    ]

    ComputeSpecialCounters: Symbol[
        Optional[list[int]],
        None,
    ]

    RecruitSpecialPokemonLog: Symbol[
        Optional[list[int]],
        None,
    ]

    IncrementNbFainted: Symbol[
        Optional[list[int]],
        None,
    ]

    GetNbFainted: Symbol[
        Optional[list[int]],
        None,
    ]

    SetItemAcquired: Symbol[
        Optional[list[int]],
        None,
    ]

    GetNbItemAcquired: Symbol[
        Optional[list[int]],
        None,
    ]

    SetChallengeLetterCleared: Symbol[
        Optional[list[int]],
        None,
    ]

    GetSentryDutyGamePoints: Symbol[
        Optional[list[int]],
        None,
    ]

    SetSentryDutyGamePoints: Symbol[
        Optional[list[int]],
        None,
    ]

    CopyLogToStream: Symbol[
        Optional[list[int]],
        None,
    ]

    CopyLogFromStream: Symbol[
        Optional[list[int]],
        None,
    ]

    GetAbilityString: Symbol[
        Optional[list[int]],
        None,
    ]

    GetAbilityDescStringId: Symbol[
        Optional[list[int]],
        None,
    ]

    GetTypeStringId: Symbol[
        Optional[list[int]],
        None,
    ]

    GetConversion2ConvertToType: Symbol[
        Optional[list[int]],
        None,
    ]

    InitBitstreamForWrite: Symbol[
        Optional[list[int]],
        None,
    ]

    InitBitstreamForRead: Symbol[
        Optional[list[int]],
        None,
    ]

    BitstreamDebug: Symbol[
        Optional[list[int]],
        None,
    ]

    CopyBitsToStream: Symbol[
        Optional[list[int]],
        None,
    ]

    CopyBitsFromStream: Symbol[
        Optional[list[int]],
        None,
    ]

    StoreDefaultTeamData: Symbol[
        Optional[list[int]],
        None,
    ]

    GetMainTeamNameWithCheck: Symbol[
        Optional[list[int]],
        None,
    ]

    GetMainTeamName: Symbol[
        Optional[list[int]],
        None,
    ]

    SetMainTeamName: Symbol[
        Optional[list[int]],
        None,
    ]

    GetRankupPoints: Symbol[
        Optional[list[int]],
        None,
    ]

    GetRank: Symbol[
        Optional[list[int]],
        None,
    ]

    GetRankStorageSize: Symbol[
        Optional[list[int]],
        None,
    ]

    ResetPlayTimer: Symbol[
        Optional[list[int]],
        None,
    ]

    PlayTimerTick: Symbol[
        Optional[list[int]],
        None,
    ]

    GetPlayTimeSeconds: Symbol[
        Optional[list[int]],
        None,
    ]

    SubFixedPoint: Symbol[
        Optional[list[int]],
        None,
    ]

    BinToDecFixedPoint: Symbol[
        Optional[list[int]],
        None,
    ]

    CeilFixedPoint: Symbol[
        Optional[list[int]],
        None,
    ]

    DungeonGoesUp: Symbol[
        Optional[list[int]],
        None,
    ]

    GetTurnLimit: Symbol[
        Optional[list[int]],
        None,
    ]

    DoesNotSaveWhenEntering: Symbol[
        Optional[list[int]],
        None,
    ]

    TreasureBoxDropsEnabled: Symbol[
        Optional[list[int]],
        None,
    ]

    IsLevelResetDungeon: Symbol[
        Optional[list[int]],
        None,
    ]

    GetMaxItemsAllowed: Symbol[
        Optional[list[int]],
        None,
    ]

    IsMoneyAllowed: Symbol[
        Optional[list[int]],
        None,
    ]

    GetMaxRescueAttempts: Symbol[
        Optional[list[int]],
        None,
    ]

    IsRecruitingAllowed: Symbol[
        Optional[list[int]],
        None,
    ]

    GetLeaderChangeFlag: Symbol[
        Optional[list[int]],
        None,
    ]

    GetRandomMovementChance: Symbol[
        Optional[list[int]],
        None,
    ]

    CanEnemyEvolve: Symbol[
        Optional[list[int]],
        None,
    ]

    GetMaxMembersAllowed: Symbol[
        Optional[list[int]],
        None,
    ]

    IsIqEnabled: Symbol[
        Optional[list[int]],
        None,
    ]

    IsTrapInvisibleWhenAttacking: Symbol[
        Optional[list[int]],
        None,
    ]

    JoinedAtRangeCheck: Symbol[
        Optional[list[int]],
        None,
    ]

    IsDojoDungeon: Symbol[
        Optional[list[int]],
        None,
    ]

    IsFutureDungeon: Symbol[
        Optional[list[int]],
        None,
    ]

    IsSpecialEpisodeDungeon: Symbol[
        Optional[list[int]],
        None,
    ]

    RetrieveFromItemList1: Symbol[
        Optional[list[int]],
        None,
    ]

    IsForbiddenFloor: Symbol[
        Optional[list[int]],
        None,
    ]

    Copy16BitsToStream: Symbol[
        Optional[list[int]],
        None,
    ]

    Copy16BitsFromStream: Symbol[
        Optional[list[int]],
        None,
    ]

    RetrieveFromItemList2: Symbol[
        Optional[list[int]],
        None,
    ]

    IsInvalidForMission: Symbol[
        Optional[list[int]],
        None,
    ]

    IsExpEnabledInDungeon: Symbol[
        Optional[list[int]],
        None,
    ]

    IsSkyExclusiveDungeon: Symbol[
        Optional[list[int]],
        None,
    ]

    JoinedAtRangeCheck2: Symbol[
        Optional[list[int]],
        None,
    ]

    GetBagCapacity: Symbol[
        Optional[list[int]],
        None,
    ]

    GetBagCapacitySpecialEpisode: Symbol[
        Optional[list[int]],
        None,
    ]

    GetRankUpEntry: Symbol[
        Optional[list[int]],
        None,
    ]

    GetBgRegionArea: Symbol[
        Optional[list[int]],
        None,
    ]

    LoadMonsterMd: Symbol[
        Optional[list[int]],
        None,
    ]

    GetNameRaw: Symbol[
        Optional[list[int]],
        None,
    ]

    GetName: Symbol[
        Optional[list[int]],
        None,
    ]

    GetNameWithGender: Symbol[
        Optional[list[int]],
        None,
    ]

    GetSpeciesString: Symbol[
        Optional[list[int]],
        None,
    ]

    GetNameString: Symbol[
        Optional[list[int]],
        None,
    ]

    GetSpriteIndex: Symbol[
        Optional[list[int]],
        None,
    ]

    GetDexNumber: Symbol[
        Optional[list[int]],
        None,
    ]

    GetCategoryString: Symbol[
        Optional[list[int]],
        None,
    ]

    GetMonsterGender: Symbol[
        Optional[list[int]],
        None,
    ]

    GetBodySize: Symbol[
        Optional[list[int]],
        None,
    ]

    GetSpriteSize: Symbol[
        Optional[list[int]],
        None,
    ]

    GetSpriteFileSize: Symbol[
        Optional[list[int]],
        None,
    ]

    GetShadowSize: Symbol[
        Optional[list[int]],
        None,
    ]

    GetSpeedStatus: Symbol[
        Optional[list[int]],
        None,
    ]

    GetMobilityType: Symbol[
        Optional[list[int]],
        None,
    ]

    GetRegenSpeed: Symbol[
        Optional[list[int]],
        None,
    ]

    GetCanMoveFlag: Symbol[
        Optional[list[int]],
        None,
    ]

    GetChanceAsleep: Symbol[
        Optional[list[int]],
        None,
    ]

    GetWeightMultiplier: Symbol[
        Optional[list[int]],
        None,
    ]

    GetSize: Symbol[
        Optional[list[int]],
        None,
    ]

    GetBaseHp: Symbol[
        Optional[list[int]],
        None,
    ]

    CanThrowItems: Symbol[
        Optional[list[int]],
        None,
    ]

    CanEvolve: Symbol[
        Optional[list[int]],
        None,
    ]

    GetMonsterPreEvolution: Symbol[
        Optional[list[int]],
        None,
    ]

    GetBaseOffensiveStat: Symbol[
        Optional[list[int]],
        None,
    ]

    GetBaseDefensiveStat: Symbol[
        Optional[list[int]],
        None,
    ]

    GetType: Symbol[
        Optional[list[int]],
        None,
    ]

    GetAbility: Symbol[
        Optional[list[int]],
        None,
    ]

    GetRecruitRate2: Symbol[
        Optional[list[int]],
        None,
    ]

    GetRecruitRate1: Symbol[
        Optional[list[int]],
        None,
    ]

    GetExp: Symbol[
        Optional[list[int]],
        None,
    ]

    GetEvoParameters: Symbol[
        Optional[list[int]],
        None,
    ]

    GetTreasureBoxChances: Symbol[
        Optional[list[int]],
        None,
    ]

    GetIqGroup: Symbol[
        Optional[list[int]],
        None,
    ]

    GetSpawnThreshold: Symbol[
        Optional[list[int]],
        None,
    ]

    NeedsItemToSpawn: Symbol[
        Optional[list[int]],
        None,
    ]

    GetExclusiveItem: Symbol[
        Optional[list[int]],
        None,
    ]

    GetFamilyIndex: Symbol[
        Optional[list[int]],
        None,
    ]

    LoadM2nAndN2m: Symbol[
        Optional[list[int]],
        None,
    ]

    GuestMonsterToGroundMonster: Symbol[
        Optional[list[int]],
        None,
    ]

    SetBaseStatsMovesGroundMonster: Symbol[
        Optional[list[int]],
        None,
    ]

    StrcmpMonsterName: Symbol[
        Optional[list[int]],
        None,
    ]

    GetLvlUpEntry: Symbol[
        Optional[list[int]],
        None,
    ]

    GetEncodedHalfword: Symbol[
        Optional[list[int]],
        None,
    ]

    GetEvoFamily: Symbol[
        Optional[list[int]],
        None,
    ]

    GetEvolutions: Symbol[
        Optional[list[int]],
        None,
    ]

    ShuffleHiddenPower: Symbol[
        Optional[list[int]],
        None,
    ]

    GetBaseForm: Symbol[
        Optional[list[int]],
        None,
    ]

    GetBaseFormBurmyWormadamShellosGastrodonCherrim: Symbol[
        Optional[list[int]],
        None,
    ]

    GetBaseFormCastformCherrimDeoxys: Symbol[
        Optional[list[int]],
        None,
    ]

    GetAllBaseForms: Symbol[
        Optional[list[int]],
        None,
    ]

    GetDexNumberVeneer: Symbol[
        Optional[list[int]],
        None,
    ]

    GetMonsterIdFromSpawnEntry: Symbol[
        Optional[list[int]],
        None,
    ]

    SetMonsterId: Symbol[
        Optional[list[int]],
        None,
    ]

    SetMonsterLevelAndId: Symbol[
        Optional[list[int]],
        None,
    ]

    GetMonsterLevelFromSpawnEntry: Symbol[
        Optional[list[int]],
        None,
    ]

    ApplyLevelUpBoostsToGroundMonster: Symbol[
        Optional[list[int]],
        None,
    ]

    GetMonsterGenderVeneer: Symbol[
        Optional[list[int]],
        None,
    ]

    IsMonsterValid: Symbol[
        Optional[list[int]],
        None,
    ]

    IsUnown: Symbol[
        Optional[list[int]],
        None,
    ]

    IsShaymin: Symbol[
        Optional[list[int]],
        None,
    ]

    IsCastform: Symbol[
        Optional[list[int]],
        None,
    ]

    IsCherrim: Symbol[
        Optional[list[int]],
        None,
    ]

    IsDeoxys: Symbol[
        Optional[list[int]],
        None,
    ]

    GetSecondFormIfValid: Symbol[
        Optional[list[int]],
        None,
    ]

    FemaleToMaleForm: Symbol[
        Optional[list[int]],
        None,
    ]

    GetBaseFormCastformDeoxysCherrim: Symbol[
        Optional[list[int]],
        None,
    ]

    BaseFormsEqual: Symbol[
        Optional[list[int]],
        None,
    ]

    DexNumbersEqual: Symbol[
        Optional[list[int]],
        None,
    ]

    GendersEqual: Symbol[
        Optional[list[int]],
        None,
    ]

    GendersEqualNotGenderless: Symbol[
        Optional[list[int]],
        None,
    ]

    GendersNotEqualNotGenderless: Symbol[
        Optional[list[int]],
        None,
    ]

    IsMonsterOnTeam: Symbol[
        Optional[list[int]],
        None,
    ]

    GetNbRecruited: Symbol[
        Optional[list[int]],
        None,
    ]

    IsValidTeamMember: Symbol[
        Optional[list[int]],
        None,
    ]

    IsMainCharacter: Symbol[
        Optional[list[int]],
        None,
    ]

    GetTeamMember: Symbol[
        Optional[list[int]],
        None,
    ]

    GetHeroMemberIdx: Symbol[
        Optional[list[int]],
        None,
    ]

    GetPartnerMemberIdx: Symbol[
        Optional[list[int]],
        None,
    ]

    GetMainCharacter1MemberIdx: Symbol[
        Optional[list[int]],
        None,
    ]

    GetMainCharacter2MemberIdx: Symbol[
        Optional[list[int]],
        None,
    ]

    GetMainCharacter3MemberIdx: Symbol[
        Optional[list[int]],
        None,
    ]

    GetHero: Symbol[
        Optional[list[int]],
        None,
    ]

    GetPartner: Symbol[
        Optional[list[int]],
        None,
    ]

    GetMainCharacter1: Symbol[
        Optional[list[int]],
        None,
    ]

    GetMainCharacter2: Symbol[
        Optional[list[int]],
        None,
    ]

    GetMainCharacter3: Symbol[
        Optional[list[int]],
        None,
    ]

    GetFirstMatchingMemberIdx: Symbol[
        Optional[list[int]],
        None,
    ]

    GetFirstEmptyMemberIdx: Symbol[
        Optional[list[int]],
        None,
    ]

    IsMonsterNotNicknamed: Symbol[
        Optional[list[int]],
        None,
    ]

    RemoveActiveMembersFromAllTeams: Symbol[
        Optional[list[int]],
        None,
    ]

    RemoveActiveMembersFromSpecialEpisodeTeam: Symbol[
        Optional[list[int]],
        None,
    ]

    RemoveActiveMembersFromRescueTeam: Symbol[
        Optional[list[int]],
        None,
    ]

    CheckTeamMemberIdx: Symbol[
        Optional[list[int]],
        None,
    ]

    IsMonsterIdInNormalRange: Symbol[
        Optional[list[int]],
        None,
    ]

    SetActiveTeam: Symbol[
        Optional[list[int]],
        None,
    ]

    GetActiveTeamMember: Symbol[
        Optional[list[int]],
        None,
    ]

    GetActiveRosterIndex: Symbol[
        Optional[list[int]],
        None,
    ]

    TryAddMonsterToActiveTeam: Symbol[
        Optional[list[int]],
        None,
    ]

    RemoveActiveMembersFromMainTeam: Symbol[
        Optional[list[int]],
        None,
    ]

    SetTeamSetupHeroAndPartnerOnly: Symbol[
        Optional[list[int]],
        None,
    ]

    SetTeamSetupHeroOnly: Symbol[
        Optional[list[int]],
        None,
    ]

    GetPartyMembers: Symbol[
        Optional[list[int]],
        None,
    ]

    RefillTeam: Symbol[
        Optional[list[int]],
        None,
    ]

    ClearItem: Symbol[
        Optional[list[int]],
        None,
    ]

    ChangeGiratinaFormIfSkyDungeon: Symbol[
        Optional[list[int]],
        None,
    ]

    RevertGiratinaAndShaymin: Symbol[
        Optional[list[int]],
        None,
    ]

    GetIqSkillStringId: Symbol[
        Optional[list[int]],
        None,
    ]

    DoesTacticFollowLeader: Symbol[
        Optional[list[int]],
        None,
    ]

    GetUnlockedTactics: Symbol[
        Optional[list[int]],
        None,
    ]

    GetUnlockedTacticFlags: Symbol[
        Optional[list[int]],
        None,
    ]

    CanLearnIqSkill: Symbol[
        Optional[list[int]],
        None,
    ]

    GetLearnableIqSkills: Symbol[
        Optional[list[int]],
        None,
    ]

    DisableIqSkill: Symbol[
        Optional[list[int]],
        None,
    ]

    EnableIqSkill: Symbol[
        Optional[list[int]],
        None,
    ]

    GetSpeciesIqSkill: Symbol[
        Optional[list[int]],
        None,
    ]

    DisableAllIqSkills: Symbol[
        Optional[list[int]],
        None,
    ]

    EnableAllLearnableIqSkills: Symbol[
        Optional[list[int]],
        None,
    ]

    IqSkillFlagTest: Symbol[
        Optional[list[int]],
        None,
    ]

    GetNextIqSkill: Symbol[
        Optional[list[int]],
        None,
    ]

    ExplorerMazeMonsterExists: Symbol[
        Optional[list[int]],
        None,
    ]

    GetExplorerMazeTeamName: Symbol[
        Optional[list[int]],
        None,
    ]

    GetExplorerMazeMonster: Symbol[
        Optional[list[int]],
        None,
    ]

    GetMonsterInfoForSave: Symbol[
        Optional[list[int]],
        None,
    ]

    ReadMonsterInfoFromSave: Symbol[
        Optional[list[int]],
        None,
    ]

    CopyMonsterToStream: Symbol[
        Optional[list[int]],
        None,
    ]

    CopyMonsterFromStream: Symbol[
        Optional[list[int]],
        None,
    ]

    GetEvolutionPossibilities: Symbol[
        Optional[list[int]],
        None,
    ]

    GetMonsterEvoStatus: Symbol[
        Optional[list[int]],
        None,
    ]

    HandleShedinjaEvolution: Symbol[
        Optional[list[int]],
        None,
    ]

    CopyTacticString: Symbol[
        Optional[list[int]],
        None,
    ]

    GetStatBoostsForMonsterSummary: Symbol[
        Optional[list[int]],
        None,
    ]

    CreateMonsterSummaryFromTeamMember: Symbol[
        Optional[list[int]],
        None,
    ]

    GetSosMailCount: Symbol[
        Optional[list[int]],
        None,
    ]

    IsMissionSuspendedAndValid: Symbol[
        Optional[list[int]],
        None,
    ]

    AreMissionsEquivalent: Symbol[
        Optional[list[int]],
        None,
    ]

    IsMissionValid: Symbol[
        Optional[list[int]],
        None,
    ]

    GenerateMission: Symbol[
        Optional[list[int]],
        None,
    ]

    IsMissionTypeSpecialEpisode: Symbol[
        Optional[list[int]],
        None,
    ]

    GenerateDailyMissions: Symbol[
        Optional[list[int]],
        None,
    ]

    AlreadyHaveMission: Symbol[
        Optional[list[int]],
        None,
    ]

    CountJobListMissions: Symbol[
        Optional[list[int]],
        None,
    ]

    DungeonRequestsDone: Symbol[
        Optional[list[int]],
        None,
    ]

    DungeonRequestsDoneWrapper: Symbol[
        Optional[list[int]],
        None,
    ]

    AnyDungeonRequestsDone: Symbol[
        Optional[list[int]],
        None,
    ]

    AddMissionToJobList: Symbol[
        Optional[list[int]],
        None,
    ]

    GetAcceptedMission: Symbol[
        Optional[list[int]],
        None,
    ]

    GetMissionByTypeAndDungeon: Symbol[
        Optional[list[int]],
        None,
    ]

    CheckAcceptedMissionByTypeAndDungeon: Symbol[
        Optional[list[int]],
        None,
    ]

    GetAllPossibleMonsters: Symbol[
        Optional[list[int]],
        None,
    ]

    GenerateAllPossibleMonstersList: Symbol[
        Optional[list[int]],
        None,
    ]

    DeleteAllPossibleMonstersList: Symbol[
        Optional[list[int]],
        None,
    ]

    GenerateAllPossibleDungeonsList: Symbol[
        Optional[list[int]],
        None,
    ]

    DeleteAllPossibleDungeonsList: Symbol[
        Optional[list[int]],
        None,
    ]

    GenerateAllPossibleDeliverList: Symbol[
        Optional[list[int]],
        None,
    ]

    DeleteAllPossibleDeliverList: Symbol[
        Optional[list[int]],
        None,
    ]

    ClearMissionData: Symbol[
        Optional[list[int]],
        None,
    ]

    GenerateMissionDetailsStruct: Symbol[
        Optional[list[int]],
        None,
    ]

    ValidateNormalChallengeMission: Symbol[
        Optional[list[int]],
        None,
    ]

    ValidateLegendaryChallengeMission: Symbol[
        Optional[list[int]],
        None,
    ]

    AppendMissionTitle: Symbol[
        Optional[list[int]],
        None,
    ]

    AppendMissionSummary: Symbol[
        Optional[list[int]],
        None,
    ]

    IsMonsterMissionAllowed: Symbol[
        Optional[list[int]],
        None,
    ]

    CanMonsterBeUsedForMissionWrapper: Symbol[
        Optional[list[int]],
        None,
    ]

    CanMonsterBeUsedForMission: Symbol[
        Optional[list[int]],
        None,
    ]

    IsMonsterMissionAllowedStory: Symbol[
        Optional[list[int]],
        None,
    ]

    IsMonsterIllegalForMissions: Symbol[
        Optional[list[int]],
        None,
    ]

    CanDungeonBeUsedForMission: Symbol[
        Optional[list[int]],
        None,
    ]

    CanSendItem: Symbol[
        Optional[list[int]],
        None,
    ]

    IsAvailableItem: Symbol[
        Optional[list[int]],
        None,
    ]

    GetAvailableItemDeliveryList: Symbol[
        Optional[list[int]],
        None,
    ]

    GetScriptEntityMonsterId: Symbol[
        Optional[list[int]],
        None,
    ]

    GetScriptEntityMatchingStorageId: Symbol[
        Optional[list[int]],
        None,
    ]

    SetActorTalkMainAndActorTalkSub: Symbol[
        Optional[list[int]],
        None,
    ]

    SetActorTalkMain: Symbol[
        Optional[list[int]],
        None,
    ]

    SetActorTalkSub: Symbol[
        Optional[list[int]],
        None,
    ]

    RandomizeDemoActors: Symbol[
        Optional[list[int]],
        None,
    ]

    ItemAtTableIdx: Symbol[
        Optional[list[int]],
        None,
    ]

    MainLoop: Symbol[
        Optional[list[int]],
        None,
    ]

    CreateJobSummary: Symbol[
        Optional[list[int]],
        None,
    ]

    DungeonSwapIdToIdx: Symbol[
        Optional[list[int]],
        None,
    ]

    DungeonSwapIdxToId: Symbol[
        Optional[list[int]],
        None,
    ]

    GetDungeonModeSpecial: Symbol[
        Optional[list[int]],
        None,
    ]


class Arm9DataProtocol(Protocol):

    SECURE: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    START_MODULE_PARAMS: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    DEFAULT_MEMORY_ARENA_SIZE: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    LOG_MAX_ARG: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    DAMAGE_SOURCE_CODE_ORB_ITEM: Symbol[
        Optional[list[int]],
        None,
    ]

    DAMAGE_SOURCE_CODE_NON_ORB_ITEM: Symbol[
        Optional[list[int]],
        None,
    ]

    AURA_BOW_ID_LAST: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    NUMBER_OF_ITEMS: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    MAX_MONEY_CARRIED: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    MAX_MONEY_STORED: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    WINDOW_LIST_PTR: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    SCRIPT_VARS_VALUES_PTR: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    MAX_PLAY_TIME: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    MONSTER_ID_LIMIT: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    MAX_RECRUITABLE_TEAM_MEMBERS: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    SINE_VALUE_TABLE: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    NATURAL_LOG_VALUE_TABLE: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    CART_REMOVED_IMG_DATA: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    STRING_DEBUG_EMPTY: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    STRING_DEBUG_FORMAT_LINE_FILE: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    STRING_DEBUG_NO_PROG_POS: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    STRING_DEBUG_SPACED_PRINT: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    STRING_DEBUG_FATAL: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    STRING_DEBUG_NEWLINE: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    STRING_DEBUG_LOG_NULL: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    STRING_DEBUG_STRING_NEWLINE: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    STRING_EFFECT_EFFECT_BIN: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    STRING_MONSTER_MONSTER_BIN: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    STRING_BALANCE_M_LEVEL_BIN: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    STRING_DUNGEON_DUNGEON_BIN: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    STRING_MONSTER_M_ATTACK_BIN: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    STRING_MONSTER_M_GROUND_BIN: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    STRING_FILE_DIRECTORY_INIT: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    AVAILABLE_ITEMS_IN_GROUP_TABLE: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    ST_I2N_I_BIN_FILE_NAME: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    ST_I2N_E_BIN_FILE_NAME: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    ST_I2N_S_BIN_FILE_NAME: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    ST_I2N_G_BIN_FILE_NAME: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    ST_I2N_F_BIN_FILE_NAME: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    BABY_EXCLUSIVE_ITEM_PAIRS: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    ITEM_P_BIN_FILE_PATH: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    ITEM_S_P_BIN_FILE_PATH: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    ITEM_ST_I2N_BIN_FORMAT: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    ITEM_NAME_FORMAT_YELLOW: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    ITEM_NAME_FORMAT_INDIGO: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    ITEM_NAME_FORMAT_PLAIN: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    ITEM_NAME_FORMAT_CREAM: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    KECLEON_SHOP_ITEM_TABLE_LISTS_1: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    KECLEON_SHOP_ITEM_TABLE_LISTS_2: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    EXCLUSIVE_ITEM_STAT_BOOST_DATA: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    EXCLUSIVE_ITEM_DEFENSE_BOOSTS: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    EXCLUSIVE_ITEM_SPECIAL_ATTACK_BOOSTS: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    EXCLUSIVE_ITEM_SPECIAL_DEFENSE_BOOSTS: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    EXCLUSIVE_ITEM_EFFECT_DATA: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    EXCLUSIVE_ITEM_STAT_BOOST_DATA_INDEXES: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    RECYCLE_SHOP_ITEM_LIST: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    TYPE_SPECIFIC_EXCLUSIVE_ITEMS: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    RECOIL_MOVE_LIST: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    PUNCH_MOVE_LIST: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    MOVE_POWER_STARS_TABLE: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    MOVE_ACCURACY_STARS_TABLE: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    PARENT_MENU_DEFAULT_WINDOW_PARAMS: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    SIMPLE_MENU_DEFAULT_WINDOW_PARAMS: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    ADVANCED_MENU_DEFAULT_WINDOW_PARAMS: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    COLLECTION_MENU_DEFAULT_WINDOW_PARAMS: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    OPTIONS_MENU_DEFAULT_WINDOW_PARAMS: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    DEBUG_MENU_DEFAULT_WINDOW_PARAMS: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    SCROLL_BOX_DEFAULT_WINDOW_PARAMS: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    DIALOGUE_BOX_DEFAULT_WINDOW_PARAMS: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    PORTRAIT_BOX_DEFAULT_WINDOW_PARAMS: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    TEXT_BOX_DEFAULT_WINDOW_PARAMS: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    AREA_NAME_BOX_DEFAULT_WINDOW_PARAMS: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    CONTROLS_CHART_DEFAULT_WINDOW_PARAMS: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    ALERT_BOX_DEFAULT_WINDOW_PARAMS: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    ADVANCED_TEXT_BOX_DEFAULT_WINDOW_PARAMS: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    TEAM_SELECTION_MENU_DEFAULT_WINDOW_PARAMS: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    NULL_OVERLAY_LOAD_ENTRY: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    PARTNER_TALK_KIND_TABLE: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    EVENT_FLAG_PROG_POS_INFO_CALC_SCRIPT_VARIABLES: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    EVENT_FLAG_PROG_POS_INFO_COMPARE_SCRIPT_VARIABLES: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    EVENT_FLAG_FILE_NAME: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    SCRIPT_VARS_LOCALS: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    EVENT_FLAG_SIZE_DEBUG_MSG: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    EVENT_FLAG_CALC_SCRIPT_VARIABLES_ERROR: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    EVENT_FLAG_COMPARE_SCRIPT_VARIABLES_ERROR: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    EVENT_FLAG_GAME_MODE_DEBUG_MSG: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    EVENT_FLAG_BACKUP_DEBUG_MSG: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    SUM_MSG: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    SUB30_PROJECTP_MSG: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    NOTE_MODIFY_FLAG_MSG: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    SCRIPT_VARS: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    SCENARIO_CALC_DEBUG_MSG: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    SCENARIO_FLAG_RESUME_DEBUG_MSG: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    SCENARIO_FLAG_BACKUP_DEBUG_MSG: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    PORTRAIT_LAYOUTS: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    KAOMADO_FILEPATH: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    WONDER_MAIL_BITS_MAP: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    WONDER_MAIL_BITS_SWAP: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    ARM9_UNKNOWN_TABLE__NA_209E12C: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    ARM9_UNKNOWN_TABLE__NA_209E164: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    ARM9_UNKNOWN_TABLE__NA_209E280: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    WONDER_MAIL_ENCRYPTION_TABLE: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    DUNGEON_DATA_LIST: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    ADVENTURE_LOG_ENCOUNTERS_MONSTER_IDS: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    ARM9_UNKNOWN_DATA__NA_209E6BC: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    TACTIC_NAME_STRING_IDS: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    STATUS_NAME_STRING_IDS: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    DUNGEON_RETURN_STATUS_TABLE: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    STATUSES_FULL_DESCRIPTION_STRING_IDS: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    ARM9_UNKNOWN_DATA__NA_209EAAC: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    MISSION_FLOOR_RANKS_AND_ITEM_LISTS_1: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    MISSION_FLOORS_FORBIDDEN: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    MISSION_FLOOR_RANKS_AND_ITEM_LISTS_2: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    MISSION_FLOOR_RANKS_PTRS: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    DUNGEON_RESTRICTIONS: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    SPECIAL_BAND_STAT_BOOST: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    UNKNOWN_PP_BOOST_AMOUNT: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    MUNCH_BELT_STAT_BOOST: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    GUMMI_STAT_BOOST: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    MIN_IQ_EXCLUSIVE_MOVE_USER: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    WONDER_GUMMI_IQ_GAIN: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    AURA_BOW_STAT_BOOST: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    MULTITALENT_PP_BOOST_AMOUNT: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    MIN_IQ_ITEM_MASTER: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    DEF_SCARF_STAT_BOOST: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    POWER_BAND_STAT_BOOST: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    WONDER_GUMMI_STAT_BOOST: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    ZINC_BAND_STAT_BOOST: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    EGG_HP_BONUS: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    EVOLUTION_HP_BONUS: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    EXCLUSIVE_ITEM_PP_BOOST_AMOUNT: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    DAMAGE_FORMULA_FLV_SHIFT: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    EVOLUTION_PHYSICAL_STAT_BONUSES: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    DAMAGE_FORMULA_CONSTANT_SHIFT: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    DAMAGE_FORMULA_FLV_DEFICIT_DIVISOR: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    EGG_STAT_BONUSES: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    EVOLUTION_SPECIAL_STAT_BONUSES: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    DAMAGE_FORMULA_NON_TEAM_MEMBER_MODIFIER: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    DAMAGE_FORMULA_LN_PREFACTOR: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    DAMAGE_FORMULA_DEF_PREFACTOR: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    DAMAGE_FORMULA_AT_PREFACTOR: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    DAMAGE_FORMULA_LN_ARG_PREFACTOR: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    TACTICS_FOLLOW_LEADER: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    FORBIDDEN_FORGOT_MOVE_LIST: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    CONVERSION2_TYPE_TABLE: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    TACTICS_UNLOCK_LEVEL_TABLE: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    CLIENT_LEVEL_TABLE: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    OUTLAW_LEVEL_TABLE: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    OUTLAW_MINION_LEVEL_TABLE: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    HIDDEN_POWER_BASE_POWER_TABLE: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    VERSION_EXCLUSIVE_MONSTERS: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    IQ_SKILL_RESTRICTIONS: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    SECONDARY_TERRAIN_TYPES: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    SENTRY_DUTY_MONSTER_IDS: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    IQ_SKILLS: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    IQ_GROUP_SKILLS: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    MONEY_QUANTITY_TABLE: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    ARM9_UNKNOWN_TABLE__NA_20A20B0: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    IQ_GUMMI_GAIN_TABLE: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    GUMMI_BELLY_RESTORE_TABLE: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    BAG_CAPACITY_TABLE_SPECIAL_EPISODES: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    BAG_CAPACITY_TABLE: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    SPECIAL_EPISODE_MAIN_CHARACTERS: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    GUEST_MONSTER_DATA: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    GUEST_MONSTER_BANETTE: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    GUEST_MONSTER_SKORUPI: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    GUEST_MONSTER_BIDOOF: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    GUEST_MONSTER_SNOVER: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    GUEST_MONSTER_BIDOOF_2: Symbol[
        Optional[list[int]],
        None,
    ]

    GUEST_MONSTER_GROVYLE: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    GUEST_MONSTER_LOUDRED: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    GUEST_MONSTER_DUSKNOIR: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    GUEST_MONSTER_GROVYLE_2: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    GUEST_MONSTER_CHATOT: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    GUEST_MONSTER_SHINY_CELEBI: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    GUEST_MONSTER_GROVYLE_3: Symbol[
        Optional[list[int]],
        None,
    ]

    GUEST_MONSTER_GROVYLE_4: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    GUEST_MONSTER_CRESSELIA: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    GUEST_MONSTER_BIDOOF_3: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    GUEST_MONSTER_BIDOOF_4: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    GUEST_MONSTER_SHAYMIN_LAND: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    GUEST_MONSTER_SNOVER_2: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    RANK_UP_TABLE: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    DS_DOWNLOAD_TEAMS: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    ARM9_UNKNOWN_PTR__NA_20A2C84: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    UNOWN_SPECIES_ADDITIONAL_CHARS: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    MONSTER_SPRITE_DATA: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    REMOTE_STRINGS: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    RANK_STRINGS_1: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    MISSION_MENU_STRING_IDS_1: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    RANK_STRINGS_2: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    MISSION_MENU_STRING_IDS_2: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    RANK_STRINGS_3: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    MISSION_DUNGEON_UNLOCK_TABLE: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    NO_SEND_ITEM_TABLE: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    CAFE_MISSION_REWARD_TYPE_WEIGHTS: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    OUTLAW_MISSION_REWARD_TYPE_WEIGHTS: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    DEFAULT_MISSION_REWARD_TYPE_WEIGHTS: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    MISSION_VALIDATION_FUNCTION_LIST: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    MISSION_BANNED_STORY_MONSTERS: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    ITEM_DELIVERY_TABLE: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    MISSION_RANK_POINTS: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    MISSION_BANNED_MONSTERS: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    MISSION_STRING_IDS: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    LEVEL_LIST: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    EVENTS: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    ARM9_UNKNOWN_TABLE__NA_20A68BC: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    DEMO_TEAMS: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    ACTOR_LIST: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    ENTITIES: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    JOB_WINDOW_PARAMS_1: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    JOB_MENU_ITEMS_1: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    JOB_MENU_ITEMS_2: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    JOB_MENU_ITEMS_3: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    JOB_MENU_ITEMS_4: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    JOB_MENU_ITEMS_5: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    JOB_MENU_ITEMS_6: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    JOB_MENU_ITEMS_7: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    JOB_MENU_ITEMS_8: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    JOB_MENU_ITEMS_9: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    JOB_MENU_ITEMS_10: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    JOB_MENU_ITEMS_11: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    JOB_MENU_ITEMS_12: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    JOB_MENU_ITEMS_13: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    JOB_WINDOW_PARAMS_2: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    DUNGEON_SWAP_ID_TABLE: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    MAP_MARKER_PLACEMENTS: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    LFO_OUTPUT_VOICE_UPDATE_FLAGS: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    TRIG_TABLE: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    FX_ATAN_IDX_TABLE: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    TEX_PLTT_START_ADDR_TABLE: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    TEX_START_ADDR_TABLE: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    ARM9_UNKNOWN_TABLE__NA_20AE924: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    MEMORY_ALLOCATION_ARENA_GETTERS: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    PRNG_SEQUENCE_NUM: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    LOADED_OVERLAY_GROUP_0: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    LOADED_OVERLAY_GROUP_1: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    LOADED_OVERLAY_GROUP_2: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    DEBUG_IS_INITIALIZED: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    PACK_FILES_OPENED: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    PACK_FILE_PATHS_TABLE: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    GAME_STATE_VALUES: Symbol[
        Optional[list[int]],
        None,
    ]

    BAG_ITEMS_PTR_MIRROR: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    ITEM_DATA_TABLE_PTRS: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    ITEM_LANG_FILE_ARRAY: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    DUNGEON_MOVE_TABLES: Symbol[
        Optional[list[int]],
        None,
    ]

    MOVE_DATA_TABLE_PTR: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    WAN_TABLE: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    RENDER_3D: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    RENDER_3D_FUNCTIONS_64: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    LANGUAGE_INFO_DATA: Symbol[
        Optional[list[int]],
        None,
    ]

    TBL_TALK_GROUP_STRING_ID_START: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    MENU_CONTROL_PTR: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    KEYBOARD_STRING_IDS: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    NOTIFY_NOTE: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    DEFAULT_HERO_ID: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    DEFAULT_PARTNER_ID: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    GAME_MODE: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    GLOBAL_PROGRESS_PTR: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    ADVENTURE_LOG_PTR: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    ITEM_TABLES_PTRS_1: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    MONSTER_DATA_TABLE_PTR: Symbol[
        Optional[list[int]],
        None,
    ]

    UNOWN_SPECIES_ADDITIONAL_CHAR_PTR_TABLE: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    TEAM_MEMBER_TABLE_PTR: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    MISSION_DELIVER_LIST_PTR: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    MISSION_DELIVER_COUNT: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    MISSION_DUNGEON_LIST_PTR: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    MISSION_DUNGEON_COUNT: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    MISSION_MONSTER_LIST_PTR: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    MISSION_MONSTER_COUNT: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    MISSION_LIST_PTR: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    REMOTE_STRING_PTR_TABLE: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    RANK_STRING_PTR_TABLE: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    SMD_EVENTS_FUN_TABLE: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    MUSIC_DURATION_LOOKUP_TABLE_1: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    MUSIC_DURATION_LOOKUP_TABLE_2: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    LFO_WAVEFORM_CALLBACKS: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    IS_DISP_ON: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    GXI_DMA_ID: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    RAND_SEQUENCE_NUM: Symbol[
        Optional[list[int]],
        None,
    ]

    JUICE_BAR_NECTAR_IQ_GAIN: Symbol[
        Optional[list[int]],
        None,
    ]

    DEBUG_TEXT_SPEED: Symbol[
        Optional[list[int]],
        None,
    ]

    REGULAR_TEXT_SPEED: Symbol[
        Optional[list[int]],
        None,
    ]

    HERO_START_LEVEL: Symbol[
        Optional[list[int]],
        None,
    ]

    PARTNER_START_LEVEL: Symbol[
        Optional[list[int]],
        None,
    ]


Arm9Protocol = SectionProtocol[
    Arm9FunctionsProtocol,
    Arm9DataProtocol,
    int,
]


class ItcmFunctionsProtocol(Protocol):

    CopyAndInterleave: Symbol[
        list[int],
        None,
    ]

    CopyAndInterleave0: Symbol[
        list[int],
        None,
    ]

    Render3dSetTextureParams: Symbol[
        list[int],
        None,
    ]

    Render3dSetPaletteBase: Symbol[
        list[int],
        None,
    ]

    Render3dRectangle: Symbol[
        list[int],
        None,
    ]

    GeomSetPolygonAttributes: Symbol[
        list[int],
        None,
    ]

    Render3dQuadrilateral: Symbol[
        list[int],
        None,
    ]

    Render3dTiling: Symbol[
        list[int],
        None,
    ]

    Render3dTextureInternal: Symbol[
        list[int],
        None,
    ]

    Render3dTexture: Symbol[
        list[int],
        None,
    ]

    Render3dTextureNoSetup: Symbol[
        list[int],
        None,
    ]

    NewRender3dElement: Symbol[
        list[int],
        None,
    ]

    EnqueueRender3dTexture: Symbol[
        list[int],
        None,
    ]

    EnqueueRender3dTiling: Symbol[
        list[int],
        None,
    ]

    NewRender3dRectangle: Symbol[
        list[int],
        None,
    ]

    NewRender3dQuadrilateral: Symbol[
        list[int],
        None,
    ]

    NewRender3dTexture: Symbol[
        list[int],
        None,
    ]

    NewRender3dTiling: Symbol[
        list[int],
        None,
    ]

    Render3dProcessQueue: Symbol[
        list[int],
        None,
    ]

    GetKeyN2MSwitch: Symbol[
        list[int],
        None,
    ]

    GetKeyN2M: Symbol[
        list[int],
        None,
    ]

    GetKeyN2MBaseForm: Symbol[
        list[int],
        None,
    ]

    GetKeyM2NSwitch: Symbol[
        list[int],
        None,
    ]

    GetKeyM2N: Symbol[
        list[int],
        None,
    ]

    GetKeyM2NBaseForm: Symbol[
        list[int],
        None,
    ]

    OS_IrqHandler: Symbol[
        list[int],
        None,
    ]

    OS_IrqHandler_ThreadSwitch: Symbol[
        list[int],
        None,
    ]

    OSi_DoResetSystem: Symbol[
        Optional[list[int]],
        None,
    ]

    OSi_DoBoot: Symbol[
        Optional[list[int]],
        None,
    ]

    OSi_CpuClear32: Symbol[
        Optional[list[int]],
        None,
    ]

    OSi_ReloadRomData: Symbol[
        Optional[list[int]],
        None,
    ]

    OSi_ReadCardRom32: Symbol[
        Optional[list[int]],
        None,
    ]

    MIi_DmaSetParams: Symbol[
        list[int],
        None,
    ]

    MIi_DmaSetParams_Wait: Symbol[
        Optional[list[int]],
        None,
    ]

    MIi_DmaSetParams_NoInt: Symbol[
        Optional[list[int]],
        None,
    ]

    ShouldMonsterRunAwayAndShowEffectOutlawCheck: Symbol[
        list[int],
        None,
    ]

    AiMovement: Symbol[
        list[int],
        None,
    ]

    CalculateAiTargetPos: Symbol[
        list[int],
        None,
    ]

    ChooseAiMove: Symbol[
        list[int],
        None,
    ]

    LightningRodStormDrainCheck: Symbol[
        list[int],
        None,
    ]


class ItcmDataProtocol(Protocol):

    MEMORY_ALLOCATION_TABLE: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    DEFAULT_MEMORY_ARENA: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    DEFAULT_MEMORY_ARENA_BLOCKS: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    RENDER_3D_FUNCTIONS: Symbol[
        list[int],
        None,
    ]


ItcmProtocol = SectionProtocol[
    ItcmFunctionsProtocol,
    ItcmDataProtocol,
    int,
]


class LibsFunctionsProtocol(Protocol):

    DseDriver_LoadDefaultSettings: Symbol[
        Optional[list[int]],
        None,
    ]

    DseDriver_IsSettingsValid: Symbol[
        Optional[list[int]],
        None,
    ]

    DseDriver_ConfigureHeap: Symbol[
        Optional[list[int]],
        None,
    ]

    DseDriver_Init: Symbol[
        Optional[list[int]],
        None,
    ]

    Dse_SetError: Symbol[
        Optional[list[int]],
        None,
    ]

    Dse_SetError2: Symbol[
        Optional[list[int]],
        None,
    ]

    DseUtil_ByteSwap32: Symbol[
        Optional[list[int]],
        None,
    ]

    SoundUtil_GetRandomNumber: Symbol[
        Optional[list[int]],
        None,
    ]

    DseMem_Init: Symbol[
        Optional[list[int]],
        None,
    ]

    DseMem_Quit: Symbol[
        Optional[list[int]],
        None,
    ]

    DseMem_AllocateUser: Symbol[
        Optional[list[int]],
        None,
    ]

    DseMem_Allocate: Symbol[
        Optional[list[int]],
        None,
    ]

    DseMem_AllocateThreadStack: Symbol[
        Optional[list[int]],
        None,
    ]

    DseMem_Free: Symbol[
        Optional[list[int]],
        None,
    ]

    DseMem_Clear: Symbol[
        Optional[list[int]],
        None,
    ]

    DseFile_CheckHeader: Symbol[
        Optional[list[int]],
        None,
    ]

    DseSwd_SysInit: Symbol[
        Optional[list[int]],
        None,
    ]

    DseSwd_SysQuit: Symbol[
        Optional[list[int]],
        None,
    ]

    DseSwd_SampleLoaderMain: Symbol[
        Optional[list[int]],
        None,
    ]

    DseSwd_MainBankDummyCallback: Symbol[
        Optional[list[int]],
        None,
    ]

    DseSwd_LoadMainBank: Symbol[
        Optional[list[int]],
        None,
    ]

    DseSwd_LoadBank: Symbol[
        Optional[list[int]],
        None,
    ]

    DseSwd_IsBankLoading: Symbol[
        Optional[list[int]],
        None,
    ]

    DseSwd_LoadWaves: Symbol[
        Optional[list[int]],
        None,
    ]

    DseSwd_LoadWavesInternal: Symbol[
        Optional[list[int]],
        None,
    ]

    DseSwd_Unload: Symbol[
        Optional[list[int]],
        None,
    ]

    ReadWaviEntry: Symbol[
        Optional[list[int]],
        None,
    ]

    DseSwd_GetInstrument: Symbol[
        Optional[list[int]],
        None,
    ]

    DseSwd_GetNextSplitInRange: Symbol[
        Optional[list[int]],
        None,
    ]

    DseSwd_GetMainBankById: Symbol[
        Optional[list[int]],
        None,
    ]

    DseSwd_GetBankById: Symbol[
        Optional[list[int]],
        None,
    ]

    DseSwd_InitMainBankFileReader: Symbol[
        Optional[list[int]],
        None,
    ]

    DseSwd_OpenMainBankFileReader: Symbol[
        Optional[list[int]],
        None,
    ]

    DseSwd_CloseMainBankFileReader: Symbol[
        Optional[list[int]],
        None,
    ]

    DseSwd_ReadMainBank: Symbol[
        Optional[list[int]],
        None,
    ]

    DseBgm_DefaultSignalCallback: Symbol[
        Optional[list[int]],
        None,
    ]

    DseBgm_Load: Symbol[
        Optional[list[int]],
        None,
    ]

    DseBgm_Unload: Symbol[
        Optional[list[int]],
        None,
    ]

    DseBgm_SetSignalCallback: Symbol[
        Optional[list[int]],
        None,
    ]

    DseBgm_IsPlaying: Symbol[
        Optional[list[int]],
        None,
    ]

    ResumeBgm: Symbol[
        Optional[list[int]],
        None,
    ]

    DseBgm_Stop: Symbol[
        Optional[list[int]],
        None,
    ]

    DseBgm_StopAll: Symbol[
        Optional[list[int]],
        None,
    ]

    DseBgm_SetFades: Symbol[
        Optional[list[int]],
        None,
    ]

    DseSequence_Start: Symbol[
        Optional[list[int]],
        None,
    ]

    DseSequence_PauseList: Symbol[
        Optional[list[int]],
        None,
    ]

    DseSequence_SetFades: Symbol[
        Optional[list[int]],
        None,
    ]

    DseSequence_GetParameter: Symbol[
        Optional[list[int]],
        None,
    ]

    DseSequence_GetSmallestNumLoops: Symbol[
        Optional[list[int]],
        None,
    ]

    DseSequence_Reset: Symbol[
        Optional[list[int]],
        None,
    ]

    DseSequence_Stop: Symbol[
        Optional[list[int]],
        None,
    ]

    FindSmdlSongChunk: Symbol[
        Optional[list[int]],
        None,
    ]

    DseSequence_LoadSong: Symbol[
        Optional[list[int]],
        None,
    ]

    DseSequence_GetById: Symbol[
        Optional[list[int]],
        None,
    ]

    DseSequence_AllocateNew: Symbol[
        Optional[list[int]],
        None,
    ]

    DseSequence_Unload: Symbol[
        Optional[list[int]],
        None,
    ]

    DseSequence_InitTracks: Symbol[
        Optional[list[int]],
        None,
    ]

    DseBgm_SysSetupNoteList: Symbol[
        Optional[list[int]],
        None,
    ]

    DseSe_SysReset: Symbol[
        Optional[list[int]],
        None,
    ]

    DseSe_Load: Symbol[
        Optional[list[int]],
        None,
    ]

    DseSe_Unload: Symbol[
        Optional[list[int]],
        None,
    ]

    DseSe_GetUsedBankIDs: Symbol[
        Optional[list[int]],
        None,
    ]

    DseSe_HasPlayingInstances: Symbol[
        Optional[list[int]],
        None,
    ]

    DseSe_Play: Symbol[
        Optional[list[int]],
        None,
    ]

    DseSe_GetEffectSong: Symbol[
        Optional[list[int]],
        None,
    ]

    DseSe_CheckTooManyInstances: Symbol[
        Optional[list[int]],
        None,
    ]

    DseSe_CheckTooManyInstancesInGroup: Symbol[
        Optional[list[int]],
        None,
    ]

    DseSe_GetBestSeqAllocation: Symbol[
        Optional[list[int]],
        None,
    ]

    DseSe_GetById: Symbol[
        Optional[list[int]],
        None,
    ]

    DseSe_Stop: Symbol[
        Optional[list[int]],
        None,
    ]

    DseSe_StopAll: Symbol[
        Optional[list[int]],
        None,
    ]

    DseSe_StopSeq: Symbol[
        Optional[list[int]],
        None,
    ]

    FlushChannels: Symbol[
        Optional[list[int]],
        None,
    ]

    DseDriver_StartMainThread: Symbol[
        Optional[list[int]],
        None,
    ]

    DseDriver_StartTickTimer: Symbol[
        Optional[list[int]],
        None,
    ]

    DseDriver_NotifyTick: Symbol[
        Optional[list[int]],
        None,
    ]

    DseDriver_Main: Symbol[
        Optional[list[int]],
        None,
    ]

    DseSequence_TickNotes: Symbol[
        Optional[list[int]],
        None,
    ]

    ParseDseEvent: Symbol[
        Optional[list[int]],
        None,
    ]

    UpdateSequencerTracks: Symbol[
        Optional[list[int]],
        None,
    ]

    DseSequence_TickFades: Symbol[
        Optional[list[int]],
        None,
    ]

    DseTrackEvent_Invalid: Symbol[
        Optional[list[int]],
        None,
    ]

    DseTrackEvent_WaitSame: Symbol[
        Optional[list[int]],
        None,
    ]

    DseTrackEvent_WaitDelta: Symbol[
        Optional[list[int]],
        None,
    ]

    DseTrackEvent_Wait8: Symbol[
        Optional[list[int]],
        None,
    ]

    DseTrackEvent_Wait16: Symbol[
        Optional[list[int]],
        None,
    ]

    DseTrackEvent_Wait24: Symbol[
        Optional[list[int]],
        None,
    ]

    DseTrackEvent_WaitUntilFadeout: Symbol[
        Optional[list[int]],
        None,
    ]

    DseTrackEvent_EndTrack: Symbol[
        Optional[list[int]],
        None,
    ]

    DseTrackEvent_MainLoopBegin: Symbol[
        Optional[list[int]],
        None,
    ]

    DseTrackEvent_SubLoopBegin: Symbol[
        Optional[list[int]],
        None,
    ]

    DseTrackEvent_SubLoopEnd: Symbol[
        Optional[list[int]],
        None,
    ]

    DseTrackEvent_SubLoopBreakOnLastIteration: Symbol[
        Optional[list[int]],
        None,
    ]

    DseTrackEvent_SetOctave: Symbol[
        Optional[list[int]],
        None,
    ]

    DseTrackEvent_OctaveDelta: Symbol[
        Optional[list[int]],
        None,
    ]

    DseTrackEvent_SetBpm: Symbol[
        Optional[list[int]],
        None,
    ]

    DseTrackEvent_SetBpm2: Symbol[
        Optional[list[int]],
        None,
    ]

    DseTrackEvent_SetBank: Symbol[
        Optional[list[int]],
        None,
    ]

    DseTrackEvent_SetBankMsb: Symbol[
        Optional[list[int]],
        None,
    ]

    DseTrackEvent_SetBankLsb: Symbol[
        Optional[list[int]],
        None,
    ]

    DseTrackEvent_Dummy1Byte: Symbol[
        Optional[list[int]],
        None,
    ]

    DseTrackEvent_SetInstrument: Symbol[
        Optional[list[int]],
        None,
    ]

    DseTrackEvent_SongVolumeFade: Symbol[
        Optional[list[int]],
        None,
    ]

    DseTrackEvent_RestoreEnvelopeDefaults: Symbol[
        Optional[list[int]],
        None,
    ]

    DseTrackEvent_SetEnvelopeAttackBegin: Symbol[
        Optional[list[int]],
        None,
    ]

    DseTrackEvent_SetEnvelopeAttackTime: Symbol[
        Optional[list[int]],
        None,
    ]

    DseTrackEvent_SetEnvelopeHoldTime: Symbol[
        Optional[list[int]],
        None,
    ]

    DseTrackEvent_SetEnvelopeDecayTimeAndSustainLevel: Symbol[
        Optional[list[int]],
        None,
    ]

    DseTrackEvent_SetEnvelopeSustainTime: Symbol[
        Optional[list[int]],
        None,
    ]

    DseTrackEvent_SetEnvelopeReleaseTime: Symbol[
        Optional[list[int]],
        None,
    ]

    DseTrackEvent_SetNoteDurationMultiplier: Symbol[
        Optional[list[int]],
        None,
    ]

    DseTrackEvent_ForceLfoEnvelopeLevel: Symbol[
        Optional[list[int]],
        None,
    ]

    DseTrackEvent_SetHoldNotes: Symbol[
        Optional[list[int]],
        None,
    ]

    DseTrackEvent_SetFlagBit1Unknown: Symbol[
        Optional[list[int]],
        None,
    ]

    DseTrackEvent_SetOptionalVolume: Symbol[
        Optional[list[int]],
        None,
    ]

    DseTrackEvent_Dummy2Bytes: Symbol[
        Optional[list[int]],
        None,
    ]

    DseTrackEvent_SetTuning: Symbol[
        Optional[list[int]],
        None,
    ]

    DseTrackEvent_TuningDeltaCoarse: Symbol[
        Optional[list[int]],
        None,
    ]

    DseTrackEvent_TuningDeltaFine: Symbol[
        Optional[list[int]],
        None,
    ]

    DseTrackEvent_TuningDeltaFull: Symbol[
        Optional[list[int]],
        None,
    ]

    DseTrackEvent_TuningFade: Symbol[
        Optional[list[int]],
        None,
    ]

    DseTrackEvent_SetNoteRandomRegion: Symbol[
        Optional[list[int]],
        None,
    ]

    DseTrackEvent_SetTuningJitterAmplitude: Symbol[
        Optional[list[int]],
        None,
    ]

    DseTrackEvent_SetKeyBend: Symbol[
        Optional[list[int]],
        None,
    ]

    DseTrackEvent_SetUnknown2: Symbol[
        Optional[list[int]],
        None,
    ]

    DseTrackEvent_SetKeyBendRange: Symbol[
        Optional[list[int]],
        None,
    ]

    DseTrackEvent_SetupKeyBendLfo: Symbol[
        Optional[list[int]],
        None,
    ]

    DseTrackEvent_SetupKeyBendLfoEnvelope: Symbol[
        Optional[list[int]],
        None,
    ]

    DseTrackEvent_UseKeyBendLfo: Symbol[
        Optional[list[int]],
        None,
    ]

    DseTrackEvent_SetVolume: Symbol[
        Optional[list[int]],
        None,
    ]

    DseTrackEvent_VolumeDelta: Symbol[
        Optional[list[int]],
        None,
    ]

    DseTrackEvent_VolumeFade: Symbol[
        Optional[list[int]],
        None,
    ]

    DseTrackEvent_SetExpression: Symbol[
        Optional[list[int]],
        None,
    ]

    DseTrackEvent_SetupVolumeLfo: Symbol[
        Optional[list[int]],
        None,
    ]

    DseTrackEvent_SetupVolumeLfoEnvelope: Symbol[
        Optional[list[int]],
        None,
    ]

    DseTrackEvent_UseVolumeLfo: Symbol[
        Optional[list[int]],
        None,
    ]

    DseTrackEvent_SetPan: Symbol[
        Optional[list[int]],
        None,
    ]

    DseTrackEvent_PanDelta: Symbol[
        Optional[list[int]],
        None,
    ]

    DseTrackEvent_PanFade: Symbol[
        Optional[list[int]],
        None,
    ]

    DseTrackEvent_SetupPanLfo: Symbol[
        Optional[list[int]],
        None,
    ]

    DseTrackEvent_SetupPanLfoEnvelope: Symbol[
        Optional[list[int]],
        None,
    ]

    DseTrackEvent_UsePanLfo: Symbol[
        Optional[list[int]],
        None,
    ]

    DseTrackEvent_SetupLfo: Symbol[
        Optional[list[int]],
        None,
    ]

    DseTrackEvent_SetupLfoEnvelope: Symbol[
        Optional[list[int]],
        None,
    ]

    DseTrackEvent_SetLfoParameter: Symbol[
        Optional[list[int]],
        None,
    ]

    DseTrackEvent_UseLfo: Symbol[
        Optional[list[int]],
        None,
    ]

    DseTrackEvent_Signal: Symbol[
        Optional[list[int]],
        None,
    ]

    DseTrackEvent_Dummy2Bytes2: Symbol[
        Optional[list[int]],
        None,
    ]

    RetEu0x02073300: Symbol[
        Optional[list[int]],
        None,
    ]

    RetEu0x02073304: Symbol[
        Optional[list[int]],
        None,
    ]

    RetEu0x02073308: Symbol[
        Optional[list[int]],
        None,
    ]

    RetEu0x0207333c: Symbol[
        Optional[list[int]],
        None,
    ]

    RetEu0x02073340: Symbol[
        Optional[list[int]],
        None,
    ]

    RetEu0x02073594: Symbol[
        Optional[list[int]],
        None,
    ]

    RetEu0x02073598: Symbol[
        Optional[list[int]],
        None,
    ]

    RetEu0x0207359c: Symbol[
        Optional[list[int]],
        None,
    ]

    DseSynth_Reset: Symbol[
        Optional[list[int]],
        None,
    ]

    DseSynth_AllocateNew: Symbol[
        Optional[list[int]],
        None,
    ]

    DseSynth_Unload: Symbol[
        Optional[list[int]],
        None,
    ]

    DseSynth_ClearHeldNotes: Symbol[
        Optional[list[int]],
        None,
    ]

    DseSynth_ResetAndSetBankAndSequence: Symbol[
        Optional[list[int]],
        None,
    ]

    DseSynth_StopChannels: Symbol[
        Optional[list[int]],
        None,
    ]

    DseSynth_ResetAllVoiceTimersAndVolumes: Symbol[
        Optional[list[int]],
        None,
    ]

    DseSynth_RestoreHeldNotes: Symbol[
        Optional[list[int]],
        None,
    ]

    DseSynth_SetGlobalVolumeIndex: Symbol[
        Optional[list[int]],
        None,
    ]

    DseSynth_SetBend: Symbol[
        Optional[list[int]],
        None,
    ]

    DseSynth_SetVolume: Symbol[
        Optional[list[int]],
        None,
    ]

    DseSynth_SetPan: Symbol[
        Optional[list[int]],
        None,
    ]

    DseSynth_SetBankAndSequence: Symbol[
        Optional[list[int]],
        None,
    ]

    DseChannel_Init: Symbol[
        Optional[list[int]],
        None,
    ]

    DseChannel_DeallocateVoices: Symbol[
        Optional[list[int]],
        None,
    ]

    DseChannel_ResetTimerAndVolumeForVoices: Symbol[
        Optional[list[int]],
        None,
    ]

    DseChannel_SetBank: Symbol[
        Optional[list[int]],
        None,
    ]

    DseChannel_SetInstrument: Symbol[
        Optional[list[int]],
        None,
    ]

    DseChannel_SetLfoConstEnvelopeLevel: Symbol[
        Optional[list[int]],
        None,
    ]

    DseChannel_SetKeyBend: Symbol[
        Optional[list[int]],
        None,
    ]

    DseChannel_AllocateNote: Symbol[
        Optional[list[int]],
        None,
    ]

    DseChannel_ReleaseNoteInternal: Symbol[
        Optional[list[int]],
        None,
    ]

    DseChannel_ChangeNote: Symbol[
        Optional[list[int]],
        None,
    ]

    DseChannel_ReleaseNote: Symbol[
        Optional[list[int]],
        None,
    ]

    DseVoice_PlayNote: Symbol[
        Optional[list[int]],
        None,
    ]

    DseVoice_ReleaseNote: Symbol[
        Optional[list[int]],
        None,
    ]

    DseVoice_UpdateParameters: Symbol[
        Optional[list[int]],
        None,
    ]

    DseVoice_ResetAll: Symbol[
        Optional[list[int]],
        None,
    ]

    DseVoice_ResetHW: Symbol[
        Optional[list[int]],
        None,
    ]

    UpdateChannels: Symbol[
        Optional[list[int]],
        None,
    ]

    DseVoice_Cleanup: Symbol[
        Optional[list[int]],
        None,
    ]

    DseVoice_Allocate: Symbol[
        Optional[list[int]],
        None,
    ]

    DseVoice_Start: Symbol[
        Optional[list[int]],
        None,
    ]

    DseVoice_ReleaseHeld: Symbol[
        Optional[list[int]],
        None,
    ]

    DseVoice_Release: Symbol[
        Optional[list[int]],
        None,
    ]

    DseVoice_Deallocate: Symbol[
        Optional[list[int]],
        None,
    ]

    DseVoice_FlagForActivation: Symbol[
        Optional[list[int]],
        None,
    ]

    DseVoice_FlagForDeactivation: Symbol[
        Optional[list[int]],
        None,
    ]

    DseVoice_CountNumActiveInChannel: Symbol[
        Optional[list[int]],
        None,
    ]

    DseVoice_UpdateHardware: Symbol[
        Optional[list[int]],
        None,
    ]

    SoundEnvelope_Reset: Symbol[
        Optional[list[int]],
        None,
    ]

    SoundEnvelopeParameters_Reset: Symbol[
        Optional[list[int]],
        None,
    ]

    SoundEnvelopeParameters_CheckValidity: Symbol[
        Optional[list[int]],
        None,
    ]

    SoundEnvelope_SetParameters: Symbol[
        Optional[list[int]],
        None,
    ]

    SoundEnvelope_SetSlide: Symbol[
        Optional[list[int]],
        None,
    ]

    UpdateTrackVolumeEnvelopes: Symbol[
        Optional[list[int]],
        None,
    ]

    SoundEnvelope_Release: Symbol[
        Optional[list[int]],
        None,
    ]

    SoundEnvelope_Stop: Symbol[
        Optional[list[int]],
        None,
    ]

    SoundEnvelope_ForceVolume: Symbol[
        Optional[list[int]],
        None,
    ]

    SoundEnvelope_Stop2: Symbol[
        Optional[list[int]],
        None,
    ]

    SoundEnvelope_Tick: Symbol[
        Optional[list[int]],
        None,
    ]

    SoundLfoBank_Reset: Symbol[
        Optional[list[int]],
        None,
    ]

    SoundLfoBank_Set: Symbol[
        Optional[list[int]],
        None,
    ]

    SoundLfoBank_SetConstEnvelopes: Symbol[
        Optional[list[int]],
        None,
    ]

    SoundLfoBank_Tick: Symbol[
        Optional[list[int]],
        None,
    ]

    SoundLfoWave_InvalidFunc: Symbol[
        Optional[list[int]],
        None,
    ]

    SoundLfoWave_HalfSquareFunc: Symbol[
        Optional[list[int]],
        None,
    ]

    SoundLfoWave_FullSquareFunc: Symbol[
        Optional[list[int]],
        None,
    ]

    SoundLfoWave_HalfTriangleFunc: Symbol[
        Optional[list[int]],
        None,
    ]

    SoundLfoWave_FullTriangleFunc: Symbol[
        Optional[list[int]],
        None,
    ]

    SoundLfoWave_SawFunc: Symbol[
        Optional[list[int]],
        None,
    ]

    SoundLfoWave_ReverseSawFunc: Symbol[
        Optional[list[int]],
        None,
    ]

    SoundLfoWave_HalfNoiseFunc: Symbol[
        Optional[list[int]],
        None,
    ]

    SoundLfoWave_FullNoiseFunc: Symbol[
        Optional[list[int]],
        None,
    ]

    Crypto_RC4Init: Symbol[
        Optional[list[int]],
        None,
    ]

    Crypto_RC4Encrypt: Symbol[
        Optional[list[int]],
        None,
    ]

    Mtx_LookAt: Symbol[
        Optional[list[int]],
        None,
    ]

    Mtx_OrthoW: Symbol[
        Optional[list[int]],
        None,
    ]

    FX_Div: Symbol[
        Optional[list[int]],
        None,
    ]

    FX_GetDivResultFx64c: Symbol[
        Optional[list[int]],
        None,
    ]

    FX_GetDivResult: Symbol[
        Optional[list[int]],
        None,
    ]

    FX_InvAsync: Symbol[
        Optional[list[int]],
        None,
    ]

    FX_DivAsync: Symbol[
        Optional[list[int]],
        None,
    ]

    FX_DivS32: Symbol[
        Optional[list[int]],
        None,
    ]

    FX_ModS32: Symbol[
        Optional[list[int]],
        None,
    ]

    Vec_DotProduct: Symbol[
        Optional[list[int]],
        None,
    ]

    Vec_CrossProduct: Symbol[
        Optional[list[int]],
        None,
    ]

    Vec_Normalize: Symbol[
        Optional[list[int]],
        None,
    ]

    Vec_Distance: Symbol[
        Optional[list[int]],
        None,
    ]

    FX_Atan2Idx: Symbol[
        Optional[list[int]],
        None,
    ]

    FX_Init: Symbol[
        Optional[list[int]],
        None,
    ]

    GX_Init: Symbol[
        Optional[list[int]],
        None,
    ]

    GX_HBlankIntr: Symbol[
        Optional[list[int]],
        None,
    ]

    GX_VBlankIntr: Symbol[
        Optional[list[int]],
        None,
    ]

    GX_DispOff: Symbol[
        Optional[list[int]],
        None,
    ]

    GX_DispOn: Symbol[
        Optional[list[int]],
        None,
    ]

    GX_SetGraphicsMode: Symbol[
        Optional[list[int]],
        None,
    ]

    Gxs_SetGraphicsMode: Symbol[
        Optional[list[int]],
        None,
    ]

    GXx_SetMasterBrightness: Symbol[
        Optional[list[int]],
        None,
    ]

    GX_InitGxState: Symbol[
        Optional[list[int]],
        None,
    ]

    EnableVramBanksInSetDontSave: Symbol[
        Optional[list[int]],
        None,
    ]

    GX_SetBankForBg: Symbol[
        Optional[list[int]],
        None,
    ]

    GX_SetBankForObj: Symbol[
        Optional[list[int]],
        None,
    ]

    GX_SetBankForBgExtPltt: Symbol[
        Optional[list[int]],
        None,
    ]

    GX_SetBankForObjExtPltt: Symbol[
        Optional[list[int]],
        None,
    ]

    GX_SetBankForTex: Symbol[
        Optional[list[int]],
        None,
    ]

    GX_SetBankForTexPltt: Symbol[
        Optional[list[int]],
        None,
    ]

    GX_SetBankForClearImage: Symbol[
        Optional[list[int]],
        None,
    ]

    GX_SetBankForArm7: Symbol[
        Optional[list[int]],
        None,
    ]

    GX_SetBankForLcdc: Symbol[
        Optional[list[int]],
        None,
    ]

    GX_SetBankForSubBg: Symbol[
        Optional[list[int]],
        None,
    ]

    GX_SetBankForSubObj: Symbol[
        Optional[list[int]],
        None,
    ]

    GX_SetBankForSubBgExtPltt: Symbol[
        Optional[list[int]],
        None,
    ]

    GX_SetBankForSubObjExtPltt: Symbol[
        Optional[list[int]],
        None,
    ]

    EnableVramBanksInSet: Symbol[
        Optional[list[int]],
        None,
    ]

    GX_ResetBankForBgExtPltt: Symbol[
        Optional[list[int]],
        None,
    ]

    GX_ResetBankForObjExtPltt: Symbol[
        Optional[list[int]],
        None,
    ]

    GX_ResetBankForTex: Symbol[
        Optional[list[int]],
        None,
    ]

    GX_ResetBankForTexPltt: Symbol[
        Optional[list[int]],
        None,
    ]

    GX_ResetBankForSubBgExtPltt: Symbol[
        Optional[list[int]],
        None,
    ]

    GX_ResetBankForSubObjExtPltt: Symbol[
        Optional[list[int]],
        None,
    ]

    DisableBankForX: Symbol[
        Optional[list[int]],
        None,
    ]

    GX_DisableBankForBg: Symbol[
        Optional[list[int]],
        None,
    ]

    GX_DisableBankForObj: Symbol[
        Optional[list[int]],
        None,
    ]

    GX_DisableBankForBgExtPltt: Symbol[
        Optional[list[int]],
        None,
    ]

    GX_DisableBankForObjExtPltt: Symbol[
        Optional[list[int]],
        None,
    ]

    GX_DisableBankForTex: Symbol[
        Optional[list[int]],
        None,
    ]

    GX_DisableBankForTexPltt: Symbol[
        Optional[list[int]],
        None,
    ]

    GX_DisableBankForClearImage: Symbol[
        Optional[list[int]],
        None,
    ]

    GX_DisableBankForArm7: Symbol[
        Optional[list[int]],
        None,
    ]

    GX_DisableBankForLcdc: Symbol[
        Optional[list[int]],
        None,
    ]

    GX_DisableBankForSubBg: Symbol[
        Optional[list[int]],
        None,
    ]

    GX_DisableBankForSubObj: Symbol[
        Optional[list[int]],
        None,
    ]

    GX_DisableBankForSubBgExtPltt: Symbol[
        Optional[list[int]],
        None,
    ]

    GX_DisableBankForSubObjExtPltt: Symbol[
        Optional[list[int]],
        None,
    ]

    G2_GetBG0ScrPtr: Symbol[
        Optional[list[int]],
        None,
    ]

    G2S_GetBG0ScrPtr: Symbol[
        Optional[list[int]],
        None,
    ]

    G2_GetBG1ScrPtr: Symbol[
        Optional[list[int]],
        None,
    ]

    G2S_GetBG1ScrPtr: Symbol[
        Optional[list[int]],
        None,
    ]

    G2_GetBG2ScrPtr: Symbol[
        Optional[list[int]],
        None,
    ]

    G2_GetBG3ScrPtr: Symbol[
        Optional[list[int]],
        None,
    ]

    G2_GetBG0CharPtr: Symbol[
        Optional[list[int]],
        None,
    ]

    G2S_GetBG0CharPtr: Symbol[
        Optional[list[int]],
        None,
    ]

    G2_GetBG1CharPtr: Symbol[
        Optional[list[int]],
        None,
    ]

    G2S_GetBG1CharPtr: Symbol[
        Optional[list[int]],
        None,
    ]

    G2_GetBG2CharPtr: Symbol[
        Optional[list[int]],
        None,
    ]

    G2_GetBG3CharPtr: Symbol[
        Optional[list[int]],
        None,
    ]

    G2x_SetBlendAlpha: Symbol[
        Optional[list[int]],
        None,
    ]

    G2x_SetBlendBrightness: Symbol[
        Optional[list[int]],
        None,
    ]

    G2x_ChangeBlendBrightness: Symbol[
        Optional[list[int]],
        None,
    ]

    G3_LoadMtx44: Symbol[
        Optional[list[int]],
        None,
    ]

    G3_LoadMtx43: Symbol[
        Optional[list[int]],
        None,
    ]

    G3_MultMtx43: Symbol[
        Optional[list[int]],
        None,
    ]

    G3X_Init: Symbol[
        Optional[list[int]],
        None,
    ]

    G3X_Reset: Symbol[
        Optional[list[int]],
        None,
    ]

    G3X_ClearFifo: Symbol[
        Optional[list[int]],
        None,
    ]

    G3X_InitMtxStack: Symbol[
        Optional[list[int]],
        None,
    ]

    G3X_ResetMtxStack: Symbol[
        Optional[list[int]],
        None,
    ]

    G3X_SetClearColor: Symbol[
        Optional[list[int]],
        None,
    ]

    G3X_InitTable: Symbol[
        Optional[list[int]],
        None,
    ]

    G3X_GetMtxStackLevelPV: Symbol[
        Optional[list[int]],
        None,
    ]

    G3X_GetMtxStackLevelPJ: Symbol[
        Optional[list[int]],
        None,
    ]

    GXi_NopClearFifo128: Symbol[
        Optional[list[int]],
        None,
    ]

    G3i_OrthoW: Symbol[
        Optional[list[int]],
        None,
    ]

    G3i_LookAt: Symbol[
        Optional[list[int]],
        None,
    ]

    GX_LoadBgPltt: Symbol[
        Optional[list[int]],
        None,
    ]

    Gxs_LoadBgPltt: Symbol[
        Optional[list[int]],
        None,
    ]

    GX_LoadObjPltt: Symbol[
        Optional[list[int]],
        None,
    ]

    Gxs_LoadObjPltt: Symbol[
        Optional[list[int]],
        None,
    ]

    GX_LoadOam: Symbol[
        Optional[list[int]],
        None,
    ]

    Gxs_LoadOam: Symbol[
        Optional[list[int]],
        None,
    ]

    GX_LoadObj: Symbol[
        Optional[list[int]],
        None,
    ]

    Gxs_LoadObj: Symbol[
        Optional[list[int]],
        None,
    ]

    GX_LoadBg0Scr: Symbol[
        Optional[list[int]],
        None,
    ]

    GX_LoadBg1Scr: Symbol[
        Optional[list[int]],
        None,
    ]

    Gxs_LoadBg1Scr: Symbol[
        Optional[list[int]],
        None,
    ]

    GX_LoadBg2Scr: Symbol[
        Optional[list[int]],
        None,
    ]

    GX_LoadBg3Scr: Symbol[
        Optional[list[int]],
        None,
    ]

    GX_LoadBg0Char: Symbol[
        Optional[list[int]],
        None,
    ]

    Gxs_LoadBg0Char: Symbol[
        Optional[list[int]],
        None,
    ]

    GX_LoadBg1Char: Symbol[
        Optional[list[int]],
        None,
    ]

    Gxs_LoadBg1Char: Symbol[
        Optional[list[int]],
        None,
    ]

    GX_LoadBg2Char: Symbol[
        Optional[list[int]],
        None,
    ]

    GX_LoadBg3Char: Symbol[
        Optional[list[int]],
        None,
    ]

    GX_BeginLoadBgExtPltt: Symbol[
        Optional[list[int]],
        None,
    ]

    GX_EndLoadBgExtPltt: Symbol[
        Optional[list[int]],
        None,
    ]

    GX_BeginLoadObjExtPltt: Symbol[
        Optional[list[int]],
        None,
    ]

    GX_EndLoadObjExtPltt: Symbol[
        Optional[list[int]],
        None,
    ]

    Gxs_BeginLoadBgExtPltt: Symbol[
        Optional[list[int]],
        None,
    ]

    Gxs_EndLoadBgExtPltt: Symbol[
        Optional[list[int]],
        None,
    ]

    Gxs_BeginLoadObjExtPltt: Symbol[
        Optional[list[int]],
        None,
    ]

    Gxs_EndLoadObjExtPltt: Symbol[
        Optional[list[int]],
        None,
    ]

    GX_BeginLoadTex: Symbol[
        Optional[list[int]],
        None,
    ]

    GX_LoadTex: Symbol[
        Optional[list[int]],
        None,
    ]

    GX_EndLoadTex: Symbol[
        Optional[list[int]],
        None,
    ]

    GX_BeginLoadTexPltt: Symbol[
        Optional[list[int]],
        None,
    ]

    GX_LoadTexPltt: Symbol[
        Optional[list[int]],
        None,
    ]

    GX_EndLoadTexPltt: Symbol[
        Optional[list[int]],
        None,
    ]

    GeomGxFifoSendMtx4x3: Symbol[
        Optional[list[int]],
        None,
    ]

    GX_SendFifo64B: Symbol[
        Optional[list[int]],
        None,
    ]

    OS_WaitIrq: Symbol[
        Optional[list[int]],
        None,
    ]

    OS_IrqDummy: Symbol[
        Optional[list[int]],
        None,
    ]

    OSi_IrqCallback: Symbol[
        Optional[list[int]],
        None,
    ]

    OSi_IrqDma0: Symbol[
        Optional[list[int]],
        None,
    ]

    OSi_IrqDma1: Symbol[
        Optional[list[int]],
        None,
    ]

    OSi_IrqDma2: Symbol[
        Optional[list[int]],
        None,
    ]

    OSi_IrqDma3: Symbol[
        Optional[list[int]],
        None,
    ]

    OSi_IrqTimer0: Symbol[
        Optional[list[int]],
        None,
    ]

    OSi_IrqTimer1: Symbol[
        Optional[list[int]],
        None,
    ]

    OSi_IrqTimer2: Symbol[
        Optional[list[int]],
        None,
    ]

    OSi_IrqTimer3: Symbol[
        Optional[list[int]],
        None,
    ]

    OS_InitIrqTable: Symbol[
        Optional[list[int]],
        None,
    ]

    OS_SetIrqFunction: Symbol[
        Optional[list[int]],
        None,
    ]

    OS_GetIrqFunction: Symbol[
        Optional[list[int]],
        None,
    ]

    OSi_EnterDmaCallback: Symbol[
        Optional[list[int]],
        None,
    ]

    OSi_EnterTimerCallback: Symbol[
        Optional[list[int]],
        None,
    ]

    OS_SetIrqMask: Symbol[
        Optional[list[int]],
        None,
    ]

    OS_EnableIrqMask: Symbol[
        Optional[list[int]],
        None,
    ]

    OS_DisableIrqMask: Symbol[
        Optional[list[int]],
        None,
    ]

    OS_ResetRequestIrqMask: Symbol[
        Optional[list[int]],
        None,
    ]

    OS_SetIrqStackChecker: Symbol[
        Optional[list[int]],
        None,
    ]

    OS_InitLock: Symbol[
        Optional[list[int]],
        None,
    ]

    OSi_DoLockByWord: Symbol[
        Optional[list[int]],
        None,
    ]

    OS_LockByWord: Symbol[
        Optional[list[int]],
        None,
    ]

    OSi_DoUnlockByWord: Symbol[
        Optional[list[int]],
        None,
    ]

    OS_UnlockByWord: Symbol[
        Optional[list[int]],
        None,
    ]

    OSi_DoTryLockByWord: Symbol[
        Optional[list[int]],
        None,
    ]

    OS_UnlockCartridge: Symbol[
        Optional[list[int]],
        None,
    ]

    OS_UnlockCartridgeVeneer: Symbol[
        Optional[list[int]],
        None,
    ]

    OS_TryLockCartridge: Symbol[
        Optional[list[int]],
        None,
    ]

    OSi_AllocateCartridgeBus: Symbol[
        Optional[list[int]],
        None,
    ]

    OSi_FreeCartridgeBus: Symbol[
        Optional[list[int]],
        None,
    ]

    OS_LockCard: Symbol[
        Optional[list[int]],
        None,
    ]

    OS_UnlockCard: Symbol[
        Optional[list[int]],
        None,
    ]

    OSi_AllocateCardBus: Symbol[
        Optional[list[int]],
        None,
    ]

    OSi_FreeCardBus: Symbol[
        Optional[list[int]],
        None,
    ]

    OS_ReadOwnerOfLockWord: Symbol[
        Optional[list[int]],
        None,
    ]

    OS_GetLockID: Symbol[
        Optional[list[int]],
        None,
    ]

    OS_ReleaseLockId: Symbol[
        Optional[list[int]],
        None,
    ]

    OS_VsPrintf: Symbol[
        Optional[list[int]],
        None,
    ]

    OS_VsNPrintf: Symbol[
        Optional[list[int]],
        None,
    ]

    OS_SnPrintf: Symbol[
        Optional[list[int]],
        None,
    ]

    OS_VsNPrintfExStub: Symbol[
        Optional[list[int]],
        None,
    ]

    OSi_GetUnusedThreadId: Symbol[
        Optional[list[int]],
        None,
    ]

    OSi_InsertLinkToQueue: Symbol[
        Optional[list[int]],
        None,
    ]

    OSi_RemoveLinkFromQueue: Symbol[
        Optional[list[int]],
        None,
    ]

    OSi_RemoveSpecifiedLinkFromQueue: Symbol[
        Optional[list[int]],
        None,
    ]

    OSi_RemoveMutexLinkFromQueue: Symbol[
        Optional[list[int]],
        None,
    ]

    OSi_InsertThreadToList: Symbol[
        Optional[list[int]],
        None,
    ]

    OSi_RemoveThreadFromList: Symbol[
        Optional[list[int]],
        None,
    ]

    OS_RescheduleThread: Symbol[
        Optional[list[int]],
        None,
    ]

    OS_InitThread: Symbol[
        Optional[list[int]],
        None,
    ]

    OS_IsThreadAvailable: Symbol[
        Optional[list[int]],
        None,
    ]

    OS_CreateThread: Symbol[
        Optional[list[int]],
        None,
    ]

    OS_ExitThread: Symbol[
        Optional[list[int]],
        None,
    ]

    OSi_ExitThread_ArgSpecified: Symbol[
        Optional[list[int]],
        None,
    ]

    OSi_ExitThread: Symbol[
        Optional[list[int]],
        None,
    ]

    OSi_ExitThread_Destroy: Symbol[
        Optional[list[int]],
        None,
    ]

    OS_DestroyThread: Symbol[
        Optional[list[int]],
        None,
    ]

    OSi_CancelThreadAlarmForSleep: Symbol[
        Optional[list[int]],
        None,
    ]

    OS_JoinThread: Symbol[
        Optional[list[int]],
        None,
    ]

    OS_IsThreadTerminated: Symbol[
        Optional[list[int]],
        None,
    ]

    OS_SleepThreadDirect: Symbol[
        Optional[list[int]],
        None,
    ]

    OS_SleepThread: Symbol[
        Optional[list[int]],
        None,
    ]

    OS_WakeupThread: Symbol[
        Optional[list[int]],
        None,
    ]

    OS_WakeupThreadDirect: Symbol[
        Optional[list[int]],
        None,
    ]

    OS_SelectThread: Symbol[
        Optional[list[int]],
        None,
    ]

    OS_YieldThread: Symbol[
        Optional[list[int]],
        None,
    ]

    OS_SetThreadPriority: Symbol[
        Optional[list[int]],
        None,
    ]

    OS_GetThreadPriority: Symbol[
        Optional[list[int]],
        None,
    ]

    OS_Sleep: Symbol[
        Optional[list[int]],
        None,
    ]

    OSi_SleepAlarmCallback: Symbol[
        Optional[list[int]],
        None,
    ]

    OS_SetSwitchThreadCallback: Symbol[
        Optional[list[int]],
        None,
    ]

    OSi_IdleThreadProc: Symbol[
        Optional[list[int]],
        None,
    ]

    OS_DisableScheduler: Symbol[
        Optional[list[int]],
        None,
    ]

    OS_EnableScheduler: Symbol[
        Optional[list[int]],
        None,
    ]

    OS_SetThreadDestructor: Symbol[
        Optional[list[int]],
        None,
    ]

    OS_InitContext: Symbol[
        Optional[list[int]],
        None,
    ]

    OS_SaveContext: Symbol[
        Optional[list[int]],
        None,
    ]

    OS_LoadContext: Symbol[
        Optional[list[int]],
        None,
    ]

    OS_IsRunOnEmulator: Symbol[
        Optional[list[int]],
        None,
    ]

    OS_GetConsoleType: Symbol[
        Optional[list[int]],
        None,
    ]

    OS_InitMessageQueue: Symbol[
        Optional[list[int]],
        None,
    ]

    OS_SendMessage: Symbol[
        Optional[list[int]],
        None,
    ]

    OS_ReceiveMessage: Symbol[
        Optional[list[int]],
        None,
    ]

    OS_JamMessage: Symbol[
        Optional[list[int]],
        None,
    ]

    OS_ReadMessage: Symbol[
        Optional[list[int]],
        None,
    ]

    OS_InitMutex: Symbol[
        Optional[list[int]],
        None,
    ]

    OS_LockMutex: Symbol[
        Optional[list[int]],
        None,
    ]

    OS_UnlockMutex: Symbol[
        Optional[list[int]],
        None,
    ]

    OSi_UnlockAllMutex: Symbol[
        Optional[list[int]],
        None,
    ]

    OS_TryLockMutex: Symbol[
        Optional[list[int]],
        None,
    ]

    OSi_EnqueueTail: Symbol[
        Optional[list[int]],
        None,
    ]

    OSi_DequeueItem: Symbol[
        Optional[list[int]],
        None,
    ]

    DC_Enable: Symbol[
        Optional[list[int]],
        None,
    ]

    DC_InvalidateAll: Symbol[
        Optional[list[int]],
        None,
    ]

    DC_StoreAll: Symbol[
        Optional[list[int]],
        None,
    ]

    DC_FlushAll: Symbol[
        Optional[list[int]],
        None,
    ]

    DC_InvalidateRange: Symbol[
        Optional[list[int]],
        None,
    ]

    DC_StoreRange: Symbol[
        Optional[list[int]],
        None,
    ]

    DC_FlushRange: Symbol[
        Optional[list[int]],
        None,
    ]

    DC_WaitWriteBufferEmpty: Symbol[
        Optional[list[int]],
        None,
    ]

    IC_Enable: Symbol[
        Optional[list[int]],
        None,
    ]

    IC_InvalidateAll: Symbol[
        Optional[list[int]],
        None,
    ]

    IC_InvalidateRange: Symbol[
        Optional[list[int]],
        None,
    ]

    OSi_WaitVCount0: Symbol[
        Optional[list[int]],
        None,
    ]

    OS_Init: Symbol[
        Optional[list[int]],
        None,
    ]

    OS_InitArena: Symbol[
        Optional[list[int]],
        None,
    ]

    OS_InitArenaEx: Symbol[
        Optional[list[int]],
        None,
    ]

    OS_GetArenaHi: Symbol[
        Optional[list[int]],
        None,
    ]

    OS_GetArenaLo: Symbol[
        Optional[list[int]],
        None,
    ]

    OS_GetInitArenaHi: Symbol[
        Optional[list[int]],
        None,
    ]

    OS_GetInitArenaLo: Symbol[
        Optional[list[int]],
        None,
    ]

    OS_SetArenaHi: Symbol[
        Optional[list[int]],
        None,
    ]

    OS_SetArenaLo: Symbol[
        Optional[list[int]],
        None,
    ]

    OS_AllocFromArenaLo: Symbol[
        Optional[list[int]],
        None,
    ]

    OS_GetDtcmAddress: Symbol[
        Optional[list[int]],
        None,
    ]

    OS_EnableProtectionUnit: Symbol[
        Optional[list[int]],
        None,
    ]

    OS_DisableProtectionUnit: Symbol[
        Optional[list[int]],
        None,
    ]

    OS_SetDPermissionsForProtectionRegion: Symbol[
        Optional[list[int]],
        None,
    ]

    OS_SetProtectionRegion1: Symbol[
        Optional[list[int]],
        None,
    ]

    OS_SetProtectionRegion2: Symbol[
        Optional[list[int]],
        None,
    ]

    OS_InitException: Symbol[
        Optional[list[int]],
        None,
    ]

    OSi_ExceptionHandler: Symbol[
        Optional[list[int]],
        None,
    ]

    OSi_GetAndDisplayContext: Symbol[
        Optional[list[int]],
        None,
    ]

    OSi_SetExContext: Symbol[
        Optional[list[int]],
        None,
    ]

    OSi_DisplayExContext: Symbol[
        Optional[list[int]],
        None,
    ]

    OSi_DisplayExContext_Helper: Symbol[
        Optional[list[int]],
        None,
    ]

    OSi_SetTimerReserved: Symbol[
        Optional[list[int]],
        None,
    ]

    OS_InitTick: Symbol[
        Optional[list[int]],
        None,
    ]

    OS_IsTickAvailable: Symbol[
        Optional[list[int]],
        None,
    ]

    OSi_CountUpTick: Symbol[
        Optional[list[int]],
        None,
    ]

    OS_GetTick: Symbol[
        Optional[list[int]],
        None,
    ]

    OS_GetTickLo: Symbol[
        Optional[list[int]],
        None,
    ]

    OS_SetTick: Symbol[
        Optional[list[int]],
        None,
    ]

    OSi_SetTimer: Symbol[
        Optional[list[int]],
        None,
    ]

    OS_InitAlarm: Symbol[
        Optional[list[int]],
        None,
    ]

    OS_IsAlarmAvailable: Symbol[
        Optional[list[int]],
        None,
    ]

    OS_CreateAlarm: Symbol[
        Optional[list[int]],
        None,
    ]

    OS_InsertAlarm: Symbol[
        Optional[list[int]],
        None,
    ]

    OS_SetAlarm: Symbol[
        Optional[list[int]],
        None,
    ]

    OS_CancelAlarm: Symbol[
        Optional[list[int]],
        None,
    ]

    OSi_AlarmHandler: Symbol[
        Optional[list[int]],
        None,
    ]

    OSi_ArrangeTimer: Symbol[
        Optional[list[int]],
        None,
    ]

    OS_InitVAlarm: Symbol[
        Optional[list[int]],
        None,
    ]

    OSi_InsertVAlarm: Symbol[
        Optional[list[int]],
        None,
    ]

    OSi_AppendVAlarm: Symbol[
        Optional[list[int]],
        None,
    ]

    OSi_DetachVAlarm: Symbol[
        Optional[list[int]],
        None,
    ]

    OS_CreateVAlarm: Symbol[
        Optional[list[int]],
        None,
    ]

    OS_SetPeriodicVAlarm: Symbol[
        Optional[list[int]],
        None,
    ]

    OSi_SetNextVAlarm: Symbol[
        Optional[list[int]],
        None,
    ]

    OS_CancelVAlarm: Symbol[
        Optional[list[int]],
        None,
    ]

    OSi_VAlarmHandler: Symbol[
        Optional[list[int]],
        None,
    ]

    OSi_CompareVCount: Symbol[
        Optional[list[int]],
        None,
    ]

    OSi_GetVFrame: Symbol[
        Optional[list[int]],
        None,
    ]

    OS_EnableInterrupts: Symbol[
        Optional[list[int]],
        None,
    ]

    OS_DisableInterrupts: Symbol[
        Optional[list[int]],
        None,
    ]

    OS_RestoreInterrupts: Symbol[
        Optional[list[int]],
        None,
    ]

    OS_EnableInterrupts_IrqAndFiq: Symbol[
        Optional[list[int]],
        None,
    ]

    OS_RestoreInterrupts_IrqAndFiq: Symbol[
        Optional[list[int]],
        None,
    ]

    OS_GetCpsrIrq: Symbol[
        Optional[list[int]],
        None,
    ]

    OS_GetProcMode: Symbol[
        Optional[list[int]],
        None,
    ]

    OS_SpinWait: Symbol[
        Optional[list[int]],
        None,
    ]

    OS_WaitVBlankIntr: Symbol[
        Optional[list[int]],
        None,
    ]

    OS_InitReset: Symbol[
        Optional[list[int]],
        None,
    ]

    OSi_CommonCallback: Symbol[
        Optional[list[int]],
        None,
    ]

    OSi_SendToPxi: Symbol[
        Optional[list[int]],
        None,
    ]

    OS_ResetSystem: Symbol[
        Optional[list[int]],
        None,
    ]

    OS_GetMacAddress: Symbol[
        Optional[list[int]],
        None,
    ]

    OS_GetOwnerInfo: Symbol[
        Optional[list[int]],
        None,
    ]

    CountLeadingZeros: Symbol[
        Optional[list[int]],
        None,
    ]

    OSi_InitVramExclusive: Symbol[
        Optional[list[int]],
        None,
    ]

    OSi_UnlockVram: Symbol[
        Optional[list[int]],
        None,
    ]

    OS_GetLowEntropyData: Symbol[
        Optional[list[int]],
        None,
    ]

    OS_Panic: Symbol[
        Optional[list[int]],
        None,
    ]

    OS_Halt: Symbol[
        Optional[list[int]],
        None,
    ]

    MI_SetWramBank: Symbol[
        Optional[list[int]],
        None,
    ]

    MI_DmaFill32: Symbol[
        Optional[list[int]],
        None,
    ]

    MI_DmaCopy32: Symbol[
        Optional[list[int]],
        None,
    ]

    MI_DmaCopy16: Symbol[
        Optional[list[int]],
        None,
    ]

    MI_DmaFill32Async: Symbol[
        Optional[list[int]],
        None,
    ]

    MI_DmaCopy32Async: Symbol[
        Optional[list[int]],
        None,
    ]

    MI_DmaSend32Async: Symbol[
        Optional[list[int]],
        None,
    ]

    MI_DmaCopy16Async: Symbol[
        Optional[list[int]],
        None,
    ]

    MI_DmaSend16Async: Symbol[
        Optional[list[int]],
        None,
    ]

    MI_IsDmaBusy: Symbol[
        Optional[list[int]],
        None,
    ]

    MI_WaitDma: Symbol[
        Optional[list[int]],
        None,
    ]

    MI_StopDma: Symbol[
        Optional[list[int]],
        None,
    ]

    MIi_CheckAnotherAutoDma: Symbol[
        Optional[list[int]],
        None,
    ]

    MIi_CheckDma0SourceAddress: Symbol[
        Optional[list[int]],
        None,
    ]

    ArrayFill16: Symbol[
        Optional[list[int]],
        None,
    ]

    ArrayCopy16: Symbol[
        Optional[list[int]],
        None,
    ]

    ArrayFill32: Symbol[
        Optional[list[int]],
        None,
    ]

    ArrayCopy32: Symbol[
        Optional[list[int]],
        None,
    ]

    ArrayFill32Fast: Symbol[
        Optional[list[int]],
        None,
    ]

    ArrayCopy32Fast: Symbol[
        Optional[list[int]],
        None,
    ]

    MemsetFast: Symbol[
        Optional[list[int]],
        None,
    ]

    MemcpyFast: Symbol[
        Optional[list[int]],
        None,
    ]

    AtomicExchange: Symbol[
        Optional[list[int]],
        None,
    ]

    MI_UncompressLZ8: Symbol[
        Optional[list[int]],
        None,
    ]

    MTi_CardDmaCopy32: Symbol[
        Optional[list[int]],
        None,
    ]

    MI_Init: Symbol[
        Optional[list[int]],
        None,
    ]

    Snd_StopSeq: Symbol[
        Optional[list[int]],
        None,
    ]

    Snd_PrepareSeq: Symbol[
        Optional[list[int]],
        None,
    ]

    Snd_StartPreparedSeq: Symbol[
        Optional[list[int]],
        None,
    ]

    Snd_SetPlayerTempoRatio: Symbol[
        Optional[list[int]],
        None,
    ]

    Snd_SetPlayerVolume: Symbol[
        Optional[list[int]],
        None,
    ]

    Snd_SetTrackPan: Symbol[
        Optional[list[int]],
        None,
    ]

    Snd_SetTrackAllocatableChannel: Symbol[
        Optional[list[int]],
        None,
    ]

    Snd_StartTimer: Symbol[
        Optional[list[int]],
        None,
    ]

    Snd_StopTimer: Symbol[
        Optional[list[int]],
        None,
    ]

    Snd_SetupCapture: Symbol[
        Optional[list[int]],
        None,
    ]

    Snd_SetupAlarm: Symbol[
        Optional[list[int]],
        None,
    ]

    Snd_LockChannel: Symbol[
        Optional[list[int]],
        None,
    ]

    Snd_UnlockChannel: Symbol[
        Optional[list[int]],
        None,
    ]

    Snd_SetChannelTimer: Symbol[
        Optional[list[int]],
        None,
    ]

    Snd_SetChannelVolume: Symbol[
        Optional[list[int]],
        None,
    ]

    Snd_SetChannelPan: Symbol[
        Optional[list[int]],
        None,
    ]

    Snd_SetupChannelPcm: Symbol[
        Optional[list[int]],
        None,
    ]

    Snd_SetupChannelPsg: Symbol[
        Optional[list[int]],
        None,
    ]

    Snd_SetupChannelNoise: Symbol[
        Optional[list[int]],
        None,
    ]

    Snd_InvalidateSeqData: Symbol[
        Optional[list[int]],
        None,
    ]

    Snd_InvalidateBankData: Symbol[
        Optional[list[int]],
        None,
    ]

    Snd_SetOutputSelector: Symbol[
        Optional[list[int]],
        None,
    ]

    Sndi_SetPlayerParam: Symbol[
        Optional[list[int]],
        None,
    ]

    Sndi_SetTrackParam: Symbol[
        Optional[list[int]],
        None,
    ]

    PushCommand_Impl: Symbol[
        Optional[list[int]],
        None,
    ]

    Snd_Init: Symbol[
        Optional[list[int]],
        None,
    ]

    Sndi_LockMutex: Symbol[
        Optional[list[int]],
        None,
    ]

    Sndi_UnlockMutex: Symbol[
        Optional[list[int]],
        None,
    ]

    Snd_CommandInit: Symbol[
        Optional[list[int]],
        None,
    ]

    Snd_RecvCommandReply: Symbol[
        Optional[list[int]],
        None,
    ]

    Snd_AllocCommand: Symbol[
        Optional[list[int]],
        None,
    ]

    Snd_PushCommand: Symbol[
        Optional[list[int]],
        None,
    ]

    Snd_FlushCommand: Symbol[
        Optional[list[int]],
        None,
    ]

    Snd_WaitForCommandProc: Symbol[
        Optional[list[int]],
        None,
    ]

    Snd_GetCurrentCommandTag: Symbol[
        Optional[list[int]],
        None,
    ]

    Snd_IsFinishedCommandTag: Symbol[
        Optional[list[int]],
        None,
    ]

    Snd_CountFreeCommand: Symbol[
        Optional[list[int]],
        None,
    ]

    Snd_CountReservedCommand: Symbol[
        Optional[list[int]],
        None,
    ]

    Snd_CountWaitingCommand: Symbol[
        Optional[list[int]],
        None,
    ]

    PxiFifoCallback: Symbol[
        Optional[list[int]],
        None,
    ]

    InitPxi: Symbol[
        Optional[list[int]],
        None,
    ]

    RequestCommandProc: Symbol[
        Optional[list[int]],
        None,
    ]

    AllocCommand: Symbol[
        Optional[list[int]],
        None,
    ]

    IsCommandAvailable: Symbol[
        Optional[list[int]],
        None,
    ]

    Snd_AlarmInit: Symbol[
        Optional[list[int]],
        None,
    ]

    Sndi_IncAlarmId: Symbol[
        Optional[list[int]],
        None,
    ]

    Sndi_SetAlarmHandler: Symbol[
        Optional[list[int]],
        None,
    ]

    Sndi_CallAlarmHandler: Symbol[
        Optional[list[int]],
        None,
    ]

    Snd_GetPlayerStatus: Symbol[
        Optional[list[int]],
        None,
    ]

    Snd_GetChannelStatus: Symbol[
        Optional[list[int]],
        None,
    ]

    Sndi_GetFinishedCommandTag: Symbol[
        Optional[list[int]],
        None,
    ]

    Sndi_InitSharedWork: Symbol[
        Optional[list[int]],
        None,
    ]

    Snd_CalcChannelVolume: Symbol[
        Optional[list[int]],
        None,
    ]

    Snd_AssignWaveArc: Symbol[
        Optional[list[int]],
        None,
    ]

    Snd_DestroyBank: Symbol[
        Optional[list[int]],
        None,
    ]

    Snd_DestroyWaveArc: Symbol[
        Optional[list[int]],
        None,
    ]

    Snd_GetFirstInstDataPos: Symbol[
        Optional[list[int]],
        None,
    ]

    Snd_GetNextInstData: Symbol[
        Optional[list[int]],
        None,
    ]

    Snd_GetWaveDataCount: Symbol[
        Optional[list[int]],
        None,
    ]

    Snd_SetWaveDataAddress: Symbol[
        Optional[list[int]],
        None,
    ]

    Snd_GetWaveDataAddress: Symbol[
        Optional[list[int]],
        None,
    ]

    Pxi_Init: Symbol[
        Optional[list[int]],
        None,
    ]

    Pxi_InitFifo: Symbol[
        Optional[list[int]],
        None,
    ]

    Pxi_SetFifoRecvCallback: Symbol[
        Optional[list[int]],
        None,
    ]

    Pxi_IsCallbackReady: Symbol[
        Optional[list[int]],
        None,
    ]

    Pxi_SendWordByFifo: Symbol[
        Optional[list[int]],
        None,
    ]

    Pxii_HandlerRecvFifoNotEmpty: Symbol[
        Optional[list[int]],
        None,
    ]

    FSi_ReleaseCommand: Symbol[
        Optional[list[int]],
        None,
    ]

    FSi_TranslateCommand: Symbol[
        Optional[list[int]],
        None,
    ]

    FSi_StrNiCmp: Symbol[
        Optional[list[int]],
        None,
    ]

    FSi_ReadTable: Symbol[
        Optional[list[int]],
        None,
    ]

    FSi_SeekDirDirect: Symbol[
        Optional[list[int]],
        None,
    ]

    FSi_ReadFileCommand: Symbol[
        Optional[list[int]],
        None,
    ]

    FSi_WriteFileCommand: Symbol[
        Optional[list[int]],
        None,
    ]

    FSi_SeekDirCommand: Symbol[
        Optional[list[int]],
        None,
    ]

    FSi_ReadDirCommand: Symbol[
        Optional[list[int]],
        None,
    ]

    FSi_FindPathCommand: Symbol[
        Optional[list[int]],
        None,
    ]

    FSi_GetPathCommand: Symbol[
        Optional[list[int]],
        None,
    ]

    FSi_OpenFileFastCommand: Symbol[
        Optional[list[int]],
        None,
    ]

    FSi_OpenFileDirectCommand: Symbol[
        Optional[list[int]],
        None,
    ]

    FSi_CloseFileCommand: Symbol[
        Optional[list[int]],
        None,
    ]

    FSi_GetPackedName: Symbol[
        Optional[list[int]],
        None,
    ]

    FSi_ReadMemCallback: Symbol[
        Optional[list[int]],
        None,
    ]

    FSi_WriteMemCallback: Symbol[
        Optional[list[int]],
        None,
    ]

    FSi_ReadMemoryCore: Symbol[
        Optional[list[int]],
        None,
    ]

    FSi_NextCommand: Symbol[
        Optional[list[int]],
        None,
    ]

    FSi_ExecuteAsyncCommand: Symbol[
        Optional[list[int]],
        None,
    ]

    FSi_ExecuteSyncCommand: Symbol[
        Optional[list[int]],
        None,
    ]

    FSi_SendCommand: Symbol[
        Optional[list[int]],
        None,
    ]

    FS_InitArchive: Symbol[
        Optional[list[int]],
        None,
    ]

    FS_FindArchive: Symbol[
        Optional[list[int]],
        None,
    ]

    FS_RegisterArchiveName: Symbol[
        Optional[list[int]],
        None,
    ]

    FS_ReleaseArchiveName: Symbol[
        Optional[list[int]],
        None,
    ]

    FS_LoadArchive: Symbol[
        Optional[list[int]],
        None,
    ]

    FS_UnloadArchive: Symbol[
        Optional[list[int]],
        None,
    ]

    FS_LoadArchiveTables: Symbol[
        Optional[list[int]],
        None,
    ]

    FS_UnloadArchiveTables: Symbol[
        Optional[list[int]],
        None,
    ]

    FS_SuspendArchive: Symbol[
        Optional[list[int]],
        None,
    ]

    FS_ResumeArchive: Symbol[
        Optional[list[int]],
        None,
    ]

    FS_SetArchiveProc: Symbol[
        Optional[list[int]],
        None,
    ]

    FS_NotifyArchiveAsyncEnd: Symbol[
        Optional[list[int]],
        None,
    ]

    FS_Init: Symbol[
        Optional[list[int]],
        None,
    ]

    FS_InitFile: Symbol[
        Optional[list[int]],
        None,
    ]

    FSi_FindPath: Symbol[
        Optional[list[int]],
        None,
    ]

    FSi_ReadFileCore: Symbol[
        Optional[list[int]],
        None,
    ]

    FS_ConvertPathToFileID: Symbol[
        Optional[list[int]],
        None,
    ]

    FS_OpenFileDirect: Symbol[
        Optional[list[int]],
        None,
    ]

    FS_OpenFileFast: Symbol[
        Optional[list[int]],
        None,
    ]

    FS_OpenFile: Symbol[
        Optional[list[int]],
        None,
    ]

    FS_CloseFile: Symbol[
        Optional[list[int]],
        None,
    ]

    FS_WaitAsync: Symbol[
        Optional[list[int]],
        None,
    ]

    FS_ReadFileAsync: Symbol[
        Optional[list[int]],
        None,
    ]

    FS_ReadFile: Symbol[
        Optional[list[int]],
        None,
    ]

    FS_SeekFile: Symbol[
        Optional[list[int]],
        None,
    ]

    FS_ChangeDir: Symbol[
        Optional[list[int]],
        None,
    ]

    FSi_OnRomReadDone: Symbol[
        Optional[list[int]],
        None,
    ]

    FSi_ReadRomCallback: Symbol[
        Optional[list[int]],
        None,
    ]

    FSi_WriteDummyCallback: Symbol[
        Optional[list[int]],
        None,
    ]

    FSi_RomArchiveProc: Symbol[
        Optional[list[int]],
        None,
    ]

    FSi_ReadDummyCallback: Symbol[
        Optional[list[int]],
        None,
    ]

    FSi_EmptyArchiveProc: Symbol[
        Optional[list[int]],
        None,
    ]

    FSi_InitRom: Symbol[
        Optional[list[int]],
        None,
    ]

    FSi_GetOverlayBinarySize: Symbol[
        Optional[list[int]],
        None,
    ]

    FS_ClearOverlayImage: Symbol[
        Optional[list[int]],
        None,
    ]

    FS_GetOverlayFileID: Symbol[
        Optional[list[int]],
        None,
    ]

    FSi_LoadOverlayInfoCore: Symbol[
        Optional[list[int]],
        None,
    ]

    FS_LoadOverlayInfo: Symbol[
        Optional[list[int]],
        None,
    ]

    FS_LoadOverlayImageAsync: Symbol[
        Optional[list[int]],
        None,
    ]

    FSi_CompareDigest: Symbol[
        Optional[list[int]],
        None,
    ]

    FS_StartOverlay: Symbol[
        Optional[list[int]],
        None,
    ]

    FS_EndOverlay: Symbol[
        Optional[list[int]],
        None,
    ]

    FS_UnloadOverlayImage: Symbol[
        Optional[list[int]],
        None,
    ]

    FS_UnloadOverlay: Symbol[
        Optional[list[int]],
        None,
    ]

    MD5_Init: Symbol[
        Optional[list[int]],
        None,
    ]

    MD5_Update: Symbol[
        Optional[list[int]],
        None,
    ]

    MD5_Digest: Symbol[
        Optional[list[int]],
        None,
    ]

    MD5_Transform: Symbol[
        Optional[list[int]],
        None,
    ]

    Dgt_Hash2Init: Symbol[
        Optional[list[int]],
        None,
    ]

    Dgt_Hash2Update: Symbol[
        Optional[list[int]],
        None,
    ]

    Dgt_Hash2GetHash: Symbol[
        Optional[list[int]],
        None,
    ]

    Dgt_Hash2CalcHmac: Symbol[
        Optional[list[int]],
        None,
    ]

    Dgti_CalcHmac: Symbol[
        Optional[list[int]],
        None,
    ]

    Dgt_Hash2Transform: Symbol[
        Optional[list[int]],
        None,
    ]

    CP_SaveContext: Symbol[
        Optional[list[int]],
        None,
    ]

    CPi_RestoreContext: Symbol[
        Optional[list[int]],
        None,
    ]

    TPi_TpCallback: Symbol[
        Optional[list[int]],
        None,
    ]

    TP_Init: Symbol[
        Optional[list[int]],
        None,
    ]

    TP_GetUserInfo: Symbol[
        Optional[list[int]],
        None,
    ]

    TP_SetCalibrateParam: Symbol[
        Optional[list[int]],
        None,
    ]

    TP_RequestSamplingAsync: Symbol[
        Optional[list[int]],
        None,
    ]

    TP_GetCalibratedResult: Symbol[
        Optional[list[int]],
        None,
    ]

    TP_WaitCalibratedResult: Symbol[
        Optional[list[int]],
        None,
    ]

    TP_RequestAutoSamplingStartAsync: Symbol[
        Optional[list[int]],
        None,
    ]

    TP_GetLatestIndexInAuto: Symbol[
        Optional[list[int]],
        None,
    ]

    TP_CalcCalibrateParam: Symbol[
        Optional[list[int]],
        None,
    ]

    TP_GetCalibratedPoint: Symbol[
        Optional[list[int]],
        None,
    ]

    TP_WaitBusy: Symbol[
        Optional[list[int]],
        None,
    ]

    TP_CheckBusy: Symbol[
        Optional[list[int]],
        None,
    ]

    PMi_Lock: Symbol[
        Optional[list[int]],
        None,
    ]

    PMi_WaitBusy: Symbol[
        Optional[list[int]],
        None,
    ]

    PMi_DummyCallback: Symbol[
        Optional[list[int]],
        None,
    ]

    PMi_CallCallbackAndUnlock: Symbol[
        Optional[list[int]],
        None,
    ]

    PM_Init: Symbol[
        Optional[list[int]],
        None,
    ]

    PMi_CommonCallback: Symbol[
        Optional[list[int]],
        None,
    ]

    PMi_SendSleepStart: Symbol[
        Optional[list[int]],
        None,
    ]

    PM_SendUtilityCommandAsync: Symbol[
        Optional[list[int]],
        None,
    ]

    PMi_ReadRegisterAsync: Symbol[
        Optional[list[int]],
        None,
    ]

    PMi_ReadRegister: Symbol[
        Optional[list[int]],
        None,
    ]

    PMi_WriteRegisterAsync: Symbol[
        Optional[list[int]],
        None,
    ]

    PMi_WriteRegister: Symbol[
        Optional[list[int]],
        None,
    ]

    PMi_SetLedAsync: Symbol[
        Optional[list[int]],
        None,
    ]

    PMi_SetLed: Symbol[
        Optional[list[int]],
        None,
    ]

    PM_SetBackLightAsync: Symbol[
        Optional[list[int]],
        None,
    ]

    PM_SetBackLight: Symbol[
        Optional[list[int]],
        None,
    ]

    PM_ForceToPowerOffAsync: Symbol[
        Optional[list[int]],
        None,
    ]

    PM_ForceToPowerOff: Symbol[
        Optional[list[int]],
        None,
    ]

    PMi_SetAmp: Symbol[
        Optional[list[int]],
        None,
    ]

    PM_GetBackLight: Symbol[
        Optional[list[int]],
        None,
    ]

    PMi_SendPxiData: Symbol[
        Optional[list[int]],
        None,
    ]

    PMi_SetLcdPower: Symbol[
        Optional[list[int]],
        None,
    ]

    PM_SetLcdPower: Symbol[
        Optional[list[int]],
        None,
    ]

    PM_GetLcdPower: Symbol[
        Optional[list[int]],
        None,
    ]

    PMi_SendLedPatternCommandAsync: Symbol[
        Optional[list[int]],
        None,
    ]

    PMi_SendLedPatternCommand: Symbol[
        Optional[list[int]],
        None,
    ]

    PM_GetLedPatternAsync: Symbol[
        Optional[list[int]],
        None,
    ]

    PM_GetLedPattern: Symbol[
        Optional[list[int]],
        None,
    ]

    PMi_PrependList: Symbol[
        Optional[list[int]],
        None,
    ]

    PMi_AppendList: Symbol[
        Optional[list[int]],
        None,
    ]

    PMi_DeleteList: Symbol[
        Optional[list[int]],
        None,
    ]

    PMi_ExecuteList: Symbol[
        Optional[list[int]],
        None,
    ]

    PM_PrependPreSleepCallback: Symbol[
        Optional[list[int]],
        None,
    ]

    PM_AppendPostSleepCallback: Symbol[
        Optional[list[int]],
        None,
    ]

    PM_DeletePreSleepCallback: Symbol[
        Optional[list[int]],
        None,
    ]

    PM_DeletePostSleepCallback: Symbol[
        Optional[list[int]],
        None,
    ]

    Rtc_Init: Symbol[
        Optional[list[int]],
        None,
    ]

    Rtc_GetDateAsync: Symbol[
        Optional[list[int]],
        None,
    ]

    Rtc_GetDate: Symbol[
        Optional[list[int]],
        None,
    ]

    Rtc_GetTimeAsync: Symbol[
        Optional[list[int]],
        None,
    ]

    Rtc_GetTime: Symbol[
        Optional[list[int]],
        None,
    ]

    Rtc_GetDateTimeAsync: Symbol[
        Optional[list[int]],
        None,
    ]

    Rtc_GetDateTime: Symbol[
        Optional[list[int]],
        None,
    ]

    RtcCommonCallback: Symbol[
        Optional[list[int]],
        None,
    ]

    RtcBcd2Hex: Symbol[
        Optional[list[int]],
        None,
    ]

    RtcGetResultCallback: Symbol[
        Optional[list[int]],
        None,
    ]

    RtcWaitBusy: Symbol[
        Optional[list[int]],
        None,
    ]

    Rtci_ReadRawDateTimeAsync: Symbol[
        Optional[list[int]],
        None,
    ]

    Rtci_ReadRawDateAsync: Symbol[
        Optional[list[int]],
        None,
    ]

    Rtci_ReadRawTimeAsync: Symbol[
        Optional[list[int]],
        None,
    ]

    Rtci_WriteRawStatus2Async: Symbol[
        Optional[list[int]],
        None,
    ]

    RtcSendPxiCommand: Symbol[
        Optional[list[int]],
        None,
    ]

    Rtc_ConvertDateToDay: Symbol[
        Optional[list[int]],
        None,
    ]

    Rtci_ConvertTimeToSecond: Symbol[
        Optional[list[int]],
        None,
    ]

    Rtc_ConvertDateTimeToSecond: Symbol[
        Optional[list[int]],
        None,
    ]

    Rtc_GetDayOfWeek: Symbol[
        Optional[list[int]],
        None,
    ]

    Cardi_SetTask: Symbol[
        Optional[list[int]],
        None,
    ]

    Cardi_LockResource: Symbol[
        Optional[list[int]],
        None,
    ]

    Cardi_UnlockResource: Symbol[
        Optional[list[int]],
        None,
    ]

    Cardi_InitCommon: Symbol[
        Optional[list[int]],
        None,
    ]

    Card_IsEnabled: Symbol[
        Optional[list[int]],
        None,
    ]

    Card_CheckEnabled: Symbol[
        Optional[list[int]],
        None,
    ]

    Card_Enable: Symbol[
        Optional[list[int]],
        None,
    ]

    Cardi_WaitAsync: Symbol[
        Optional[list[int]],
        None,
    ]

    Cardi_TryWaitAsync: Symbol[
        Optional[list[int]],
        None,
    ]

    Card_SetThreadPriority: Symbol[
        Optional[list[int]],
        None,
    ]

    Card_LockRom: Symbol[
        Optional[list[int]],
        None,
    ]

    Card_UnlockRom: Symbol[
        Optional[list[int]],
        None,
    ]

    Card_LockBackup: Symbol[
        Optional[list[int]],
        None,
    ]

    Card_UnlockBackup: Symbol[
        Optional[list[int]],
        None,
    ]

    Cardi_IdentifyBackupCore: Symbol[
        Optional[list[int]],
        None,
    ]

    Cardi_RequestStreamCommandCore: Symbol[
        Optional[list[int]],
        None,
    ]

    Cardi_RequestStreamCommand: Symbol[
        Optional[list[int]],
        None,
    ]

    Card_GetCurrentBackupType: Symbol[
        Optional[list[int]],
        None,
    ]

    Card_GetBackupTotalSize: Symbol[
        Optional[list[int]],
        None,
    ]

    Card_GetBackupSectorSize: Symbol[
        Optional[list[int]],
        None,
    ]

    Card_IdentifyBackup: Symbol[
        Optional[list[int]],
        None,
    ]

    Card_WaitBackupAsync: Symbol[
        Optional[list[int]],
        None,
    ]

    Card_TryWaitBackupAsync: Symbol[
        Optional[list[int]],
        None,
    ]

    Cardi_ReadFromCache: Symbol[
        Optional[list[int]],
        None,
    ]

    Cardi_SetRomOp: Symbol[
        Optional[list[int]],
        None,
    ]

    Cardi_TryReadCardDma: Symbol[
        Optional[list[int]],
        None,
    ]

    Cardi_ReadCard: Symbol[
        Optional[list[int]],
        None,
    ]

    Cardi_ReadRomSyncCore: Symbol[
        Optional[list[int]],
        None,
    ]

    Cardi_ReadRom: Symbol[
        Optional[list[int]],
        None,
    ]

    Card_Init: Symbol[
        Optional[list[int]],
        None,
    ]

    Card_WaitRomAsync: Symbol[
        Optional[list[int]],
        None,
    ]

    Cardi_GetRomAccessor: Symbol[
        Optional[list[int]],
        None,
    ]

    Cardi_OnFifoRecv: Symbol[
        Optional[list[int]],
        None,
    ]

    Cardi_TaskThread: Symbol[
        Optional[list[int]],
        None,
    ]

    Cardi_Request: Symbol[
        Optional[list[int]],
        None,
    ]

    Card_InitPulledOutCallback: Symbol[
        Optional[list[int]],
        None,
    ]

    Cardi_PulledOutCallback: Symbol[
        Optional[list[int]],
        None,
    ]

    Card_SetPulledOutCallback: Symbol[
        Optional[list[int]],
        None,
    ]

    Card_IsPulledOut: Symbol[
        Optional[list[int]],
        None,
    ]

    Card_TerminateForPulledOut: Symbol[
        Optional[list[int]],
        None,
    ]

    Cardi_CheckPulledOutCore: Symbol[
        Optional[list[int]],
        None,
    ]

    Cardi_SendtoPxi: Symbol[
        Optional[list[int]],
        None,
    ]

    Ctrdgi_InitCommon: Symbol[
        Optional[list[int]],
        None,
    ]

    Ctrdg_IsOptionCartridge: Symbol[
        Optional[list[int]],
        None,
    ]

    Ctrdgi_IsAgbCartridgeAtInit: Symbol[
        Optional[list[int]],
        None,
    ]

    Ctrdg_IsExisting: Symbol[
        Optional[list[int]],
        None,
    ]

    Ctrdgi_ChangeLatestAccessCycle: Symbol[
        Optional[list[int]],
        None,
    ]

    Ctrdgi_RestoreAccessCycle: Symbol[
        Optional[list[int]],
        None,
    ]

    Ctrdgi_LockByProcessor: Symbol[
        Optional[list[int]],
        None,
    ]

    Ctrdgi_UnlockByProcessor: Symbol[
        Optional[list[int]],
        None,
    ]

    Ctrdgi_SendtoPxi: Symbol[
        Optional[list[int]],
        None,
    ]

    Ctrdg_Enable: Symbol[
        Optional[list[int]],
        None,
    ]

    Ctrdg_Init: Symbol[
        Optional[list[int]],
        None,
    ]

    Ctrdgi_InitModuleInfo: Symbol[
        Optional[list[int]],
        None,
    ]

    Ctrdgi_CallbackForInitModuleInfo: Symbol[
        Optional[list[int]],
        None,
    ]

    Ctrdgi_PulledOutCallback: Symbol[
        Optional[list[int]],
        None,
    ]

    Ctrdg_TerminateForPulledOut: Symbol[
        Optional[list[int]],
        None,
    ]

    Ctrdgi_CallbackForSetPhi: Symbol[
        Optional[list[int]],
        None,
    ]

    Ctrdgi_InitTaskThread: Symbol[
        Optional[list[int]],
        None,
    ]

    Ctrdgi_InitTaskInfo: Symbol[
        Optional[list[int]],
        None,
    ]

    Ctrdgi_TaskThread: Symbol[
        Optional[list[int]],
        None,
    ]

    Math_CountPopulation: Symbol[
        Optional[list[int]],
        None,
    ]

    Math_CalcSha1: Symbol[
        Optional[list[int]],
        None,
    ]

    Mathi_Crc8InitTable: Symbol[
        Optional[list[int]],
        None,
    ]

    Mathi_Crc8Update: Symbol[
        Optional[list[int]],
        None,
    ]

    Mathi_Crc16InitTable: Symbol[
        Optional[list[int]],
        None,
    ]

    Mathi_Crc16Update: Symbol[
        Optional[list[int]],
        None,
    ]

    Mathi_Crc32InitTable: Symbol[
        Optional[list[int]],
        None,
    ]

    Mathi_Crc32Update: Symbol[
        Optional[list[int]],
        None,
    ]

    Math_CalcCrc8: Symbol[
        Optional[list[int]],
        None,
    ]

    Math_CalcCrc16: Symbol[
        Optional[list[int]],
        None,
    ]

    Math_CalcCrc32: Symbol[
        Optional[list[int]],
        None,
    ]

    Std_CopyLString: Symbol[
        Optional[list[int]],
        None,
    ]

    Std_GetStringLength: Symbol[
        Optional[list[int]],
        None,
    ]

    Std_CompareString: Symbol[
        Optional[list[int]],
        None,
    ]

    Std_CompareNString: Symbol[
        Optional[list[int]],
        None,
    ]

    Std_TsScanf: Symbol[
        Optional[list[int]],
        None,
    ]

    Stdi_IsSpace: Symbol[
        Optional[list[int]],
        None,
    ]

    Stdi_FillBitset: Symbol[
        Optional[list[int]],
        None,
    ]

    Std_TvsScanf: Symbol[
        Optional[list[int]],
        None,
    ]

    string_put_char: Symbol[
        Optional[list[int]],
        None,
    ]

    string_fill_char: Symbol[
        Optional[list[int]],
        None,
    ]

    string_put_string: Symbol[
        Optional[list[int]],
        None,
    ]

    OS_VsNPrintfEx: Symbol[
        Optional[list[int]],
        None,
    ]

    NotANumber: Symbol[
        Optional[list[int]],
        None,
    ]

    _flush_line_buffered_output_files: Symbol[
        Optional[list[int]],
        None,
    ]

    _flush_all: Symbol[
        Optional[list[int]],
        None,
    ]

    abs: Symbol[
        Optional[list[int]],
        None,
    ]

    _convert_from_newlines: Symbol[
        Optional[list[int]],
        None,
    ]

    _convert_to_newlines: Symbol[
        Optional[list[int]],
        None,
    ]

    _prep_buffer: Symbol[
        Optional[list[int]],
        None,
    ]

    _load_buffer: Symbol[
        Optional[list[int]],
        None,
    ]

    _flush_buffer: Symbol[
        Optional[list[int]],
        None,
    ]

    fread: Symbol[
        Optional[list[int]],
        None,
    ]

    _fread: Symbol[
        Optional[list[int]],
        None,
    ]

    fclose: Symbol[
        Optional[list[int]],
        None,
    ]

    fflush: Symbol[
        Optional[list[int]],
        None,
    ]

    _msl_strnicmp: Symbol[
        Optional[list[int]],
        None,
    ]

    _ftell: Symbol[
        Optional[list[int]],
        None,
    ]

    ftell: Symbol[
        Optional[list[int]],
        None,
    ]

    _fseek: Symbol[
        Optional[list[int]],
        None,
    ]

    fseek: Symbol[
        Optional[list[int]],
        None,
    ]

    rewind: Symbol[
        Optional[list[int]],
        None,
    ]

    _mbtowc_noconv: Symbol[
        Optional[list[int]],
        None,
    ]

    _wctomb_noconv: Symbol[
        Optional[list[int]],
        None,
    ]

    wctomb: Symbol[
        Optional[list[int]],
        None,
    ]

    wcstombs: Symbol[
        Optional[list[int]],
        None,
    ]

    memcpy: Symbol[
        Optional[list[int]],
        None,
    ]

    memmove: Symbol[
        Optional[list[int]],
        None,
    ]

    memset: Symbol[
        Optional[list[int]],
        None,
    ]

    memchr: Symbol[
        Optional[list[int]],
        None,
    ]

    memcmp: Symbol[
        Optional[list[int]],
        None,
    ]

    _fill_mem: Symbol[
        Optional[list[int]],
        None,
    ]

    parse_format: Symbol[
        Optional[list[int]],
        None,
    ]

    long2str: Symbol[
        Optional[list[int]],
        None,
    ]

    longlong2str: Symbol[
        Optional[list[int]],
        None,
    ]

    double2hex: Symbol[
        Optional[list[int]],
        None,
    ]

    round_decimal: Symbol[
        Optional[list[int]],
        None,
    ]

    float2str: Symbol[
        Optional[list[int]],
        None,
    ]

    __vsprintf_internal_slice: Symbol[
        Optional[list[int]],
        None,
    ]

    TryAppendToSlice: Symbol[
        Optional[list[int]],
        None,
    ]

    __vsprintf_internal: Symbol[
        Optional[list[int]],
        None,
    ]

    vsprintf: Symbol[
        Optional[list[int]],
        None,
    ]

    snprintf: Symbol[
        Optional[list[int]],
        None,
    ]

    sprintf: Symbol[
        Optional[list[int]],
        None,
    ]

    rand: Symbol[
        Optional[list[int]],
        None,
    ]

    srand: Symbol[
        Optional[list[int]],
        None,
    ]

    strlen: Symbol[
        Optional[list[int]],
        None,
    ]

    strcpy: Symbol[
        Optional[list[int]],
        None,
    ]

    strncpy: Symbol[
        Optional[list[int]],
        None,
    ]

    strcat: Symbol[
        Optional[list[int]],
        None,
    ]

    strncat: Symbol[
        Optional[list[int]],
        None,
    ]

    strcmp: Symbol[
        Optional[list[int]],
        None,
    ]

    strncmp: Symbol[
        Optional[list[int]],
        None,
    ]

    strchr: Symbol[
        Optional[list[int]],
        None,
    ]

    strcspn: Symbol[
        Optional[list[int]],
        None,
    ]

    strstr: Symbol[
        Optional[list[int]],
        None,
    ]

    _strtold: Symbol[
        Optional[list[int]],
        None,
    ]

    strtold: Symbol[
        Optional[list[int]],
        None,
    ]

    atof: Symbol[
        Optional[list[int]],
        None,
    ]

    _strtoul: Symbol[
        Optional[list[int]],
        None,
    ]

    strtoul: Symbol[
        Optional[list[int]],
        None,
    ]

    strtol: Symbol[
        Optional[list[int]],
        None,
    ]

    atoi: Symbol[
        Optional[list[int]],
        None,
    ]

    fwide: Symbol[
        Optional[list[int]],
        None,
    ]

    wcslen: Symbol[
        Optional[list[int]],
        None,
    ]

    fabs: Symbol[
        Optional[list[int]],
        None,
    ]

    _num2dec: Symbol[
        Optional[list[int]],
        None,
    ]

    _dec2num: Symbol[
        Optional[list[int]],
        None,
    ]

    strcasecmp: Symbol[
        Optional[list[int]],
        None,
    ]

    _dadd: Symbol[
        Optional[list[int]],
        None,
    ]

    _d2f: Symbol[
        Optional[list[int]],
        None,
    ]

    _ll_ufrom_d: Symbol[
        Optional[list[int]],
        None,
    ]

    _dflt: Symbol[
        Optional[list[int]],
        None,
    ]

    _dfltu: Symbol[
        Optional[list[int]],
        None,
    ]

    _dmul: Symbol[
        Optional[list[int]],
        None,
    ]

    _dsqrt: Symbol[
        Optional[list[int]],
        None,
    ]

    _dsub: Symbol[
        Optional[list[int]],
        None,
    ]

    _fadd: Symbol[
        Optional[list[int]],
        None,
    ]

    _dgr: Symbol[
        Optional[list[int]],
        None,
    ]

    _dleq: Symbol[
        Optional[list[int]],
        None,
    ]

    _dls: Symbol[
        Optional[list[int]],
        None,
    ]

    _deq: Symbol[
        Optional[list[int]],
        None,
    ]

    _dneq: Symbol[
        Optional[list[int]],
        None,
    ]

    _fls: Symbol[
        Optional[list[int]],
        None,
    ]

    _fdiv: Symbol[
        Optional[list[int]],
        None,
    ]

    _f2d: Symbol[
        Optional[list[int]],
        None,
    ]

    _ffix: Symbol[
        Optional[list[int]],
        None,
    ]

    _fflt: Symbol[
        Optional[list[int]],
        None,
    ]

    _ffltu: Symbol[
        Optional[list[int]],
        None,
    ]

    _fmul: Symbol[
        Optional[list[int]],
        None,
    ]

    sqrtf: Symbol[
        Optional[list[int]],
        None,
    ]

    _fsub: Symbol[
        Optional[list[int]],
        None,
    ]

    _ll_mod: Symbol[
        Optional[list[int]],
        None,
    ]

    _ll_sdiv: Symbol[
        Optional[list[int]],
        None,
    ]

    _ll_udiv: Symbol[
        Optional[list[int]],
        None,
    ]

    _ull_mod: Symbol[
        Optional[list[int]],
        None,
    ]

    _ll_mul: Symbol[
        Optional[list[int]],
        None,
    ]

    _s32_div_f: Symbol[
        Optional[list[int]],
        None,
    ]

    _u32_div_f: Symbol[
        Optional[list[int]],
        None,
    ]

    _u32_div_not_0_f: Symbol[
        Optional[list[int]],
        None,
    ]

    _drdiv: Symbol[
        Optional[list[int]],
        None,
    ]

    _ddiv: Symbol[
        Optional[list[int]],
        None,
    ]

    _fp_init: Symbol[
        Optional[list[int]],
        None,
    ]

    _call_static_initializers: Symbol[
        Optional[list[int]],
        None,
    ]


class LibsDataProtocol(Protocol):

    ANSI_C_LCG_MULTIPLIER: Symbol[
        Optional[list[int]],
        None,
    ]

    RAND_MAX: Symbol[
        Optional[list[int]],
        None,
    ]


LibsProtocol = SectionProtocol[
    LibsFunctionsProtocol,
    LibsDataProtocol,
    Optional[int],
]


class Move_effectsFunctionsProtocol(Protocol):

    DoMoveDamage: Symbol[
        Optional[list[int]],
        None,
    ]

    DoMoveIronTail: Symbol[
        Optional[list[int]],
        None,
    ]

    DoMoveDamageMultihitUntilMiss: Symbol[
        Optional[list[int]],
        None,
    ]

    DoMoveYawn: Symbol[
        Optional[list[int]],
        None,
    ]

    DoMoveSleep: Symbol[
        Optional[list[int]],
        None,
    ]

    DoMoveNightmare: Symbol[
        Optional[list[int]],
        None,
    ]

    DoMoveMorningSun: Symbol[
        Optional[list[int]],
        None,
    ]

    DoMoveVitalThrow: Symbol[
        Optional[list[int]],
        None,
    ]

    DoMoveDig: Symbol[
        Optional[list[int]],
        None,
    ]

    DoMoveSweetScent: Symbol[
        Optional[list[int]],
        None,
    ]

    DoMoveCharm: Symbol[
        Optional[list[int]],
        None,
    ]

    DoMoveRainDance: Symbol[
        Optional[list[int]],
        None,
    ]

    DoMoveHail: Symbol[
        Optional[list[int]],
        None,
    ]

    DoMoveHealStatus: Symbol[
        Optional[list[int]],
        None,
    ]

    DoMoveBubble: Symbol[
        Optional[list[int]],
        None,
    ]

    DoMoveEncore: Symbol[
        Optional[list[int]],
        None,
    ]

    DoMoveRage: Symbol[
        Optional[list[int]],
        None,
    ]

    DoMoveSuperFang: Symbol[
        Optional[list[int]],
        None,
    ]

    DoMovePainSplit: Symbol[
        Optional[list[int]],
        None,
    ]

    DoMoveTorment: Symbol[
        Optional[list[int]],
        None,
    ]

    DoMoveStringShot: Symbol[
        Optional[list[int]],
        None,
    ]

    DoMoveSwagger: Symbol[
        Optional[list[int]],
        None,
    ]

    DoMoveSnore: Symbol[
        Optional[list[int]],
        None,
    ]

    DoMoveScreech: Symbol[
        Optional[list[int]],
        None,
    ]

    DoMoveDamageCringe30: Symbol[
        Optional[list[int]],
        None,
    ]

    DoMoveWeatherBall: Symbol[
        Optional[list[int]],
        None,
    ]

    DoMoveWhirlpool: Symbol[
        Optional[list[int]],
        None,
    ]

    DoMoveFakeTears: Symbol[
        Optional[list[int]],
        None,
    ]

    DoMoveSpite: Symbol[
        Optional[list[int]],
        None,
    ]

    DoMoveFocusEnergy: Symbol[
        Optional[list[int]],
        None,
    ]

    DoMoveSmokescreen: Symbol[
        Optional[list[int]],
        None,
    ]

    DoMoveMirrorMove: Symbol[
        Optional[list[int]],
        None,
    ]

    DoMoveOverheat: Symbol[
        Optional[list[int]],
        None,
    ]

    DoMoveAuroraBeam: Symbol[
        Optional[list[int]],
        None,
    ]

    DoMoveMemento: Symbol[
        Optional[list[int]],
        None,
    ]

    DoMoveOctazooka: Symbol[
        Optional[list[int]],
        None,
    ]

    DoMoveFlatter: Symbol[
        Optional[list[int]],
        None,
    ]

    DoMoveWillOWisp: Symbol[
        Optional[list[int]],
        None,
    ]

    DoMoveReturn: Symbol[
        Optional[list[int]],
        None,
    ]

    DoMoveGrudge: Symbol[
        Optional[list[int]],
        None,
    ]

    DoMoveCounter: Symbol[
        Optional[list[int]],
        None,
    ]

    DoMoveDamageBurn10FlameWheel: Symbol[
        Optional[list[int]],
        None,
    ]

    DoMoveDamageBurn10: Symbol[
        Optional[list[int]],
        None,
    ]

    DoMoveExpose: Symbol[
        Optional[list[int]],
        None,
    ]

    DoMoveDoubleTeam: Symbol[
        Optional[list[int]],
        None,
    ]

    DoMoveGust: Symbol[
        Optional[list[int]],
        None,
    ]

    DoMoveBoostDefense1: Symbol[
        Optional[list[int]],
        None,
    ]

    DoMoveParalyze: Symbol[
        Optional[list[int]],
        None,
    ]

    DoMoveBoostAttack1: Symbol[
        Optional[list[int]],
        None,
    ]

    DoMoveRazorWind: Symbol[
        Optional[list[int]],
        None,
    ]

    DoMoveBide: Symbol[
        Optional[list[int]],
        None,
    ]

    DoMoveBideUnleash: Symbol[
        Optional[list[int]],
        None,
    ]

    DoMoveCrunch: Symbol[
        Optional[list[int]],
        None,
    ]

    DoMoveDamageCringe20: Symbol[
        Optional[list[int]],
        None,
    ]

    DoMoveDamageParalyze20: Symbol[
        Optional[list[int]],
        None,
    ]

    DoMoveEndeavor: Symbol[
        Optional[list[int]],
        None,
    ]

    DoMoveFacade: Symbol[
        Optional[list[int]],
        None,
    ]

    DoMoveDamageLowerSpeed20: Symbol[
        Optional[list[int]],
        None,
    ]

    DoMoveBrickBreak: Symbol[
        Optional[list[int]],
        None,
    ]

    DoMoveDamageLowerSpeed100: Symbol[
        Optional[list[int]],
        None,
    ]

    DoMoveFocusPunch: Symbol[
        Optional[list[int]],
        None,
    ]

    DoMoveDamageDrain: Symbol[
        Optional[list[int]],
        None,
    ]

    DoMoveReversal: Symbol[
        Optional[list[int]],
        None,
    ]

    DoMoveSmellingSalt: Symbol[
        Optional[list[int]],
        None,
    ]

    DoMoveMetalSound: Symbol[
        Optional[list[int]],
        None,
    ]

    DoMoveTickle: Symbol[
        Optional[list[int]],
        None,
    ]

    DoMoveShadowHold: Symbol[
        Optional[list[int]],
        None,
    ]

    DoMoveHaze: Symbol[
        Optional[list[int]],
        None,
    ]

    DoMoveDamageMultihitFatigue: Symbol[
        Optional[list[int]],
        None,
    ]

    DoMoveDamageWeightDependent: Symbol[
        Optional[list[int]],
        None,
    ]

    DoMoveDamageBoostAllStats: Symbol[
        Optional[list[int]],
        None,
    ]

    DoMoveSynthesis: Symbol[
        Optional[list[int]],
        None,
    ]

    DoMoveBoostSpeed1: Symbol[
        Optional[list[int]],
        None,
    ]

    DoMoveRapidSpin: Symbol[
        Optional[list[int]],
        None,
    ]

    DoMoveSureShot: Symbol[
        Optional[list[int]],
        None,
    ]

    DoMoveCosmicPower: Symbol[
        Optional[list[int]],
        None,
    ]

    DoMoveSkyAttack: Symbol[
        Optional[list[int]],
        None,
    ]

    DoMoveDamageFreeze15: Symbol[
        Optional[list[int]],
        None,
    ]

    DoMoveMeteorMash: Symbol[
        Optional[list[int]],
        None,
    ]

    DoMoveEndure: Symbol[
        Optional[list[int]],
        None,
    ]

    DoMoveLowerSpeed1: Symbol[
        Optional[list[int]],
        None,
    ]

    DoMoveDamageConfuse10: Symbol[
        Optional[list[int]],
        None,
    ]

    DoMovePsywave: Symbol[
        Optional[list[int]],
        None,
    ]

    DoMoveDamageLowerDefensiveStatVariable: Symbol[
        Optional[list[int]],
        None,
    ]

    DoMovePsychoBoost: Symbol[
        Optional[list[int]],
        None,
    ]

    DoMoveUproar: Symbol[
        Optional[list[int]],
        None,
    ]

    DoMoveWaterSpout: Symbol[
        Optional[list[int]],
        None,
    ]

    DoMovePsychUp: Symbol[
        Optional[list[int]],
        None,
    ]

    DoMoveDamageWithRecoil: Symbol[
        Optional[list[int]],
        None,
    ]

    EntityIsValidMoveEffects: Symbol[
        Optional[list[int]],
        None,
    ]

    DoMoveRecoverHp: Symbol[
        Optional[list[int]],
        None,
    ]

    DoMoveEarthquake: Symbol[
        Optional[list[int]],
        None,
    ]

    GetNaturePowerVariant: Symbol[
        Optional[list[int]],
        None,
    ]

    DoMoveNaturePower: Symbol[
        Optional[list[int]],
        None,
    ]

    DoMoveDamageParalyze10: Symbol[
        Optional[list[int]],
        None,
    ]

    DoMoveSelfdestruct: Symbol[
        Optional[list[int]],
        None,
    ]

    DoMoveShadowBall: Symbol[
        Optional[list[int]],
        None,
    ]

    DoMoveCharge: Symbol[
        Optional[list[int]],
        None,
    ]

    DoMoveThunderbolt: Symbol[
        Optional[list[int]],
        None,
    ]

    DoMoveMist: Symbol[
        Optional[list[int]],
        None,
    ]

    DoMoveFissure: Symbol[
        Optional[list[int]],
        None,
    ]

    DoMoveDamageCringe10: Symbol[
        Optional[list[int]],
        None,
    ]

    DoMoveSafeguard: Symbol[
        Optional[list[int]],
        None,
    ]

    DoMoveAbsorb: Symbol[
        Optional[list[int]],
        None,
    ]

    DefenderAbilityIsActiveMoveEffects: Symbol[
        Optional[list[int]],
        None,
    ]

    DoMoveSkillSwap: Symbol[
        Optional[list[int]],
        None,
    ]

    DoMoveSketch: Symbol[
        Optional[list[int]],
        None,
    ]

    DoMoveHeadbutt: Symbol[
        Optional[list[int]],
        None,
    ]

    DoMoveDoubleEdge: Symbol[
        Optional[list[int]],
        None,
    ]

    DoMoveSandstorm: Symbol[
        Optional[list[int]],
        None,
    ]

    DoMoveLowerAccuracy1: Symbol[
        Optional[list[int]],
        None,
    ]

    DoMoveDamagePoison40: Symbol[
        Optional[list[int]],
        None,
    ]

    DoMoveGrowth: Symbol[
        Optional[list[int]],
        None,
    ]

    DoMoveSacredFire: Symbol[
        Optional[list[int]],
        None,
    ]

    DoMoveOhko: Symbol[
        Optional[list[int]],
        None,
    ]

    DoMoveSolarBeam: Symbol[
        Optional[list[int]],
        None,
    ]

    DoMoveSonicBoom: Symbol[
        Optional[list[int]],
        None,
    ]

    DoMoveFly: Symbol[
        Optional[list[int]],
        None,
    ]

    DoMoveExplosion: Symbol[
        Optional[list[int]],
        None,
    ]

    DoMoveDive: Symbol[
        Optional[list[int]],
        None,
    ]

    DoMoveWaterfall: Symbol[
        Optional[list[int]],
        None,
    ]

    DoMoveDamageLowerAccuracy40: Symbol[
        Optional[list[int]],
        None,
    ]

    DoMoveStockpile: Symbol[
        Optional[list[int]],
        None,
    ]

    DoMoveTwister: Symbol[
        Optional[list[int]],
        None,
    ]

    DoMoveTwineedle: Symbol[
        Optional[list[int]],
        None,
    ]

    DoMoveRecoverHpTeam: Symbol[
        Optional[list[int]],
        None,
    ]

    DoMoveMinimize: Symbol[
        Optional[list[int]],
        None,
    ]

    DoMoveSeismicToss: Symbol[
        Optional[list[int]],
        None,
    ]

    DoMoveConfuse: Symbol[
        Optional[list[int]],
        None,
    ]

    DoMoveTaunt: Symbol[
        Optional[list[int]],
        None,
    ]

    DoMoveMoonlight: Symbol[
        Optional[list[int]],
        None,
    ]

    DoMoveHornDrill: Symbol[
        Optional[list[int]],
        None,
    ]

    DoMoveSwordsDance: Symbol[
        Optional[list[int]],
        None,
    ]

    DoMoveConversion: Symbol[
        Optional[list[int]],
        None,
    ]

    DoMoveConversion2: Symbol[
        Optional[list[int]],
        None,
    ]

    DoMoveHelpingHand: Symbol[
        Optional[list[int]],
        None,
    ]

    DoMoveBoostDefense2: Symbol[
        Optional[list[int]],
        None,
    ]

    DoMoveWarp: Symbol[
        Optional[list[int]],
        None,
    ]

    DoMoveThundershock: Symbol[
        Optional[list[int]],
        None,
    ]

    DoMoveThunderWave: Symbol[
        Optional[list[int]],
        None,
    ]

    DoMoveZapCannon: Symbol[
        Optional[list[int]],
        None,
    ]

    DoMoveBlock: Symbol[
        Optional[list[int]],
        None,
    ]

    DoMovePoison: Symbol[
        Optional[list[int]],
        None,
    ]

    DoMoveToxic: Symbol[
        Optional[list[int]],
        None,
    ]

    DoMovePoisonFang: Symbol[
        Optional[list[int]],
        None,
    ]

    DoMoveDamagePoison18: Symbol[
        Optional[list[int]],
        None,
    ]

    DoMoveJumpKick: Symbol[
        Optional[list[int]],
        None,
    ]

    DoMoveBounce: Symbol[
        Optional[list[int]],
        None,
    ]

    DoMoveHiJumpKick: Symbol[
        Optional[list[int]],
        None,
    ]

    DoMoveTriAttack: Symbol[
        Optional[list[int]],
        None,
    ]

    DoMoveSwapItems: Symbol[
        Optional[list[int]],
        None,
    ]

    DoMoveTripleKick: Symbol[
        Optional[list[int]],
        None,
    ]

    DoMoveSport: Symbol[
        Optional[list[int]],
        None,
    ]

    DoMoveMudSlap: Symbol[
        Optional[list[int]],
        None,
    ]

    DoMoveDamageStealItem: Symbol[
        Optional[list[int]],
        None,
    ]

    DoMoveAmnesia: Symbol[
        Optional[list[int]],
        None,
    ]

    DoMoveNightShade: Symbol[
        Optional[list[int]],
        None,
    ]

    DoMoveGrowl: Symbol[
        Optional[list[int]],
        None,
    ]

    DoMoveSurf: Symbol[
        Optional[list[int]],
        None,
    ]

    DoMoveRolePlay: Symbol[
        Optional[list[int]],
        None,
    ]

    DoMoveSunnyDay: Symbol[
        Optional[list[int]],
        None,
    ]

    DoMoveLowerDefense1: Symbol[
        Optional[list[int]],
        None,
    ]

    DoMoveWish: Symbol[
        Optional[list[int]],
        None,
    ]

    DoMoveFakeOut: Symbol[
        Optional[list[int]],
        None,
    ]

    DoMoveSleepTalk: Symbol[
        Optional[list[int]],
        None,
    ]

    DoMovePayDay: Symbol[
        Optional[list[int]],
        None,
    ]

    DoMoveAssist: Symbol[
        Optional[list[int]],
        None,
    ]

    DoMoveRest: Symbol[
        Optional[list[int]],
        None,
    ]

    DoMoveIngrain: Symbol[
        Optional[list[int]],
        None,
    ]

    DoMoveSwallow: Symbol[
        Optional[list[int]],
        None,
    ]

    DoMoveCurse: Symbol[
        Optional[list[int]],
        None,
    ]

    DoMoveSuperpower: Symbol[
        Optional[list[int]],
        None,
    ]

    DoMoveSteelWing: Symbol[
        Optional[list[int]],
        None,
    ]

    DoMoveSpitUp: Symbol[
        Optional[list[int]],
        None,
    ]

    DoMoveDynamicPunch: Symbol[
        Optional[list[int]],
        None,
    ]

    DoMoveKnockOff: Symbol[
        Optional[list[int]],
        None,
    ]

    DoMoveSplash: Symbol[
        Optional[list[int]],
        None,
    ]

    DoMoveSetDamage: Symbol[
        Optional[list[int]],
        None,
    ]

    DoMoveBellyDrum: Symbol[
        Optional[list[int]],
        None,
    ]

    DoMoveLightScreen: Symbol[
        Optional[list[int]],
        None,
    ]

    DoMoveSecretPower: Symbol[
        Optional[list[int]],
        None,
    ]

    DoMoveDamageConfuse30: Symbol[
        Optional[list[int]],
        None,
    ]

    DoMoveBulkUp: Symbol[
        Optional[list[int]],
        None,
    ]

    DoMovePause: Symbol[
        Optional[list[int]],
        None,
    ]

    DoMoveFeatherDance: Symbol[
        Optional[list[int]],
        None,
    ]

    DoMoveBeatUp: Symbol[
        Optional[list[int]],
        None,
    ]

    DoMoveBlastBurn: Symbol[
        Optional[list[int]],
        None,
    ]

    DoMoveCrushClaw: Symbol[
        Optional[list[int]],
        None,
    ]

    DoMoveBlazeKick: Symbol[
        Optional[list[int]],
        None,
    ]

    DoMovePresent: Symbol[
        Optional[list[int]],
        None,
    ]

    DoMoveEruption: Symbol[
        Optional[list[int]],
        None,
    ]

    DoMoveTransform: Symbol[
        Optional[list[int]],
        None,
    ]

    DoMovePoisonTail: Symbol[
        Optional[list[int]],
        None,
    ]

    DoMoveBlowback: Symbol[
        Optional[list[int]],
        None,
    ]

    DoMoveCamouflage: Symbol[
        Optional[list[int]],
        None,
    ]

    DoMoveTailGlow: Symbol[
        Optional[list[int]],
        None,
    ]

    DoMoveDamageConstrict10: Symbol[
        Optional[list[int]],
        None,
    ]

    DoMovePerishSong: Symbol[
        Optional[list[int]],
        None,
    ]

    DoMoveWrap: Symbol[
        Optional[list[int]],
        None,
    ]

    DoMoveSpikes: Symbol[
        Optional[list[int]],
        None,
    ]

    DoMoveMagnitude: Symbol[
        Optional[list[int]],
        None,
    ]

    DoMoveMagicCoat: Symbol[
        Optional[list[int]],
        None,
    ]

    DoMoveProtect: Symbol[
        Optional[list[int]],
        None,
    ]

    DoMoveDefenseCurl: Symbol[
        Optional[list[int]],
        None,
    ]

    DoMoveDecoy: Symbol[
        Optional[list[int]],
        None,
    ]

    DoMoveMistBall: Symbol[
        Optional[list[int]],
        None,
    ]

    DoMoveDestinyBond: Symbol[
        Optional[list[int]],
        None,
    ]

    DoMoveMirrorCoat: Symbol[
        Optional[list[int]],
        None,
    ]

    DoMoveCalmMind: Symbol[
        Optional[list[int]],
        None,
    ]

    DoMoveHiddenPower: Symbol[
        Optional[list[int]],
        None,
    ]

    DoMoveMetalClaw: Symbol[
        Optional[list[int]],
        None,
    ]

    DoMoveAttract: Symbol[
        Optional[list[int]],
        None,
    ]

    DoMoveCopycat: Symbol[
        Optional[list[int]],
        None,
    ]

    DoMoveFrustration: Symbol[
        Optional[list[int]],
        None,
    ]

    DoMoveLeechSeed: Symbol[
        Optional[list[int]],
        None,
    ]

    DoMoveMetronome: Symbol[
        Optional[list[int]],
        None,
    ]

    DoMoveDreamEater: Symbol[
        Optional[list[int]],
        None,
    ]

    DoMoveSnatch: Symbol[
        Optional[list[int]],
        None,
    ]

    DoMoveRecycle: Symbol[
        Optional[list[int]],
        None,
    ]

    DoMoveReflect: Symbol[
        Optional[list[int]],
        None,
    ]

    DoMoveDragonRage: Symbol[
        Optional[list[int]],
        None,
    ]

    DoMoveDragonDance: Symbol[
        Optional[list[int]],
        None,
    ]

    DoMoveSkullBash: Symbol[
        Optional[list[int]],
        None,
    ]

    DoMoveDamageLowerSpecialDefense50: Symbol[
        Optional[list[int]],
        None,
    ]

    DoMoveStruggle: Symbol[
        Optional[list[int]],
        None,
    ]

    DoMoveRockSmash: Symbol[
        Optional[list[int]],
        None,
    ]

    DoMoveSeeTrap: Symbol[
        Optional[list[int]],
        None,
    ]

    DoMoveTakeaway: Symbol[
        Optional[list[int]],
        None,
    ]

    DoMoveRebound: Symbol[
        Optional[list[int]],
        None,
    ]

    DoMoveSwitchPositions: Symbol[
        Optional[list[int]],
        None,
    ]

    DoMoveStayAway: Symbol[
        Optional[list[int]],
        None,
    ]

    DoMoveCleanse: Symbol[
        Optional[list[int]],
        None,
    ]

    DoMoveSiesta: Symbol[
        Optional[list[int]],
        None,
    ]

    DoMoveTwoEdge: Symbol[
        Optional[list[int]],
        None,
    ]

    DoMoveNoMove: Symbol[
        Optional[list[int]],
        None,
    ]

    DoMoveScan: Symbol[
        Optional[list[int]],
        None,
    ]

    DoMovePowerEars: Symbol[
        Optional[list[int]],
        None,
    ]

    DoMoveTransfer: Symbol[
        Optional[list[int]],
        None,
    ]

    DoMoveSlowDown: Symbol[
        Optional[list[int]],
        None,
    ]

    DoMoveSearchlight: Symbol[
        Optional[list[int]],
        None,
    ]

    DoMovePetrify: Symbol[
        Optional[list[int]],
        None,
    ]

    DoMovePounce: Symbol[
        Optional[list[int]],
        None,
    ]

    DoMoveTrawl: Symbol[
        Optional[list[int]],
        None,
    ]

    DoMoveEscape: Symbol[
        Optional[list[int]],
        None,
    ]

    DoMoveDrought: Symbol[
        Optional[list[int]],
        None,
    ]

    DoMoveTrapBuster: Symbol[
        Optional[list[int]],
        None,
    ]

    DoMoveWildCall: Symbol[
        Optional[list[int]],
        None,
    ]

    DoMoveInvisify: Symbol[
        Optional[list[int]],
        None,
    ]

    DoMoveOneShot: Symbol[
        Optional[list[int]],
        None,
    ]

    DoMoveHpGauge: Symbol[
        Optional[list[int]],
        None,
    ]

    DoMoveVacuumCut: Symbol[
        Optional[list[int]],
        None,
    ]

    DoMoveReviver: Symbol[
        Optional[list[int]],
        None,
    ]

    DoMoveShocker: Symbol[
        Optional[list[int]],
        None,
    ]

    DoMoveEcho: Symbol[
        Optional[list[int]],
        None,
    ]

    DoMoveFamish: Symbol[
        Optional[list[int]],
        None,
    ]

    DoMoveOneRoom: Symbol[
        Optional[list[int]],
        None,
    ]

    DoMoveFillIn: Symbol[
        Optional[list[int]],
        None,
    ]

    DoMoveTrapper: Symbol[
        Optional[list[int]],
        None,
    ]

    DoMoveItemize: Symbol[
        Optional[list[int]],
        None,
    ]

    DoMoveHurl: Symbol[
        Optional[list[int]],
        None,
    ]

    DoMoveMobile: Symbol[
        Optional[list[int]],
        None,
    ]

    DoMoveSeeStairs: Symbol[
        Optional[list[int]],
        None,
    ]

    DoMoveLongToss: Symbol[
        Optional[list[int]],
        None,
    ]

    DoMovePierce: Symbol[
        Optional[list[int]],
        None,
    ]

    DoMoveHammerArm: Symbol[
        Optional[list[int]],
        None,
    ]

    DoMoveAquaRing: Symbol[
        Optional[list[int]],
        None,
    ]

    DoMoveGastroAcid: Symbol[
        Optional[list[int]],
        None,
    ]

    DoMoveHealingWish: Symbol[
        Optional[list[int]],
        None,
    ]

    DoMoveCloseCombat: Symbol[
        Optional[list[int]],
        None,
    ]

    DoMoveLuckyChant: Symbol[
        Optional[list[int]],
        None,
    ]

    DoMoveGuardSwap: Symbol[
        Optional[list[int]],
        None,
    ]

    DoMoveHealOrder: Symbol[
        Optional[list[int]],
        None,
    ]

    DoMoveHealBlock: Symbol[
        Optional[list[int]],
        None,
    ]

    DoMoveThunderFang: Symbol[
        Optional[list[int]],
        None,
    ]

    DoMoveDefog: Symbol[
        Optional[list[int]],
        None,
    ]

    DoMoveTrumpCard: Symbol[
        Optional[list[int]],
        None,
    ]

    DoMoveIceFang: Symbol[
        Optional[list[int]],
        None,
    ]

    DoMovePsychoShift: Symbol[
        Optional[list[int]],
        None,
    ]

    DoMoveEmbargo: Symbol[
        Optional[list[int]],
        None,
    ]

    DoMoveBrine: Symbol[
        Optional[list[int]],
        None,
    ]

    DoMoveNaturalGift: Symbol[
        Optional[list[int]],
        None,
    ]

    DoMoveGyroBall: Symbol[
        Optional[list[int]],
        None,
    ]

    DoMoveShadowForce: Symbol[
        Optional[list[int]],
        None,
    ]

    DoMoveGravity: Symbol[
        Optional[list[int]],
        None,
    ]

    DoMoveStealthRock: Symbol[
        Optional[list[int]],
        None,
    ]

    DoMoveChargeBeam: Symbol[
        Optional[list[int]],
        None,
    ]

    DoMoveDamageEatItem: Symbol[
        Optional[list[int]],
        None,
    ]

    DoMoveAcupressure: Symbol[
        Optional[list[int]],
        None,
    ]

    DoMoveMagnetRise: Symbol[
        Optional[list[int]],
        None,
    ]

    DoMoveToxicSpikes: Symbol[
        Optional[list[int]],
        None,
    ]

    DoMoveLastResort: Symbol[
        Optional[list[int]],
        None,
    ]

    DoMoveTrickRoom: Symbol[
        Optional[list[int]],
        None,
    ]

    DoMoveWorrySeed: Symbol[
        Optional[list[int]],
        None,
    ]

    DoMoveDamageHpDependent: Symbol[
        Optional[list[int]],
        None,
    ]

    DoMoveHeartSwap: Symbol[
        Optional[list[int]],
        None,
    ]

    DoMoveRoost: Symbol[
        Optional[list[int]],
        None,
    ]

    DoMovePowerSwap: Symbol[
        Optional[list[int]],
        None,
    ]

    DoMovePowerTrick: Symbol[
        Optional[list[int]],
        None,
    ]

    DoMoveFeint: Symbol[
        Optional[list[int]],
        None,
    ]

    DoMoveFlareBlitz: Symbol[
        Optional[list[int]],
        None,
    ]

    DoMoveDefendOrder: Symbol[
        Optional[list[int]],
        None,
    ]

    DoMoveFireFang: Symbol[
        Optional[list[int]],
        None,
    ]

    DoMoveLunarDance: Symbol[
        Optional[list[int]],
        None,
    ]

    DoMoveMiracleEye: Symbol[
        Optional[list[int]],
        None,
    ]

    DoMoveWakeUpSlap: Symbol[
        Optional[list[int]],
        None,
    ]

    DoMoveMetalBurst: Symbol[
        Optional[list[int]],
        None,
    ]

    DoMoveHeadSmash: Symbol[
        Optional[list[int]],
        None,
    ]

    DoMoveCaptivate: Symbol[
        Optional[list[int]],
        None,
    ]

    DoMoveLeafStorm: Symbol[
        Optional[list[int]],
        None,
    ]

    DoMoveDracoMeteor: Symbol[
        Optional[list[int]],
        None,
    ]

    DoMoveRockPolish: Symbol[
        Optional[list[int]],
        None,
    ]

    DoMoveNastyPlot: Symbol[
        Optional[list[int]],
        None,
    ]

    DoMoveTag0x1AB: Symbol[
        Optional[list[int]],
        None,
    ]

    DoMoveTag0x1A6: Symbol[
        Optional[list[int]],
        None,
    ]

    DoMoveTag0x1A7: Symbol[
        Optional[list[int]],
        None,
    ]


class Move_effectsDataProtocol(Protocol):

    MAX_HP_CAP_MOVE_EFFECTS: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    LUNAR_DANCE_PP_RESTORATION: Symbol[
        Optional[list[int]],
        Optional[int],
    ]


Move_effectsProtocol = SectionProtocol[
    Move_effectsFunctionsProtocol,
    Move_effectsDataProtocol,
    Optional[int],
]


class Overlay0FunctionsProtocol(Protocol):

    SelectRandomBackground: Symbol[
        Optional[list[int]],
        None,
    ]

    WM_Init: Symbol[
        Optional[list[int]],
        None,
    ]

    WmInitCore: Symbol[
        Optional[list[int]],
        None,
    ]

    WM_Finish: Symbol[
        Optional[list[int]],
        None,
    ]

    WMi_SetCallbackTable: Symbol[
        Optional[list[int]],
        None,
    ]

    WmGetCommandBuffer4Arm7: Symbol[
        Optional[list[int]],
        None,
    ]

    WMi_SendCommand: Symbol[
        Optional[list[int]],
        None,
    ]

    WMi_SendCommandDirect: Symbol[
        Optional[list[int]],
        None,
    ]

    WMi_GetSystemWork: Symbol[
        Optional[list[int]],
        None,
    ]

    WMi_CheckInitialized: Symbol[
        Optional[list[int]],
        None,
    ]

    WMi_CheckIdle: Symbol[
        Optional[list[int]],
        None,
    ]

    WMi_CheckState: Symbol[
        Optional[list[int]],
        None,
    ]

    WmReceiveFifo: Symbol[
        Optional[list[int]],
        None,
    ]

    WmClearFifoRecvFlag: Symbol[
        Optional[list[int]],
        None,
    ]

    WMi_GetStatusAddress: Symbol[
        Optional[list[int]],
        None,
    ]

    WM_GetAid: Symbol[
        Optional[list[int]],
        None,
    ]

    WM_GetConnectedAids: Symbol[
        Optional[list[int]],
        None,
    ]

    WM_SetIndCallback: Symbol[
        Optional[list[int]],
        None,
    ]

    WM_SetPortCallback: Symbol[
        Optional[list[int]],
        None,
    ]

    WM_ReadStatus: Symbol[
        Optional[list[int]],
        None,
    ]

    WM_GetMpSendBufferSize: Symbol[
        Optional[list[int]],
        None,
    ]

    WM_GetMpReceiveBufferSize: Symbol[
        Optional[list[int]],
        None,
    ]

    WM_ReadMpData: Symbol[
        Optional[list[int]],
        None,
    ]

    WM_GetAllowedChannel: Symbol[
        Optional[list[int]],
        None,
    ]

    WM_GetLinkLevel: Symbol[
        Optional[list[int]],
        None,
    ]

    WM_GetDispersionBeaconPeriod: Symbol[
        Optional[list[int]],
        None,
    ]

    WM_GetDispersionScanPeriod: Symbol[
        Optional[list[int]],
        None,
    ]

    WM_GetOtherElements: Symbol[
        Optional[list[int]],
        None,
    ]

    WM_GetNextTgid: Symbol[
        Optional[list[int]],
        None,
    ]

    WM_Enable: Symbol[
        Optional[list[int]],
        None,
    ]

    WMi_EnableEx: Symbol[
        Optional[list[int]],
        None,
    ]

    WM_Disable: Symbol[
        Optional[list[int]],
        None,
    ]

    WM_PowerOn: Symbol[
        Optional[list[int]],
        None,
    ]

    WM_PowerOff: Symbol[
        Optional[list[int]],
        None,
    ]

    WM_InitializeEx: Symbol[
        Optional[list[int]],
        None,
    ]

    WM_InitializeForListening: Symbol[
        Optional[list[int]],
        None,
    ]

    WMi_InitializeEx: Symbol[
        Optional[list[int]],
        None,
    ]

    WM_Reset: Symbol[
        Optional[list[int]],
        None,
    ]

    WM_End: Symbol[
        Optional[list[int]],
        None,
    ]

    WM_SetParentParameter: Symbol[
        Optional[list[int]],
        None,
    ]

    WmCheckParentParameter: Symbol[
        Optional[list[int]],
        None,
    ]

    WMi_StartParentEx: Symbol[
        Optional[list[int]],
        None,
    ]

    WM_StartParent: Symbol[
        Optional[list[int]],
        None,
    ]

    WM_EndParent: Symbol[
        Optional[list[int]],
        None,
    ]

    WM_StartScan: Symbol[
        Optional[list[int]],
        None,
    ]

    WM_StartScanEx: Symbol[
        Optional[list[int]],
        None,
    ]

    WM_EndScan: Symbol[
        Optional[list[int]],
        None,
    ]

    WM_StartConnectEx: Symbol[
        Optional[list[int]],
        None,
    ]

    WM_Disconnect: Symbol[
        Optional[list[int]],
        None,
    ]

    WMi_StartMP: Symbol[
        Optional[list[int]],
        None,
    ]

    WM_StartMpEx: Symbol[
        Optional[list[int]],
        None,
    ]

    WM_StartMP: Symbol[
        Optional[list[int]],
        None,
    ]

    WM_SetMpDataToPortEx: Symbol[
        Optional[list[int]],
        None,
    ]

    WM_EndMP: Symbol[
        Optional[list[int]],
        None,
    ]

    WM_StartDcf: Symbol[
        Optional[list[int]],
        None,
    ]

    WM_SetDcfData: Symbol[
        Optional[list[int]],
        None,
    ]

    WM_EndDcf: Symbol[
        Optional[list[int]],
        None,
    ]

    WM_StartDataSharing: Symbol[
        Optional[list[int]],
        None,
    ]

    WM_EndDataSharing: Symbol[
        Optional[list[int]],
        None,
    ]

    WM_StepDataSharing: Symbol[
        Optional[list[int]],
        None,
    ]

    WmDataSharingSetDataCallback: Symbol[
        Optional[list[int]],
        None,
    ]

    WmDataSharingReceiveCallback_Parent: Symbol[
        Optional[list[int]],
        None,
    ]

    WmDataSharingReceiveCallback_Child: Symbol[
        Optional[list[int]],
        None,
    ]

    WmDataSharingReceiveData: Symbol[
        Optional[list[int]],
        None,
    ]

    WmDataSharingSendDataSet: Symbol[
        Optional[list[int]],
        None,
    ]

    WM_GetSharedDataAddress: Symbol[
        Optional[list[int]],
        None,
    ]

    WmGetSharedDataAddress: Symbol[
        Optional[list[int]],
        None,
    ]

    WM_StartKeySharing: Symbol[
        Optional[list[int]],
        None,
    ]

    WM_SetWepKey: Symbol[
        Optional[list[int]],
        None,
    ]

    WM_SetWepKeyEx: Symbol[
        Optional[list[int]],
        None,
    ]

    WM_SetGameInfo: Symbol[
        Optional[list[int]],
        None,
    ]

    WM_SetBeaconIndication: Symbol[
        Optional[list[int]],
        None,
    ]

    WM_SetLifeTime: Symbol[
        Optional[list[int]],
        None,
    ]

    WM_MeasureChannel: Symbol[
        Optional[list[int]],
        None,
    ]

    WM_SetEntry: Symbol[
        Optional[list[int]],
        None,
    ]

    Wbti_InitBitmap: Symbol[
        Optional[list[int]],
        None,
    ]

    Wbti_MergeBitmapIndex: Symbol[
        Optional[list[int]],
        None,
    ]

    Wbti_FindBitmapIndex: Symbol[
        Optional[list[int]],
        None,
    ]

    Wbti_GetPacketBuffer: Symbol[
        Optional[list[int]],
        None,
    ]

    Wbti_SwitchNextCommand: Symbol[
        Optional[list[int]],
        None,
    ]

    Wbti_NotifySystemCallback: Symbol[
        Optional[list[int]],
        None,
    ]

    Wbti_TryCreateResponse: Symbol[
        Optional[list[int]],
        None,
    ]

    Wbti_CheckRequest: Symbol[
        Optional[list[int]],
        None,
    ]

    Wbti_CheckBlockResponse: Symbol[
        Optional[list[int]],
        None,
    ]

    Wbt_CallPacketSendHook: Symbol[
        Optional[list[int]],
        None,
    ]

    Wbti_NotifyCompletionCallback: Symbol[
        Optional[list[int]],
        None,
    ]

    Wbt_CallPacketRecvHook: Symbol[
        Optional[list[int]],
        None,
    ]

    Wbt_InitContext: Symbol[
        Optional[list[int]],
        None,
    ]

    Wbt_ResetContext: Symbol[
        Optional[list[int]],
        None,
    ]

    Wbt_PostCommand: Symbol[
        Optional[list[int]],
        None,
    ]

    Wbt_CancelCommand: Symbol[
        Optional[list[int]],
        None,
    ]

    Wbt_GetBitmapLength: Symbol[
        Optional[list[int]],
        None,
    ]

    Wbt_RegisterBlockInfo: Symbol[
        Optional[list[int]],
        None,
    ]

    Wbt_UnregisterBlockInfo: Symbol[
        Optional[list[int]],
        None,
    ]

    Wbt_GetRegisteredCount: Symbol[
        Optional[list[int]],
        None,
    ]

    Wbt_PrintBtList: Symbol[
        Optional[list[int]],
        None,
    ]

    Wbt_AidbitmapToAid: Symbol[
        Optional[list[int]],
        None,
    ]

    Wbt_InitParent: Symbol[
        Optional[list[int]],
        None,
    ]

    Wbt_InitChild: Symbol[
        Optional[list[int]],
        None,
    ]

    Wbt_End: Symbol[
        Optional[list[int]],
        None,
    ]

    Wbt_SetOwnAid: Symbol[
        Optional[list[int]],
        None,
    ]

    Wbt_MpParentSendHook: Symbol[
        Optional[list[int]],
        None,
    ]

    Wbt_MpChildSendHook: Symbol[
        Optional[list[int]],
        None,
    ]

    Wbt_MpParentRecvHook: Symbol[
        Optional[list[int]],
        None,
    ]

    Wbt_MpChildRecvHook: Symbol[
        Optional[list[int]],
        None,
    ]

    Wbt_RegisterBlock: Symbol[
        Optional[list[int]],
        None,
    ]

    Wbt_UnregisterBlock: Symbol[
        Optional[list[int]],
        None,
    ]

    Wbt_RequestSync: Symbol[
        Optional[list[int]],
        None,
    ]

    Wbt_GetBlockInfo: Symbol[
        Optional[list[int]],
        None,
    ]

    Wbt_GetBlock: Symbol[
        Optional[list[int]],
        None,
    ]

    Wbt_PutUserData: Symbol[
        Optional[list[int]],
        None,
    ]

    Wbt_CancelCurrentCommand: Symbol[
        Optional[list[int]],
        None,
    ]

    MB_CommSetParentStateCallback: Symbol[
        Optional[list[int]],
        None,
    ]

    MB_CommGetParentState: Symbol[
        Optional[list[int]],
        None,
    ]

    MB_CommGetChildUser: Symbol[
        Optional[list[int]],
        None,
    ]

    MB_CommIsBootable: Symbol[
        Optional[list[int]],
        None,
    ]

    MB_CommResponseRequest: Symbol[
        Optional[list[int]],
        None,
    ]

    MBi_CommChangeParentState: Symbol[
        Optional[list[int]],
        None,
    ]

    MBi_CommChangeParentStateCallbackOnly: Symbol[
        Optional[list[int]],
        None,
    ]

    MBi_CommParentCallback: Symbol[
        Optional[list[int]],
        None,
    ]

    MBi_CommParentRecvDataPerChild: Symbol[
        Optional[list[int]],
        None,
    ]

    MBi_CommParentRecvData: Symbol[
        Optional[list[int]],
        None,
    ]

    MBi_CommParentSendMsg: Symbol[
        Optional[list[int]],
        None,
    ]

    MBi_CommParentSendDlFileInfo: Symbol[
        Optional[list[int]],
        None,
    ]

    MBi_ReloadCache: Symbol[
        Optional[list[int]],
        None,
    ]

    MBi_CommParentSendBlock: Symbol[
        Optional[list[int]],
        None,
    ]

    MBi_CommParentSendData: Symbol[
        Optional[list[int]],
        None,
    ]

    MBi_Calc_SendBlock: Symbol[
        Optional[list[int]],
        None,
    ]

    MBi_Calc_NextSendBlock: Symbol[
        Optional[list[int]],
        None,
    ]

    IsChildAidValid: Symbol[
        Optional[list[int]],
        None,
    ]

    MBi_CommCallParentError: Symbol[
        Optional[list[int]],
        None,
    ]

    MB_GetSegmentLength: Symbol[
        Optional[list[int]],
        None,
    ]

    MB_ReadSegment: Symbol[
        Optional[list[int]],
        None,
    ]

    MBi_ReadSegmentHeader: Symbol[
        Optional[list[int]],
        None,
    ]

    MB_RegisterFile: Symbol[
        Optional[list[int]],
        None,
    ]

    MBi_MakeDownloadFileInfo: Symbol[
        Optional[list[int]],
        None,
    ]

    MBi_SetSegmentInfo: Symbol[
        Optional[list[int]],
        None,
    ]

    MBi_MakeBlockInfoTable: Symbol[
        Optional[list[int]],
        None,
    ]

    MBi_Get_BlockInfo: Symbol[
        Optional[list[int]],
        None,
    ]

    MBi_IsAbleToRecv: Symbol[
        Optional[list[int]],
        None,
    ]

    IsAbleToLoad: Symbol[
        Optional[list[int]],
        None,
    ]

    MBi_BlockHeaderEnd: Symbol[
        Optional[list[int]],
        None,
    ]

    MBi_Calc_Cksum: Symbol[
        Optional[list[int]],
        None,
    ]

    MBi_MakeGameInfo: Symbol[
        Optional[list[int]],
        None,
    ]

    MBi_ReadIconInfo: Symbol[
        Optional[list[int]],
        None,
    ]

    MB_UpdateGameInfoMember: Symbol[
        Optional[list[int]],
        None,
    ]

    Mystrlen_MB: Symbol[
        Optional[list[int]],
        None,
    ]

    MB_AddGameInfo: Symbol[
        Optional[list[int]],
        None,
    ]

    MB_InitSendGameInfoStatus: Symbol[
        Optional[list[int]],
        None,
    ]

    MBi_ClearSendStatus: Symbol[
        Optional[list[int]],
        None,
    ]

    MB_SendGameInfoBeacon: Symbol[
        Optional[list[int]],
        None,
    ]

    MBi_ReadyBeaconSendStatus: Symbol[
        Optional[list[int]],
        None,
    ]

    MBi_InitSendFixedBeacon: Symbol[
        Optional[list[int]],
        None,
    ]

    MBi_SendFixedBeacon: Symbol[
        Optional[list[int]],
        None,
    ]

    MBi_InitSendVolatBeacon: Symbol[
        Optional[list[int]],
        None,
    ]

    MBi_SendVolatBeacon: Symbol[
        Optional[list[int]],
        None,
    ]

    ChangeScanChannel: Symbol[
        Optional[list[int]],
        None,
    ]

    MBi_IsSendEnabled: Symbol[
        Optional[list[int]],
        None,
    ]

    MBi_OnInitializeDone: Symbol[
        Optional[list[int]],
        None,
    ]

    MBi_EndCommon: Symbol[
        Optional[list[int]],
        None,
    ]

    MBi_ParentCallback: Symbol[
        Optional[list[int]],
        None,
    ]

    MBi_ChildPortCallback: Symbol[
        Optional[list[int]],
        None,
    ]

    MBi_ChildCallback: Symbol[
        Optional[list[int]],
        None,
    ]

    MBi_GetBeaconPeriodDispersion: Symbol[
        Optional[list[int]],
        None,
    ]

    MB_Init: Symbol[
        Optional[list[int]],
        None,
    ]

    MBi_IsCommSizeValid: Symbol[
        Optional[list[int]],
        None,
    ]

    MB_SetParentCommParam: Symbol[
        Optional[list[int]],
        None,
    ]

    MBi_StartCommon: Symbol[
        Optional[list[int]],
        None,
    ]

    MBi_StartParentCore: Symbol[
        Optional[list[int]],
        None,
    ]

    MB_StartParentFromIdle: Symbol[
        Optional[list[int]],
        None,
    ]

    MBi_CallReset: Symbol[
        Optional[list[int]],
        None,
    ]

    MBi_OnReset: Symbol[
        Optional[list[int]],
        None,
    ]

    MBi_CommEnd: Symbol[
        Optional[list[int]],
        None,
    ]

    MB_EndToIdle: Symbol[
        Optional[list[int]],
        None,
    ]

    MB_DisconnectChild: Symbol[
        Optional[list[int]],
        None,
    ]

    MBi_SetMaxScanTime: Symbol[
        Optional[list[int]],
        None,
    ]

    MBi_SetMpData: Symbol[
        Optional[list[int]],
        None,
    ]

    MBi_SendMP: Symbol[
        Optional[list[int]],
        None,
    ]

    MBi_GetGgid: Symbol[
        Optional[list[int]],
        None,
    ]

    MBi_GetTgid: Symbol[
        Optional[list[int]],
        None,
    ]

    MBi_GetAttribute: Symbol[
        Optional[list[int]],
        None,
    ]

    MBi_IsStarted: Symbol[
        Optional[list[int]],
        None,
    ]

    MBi_CheckWmErrcode: Symbol[
        Optional[list[int]],
        None,
    ]

    MBi_InitCache: Symbol[
        Optional[list[int]],
        None,
    ]

    MBi_AttachCacheBuffer: Symbol[
        Optional[list[int]],
        None,
    ]

    MBi_MakeParentSendBuffer: Symbol[
        Optional[list[int]],
        None,
    ]

    MBi_TaskThread: Symbol[
        Optional[list[int]],
        None,
    ]

    MBi_InitTaskThread: Symbol[
        Optional[list[int]],
        None,
    ]

    MBi_IsTaskAvailable: Symbol[
        Optional[list[int]],
        None,
    ]

    MBi_InitTaskInfo: Symbol[
        Optional[list[int]],
        None,
    ]

    MBi_ReadFromCache: Symbol[
        Optional[list[int]],
        None,
    ]

    MBi_SetTask: Symbol[
        Optional[list[int]],
        None,
    ]

    MBi_EndTaskThread: Symbol[
        Optional[list[int]],
        None,
    ]

    MBi_SetChildMpMaxSize: Symbol[
        Optional[list[int]],
        None,
    ]

    MBi_SetParentPieceBuffer: Symbol[
        Optional[list[int]],
        None,
    ]

    MBi_ClearParentPieceBuffer: Symbol[
        Optional[list[int]],
        None,
    ]

    MBi_SetRecvBufferFromChild: Symbol[
        Optional[list[int]],
        None,
    ]

    MBi_ReceiveRequestDataPiece: Symbol[
        Optional[list[int]],
        None,
    ]

    IsGetAllRequestData: Symbol[
        Optional[list[int]],
        None,
    ]

    reset_network_vars: Symbol[
        Optional[list[int]],
        None,
    ]

    OS_YieldThread2: Symbol[
        Optional[list[int]],
        None,
    ]

    Empty_Func_Cps: Symbol[
        Optional[list[int]],
        None,
    ]

    default_link_is_on: Symbol[
        Optional[list[int]],
        None,
    ]

    Cps_Startup: Symbol[
        Optional[list[int]],
        None,
    ]

    Cps_CalmDown: Symbol[
        Optional[list[int]],
        None,
    ]

    Cps_SetScavengerCallback: Symbol[
        Optional[list[int]],
        None,
    ]

    Cps_Cleanup: Symbol[
        Optional[list[int]],
        None,
    ]

    Cps_SetThreadPriority: Symbol[
        Optional[list[int]],
        None,
    ]

    calc_checksum_do: Symbol[
        Optional[list[int]],
        None,
    ]

    invert_checksum: Symbol[
        Optional[list[int]],
        None,
    ]

    calc_checksum: Symbol[
        Optional[list[int]],
        None,
    ]

    check_tcpudpsum: Symbol[
        Optional[list[int]],
        None,
    ]

    ip_islocal: Symbol[
        Optional[list[int]],
        None,
    ]

    get_targetip: Symbol[
        Optional[list[int]],
        None,
    ]

    is_broadcast: Symbol[
        Optional[list[int]],
        None,
    ]

    is_multicast: Symbol[
        Optional[list[int]],
        None,
    ]

    ip_isme: Symbol[
        Optional[list[int]],
        None,
    ]

    maccmp: Symbol[
        Optional[list[int]],
        None,
    ]

    send_packet: Symbol[
        Optional[list[int]],
        None,
    ]

    put_in_buffer: Symbol[
        Optional[list[int]],
        None,
    ]

    Cpsi_RecvCallbackFunc: Symbol[
        Optional[list[int]],
        None,
    ]

    receive_packet: Symbol[
        Optional[list[int]],
        None,
    ]

    throw_packet: Symbol[
        Optional[list[int]],
        None,
    ]

    inq_arpcache: Symbol[
        Optional[list[int]],
        None,
    ]

    send_arprequest: Symbol[
        Optional[list[int]],
        None,
    ]

    arprequest: Symbol[
        Optional[list[int]],
        None,
    ]

    reg_arpcache: Symbol[
        Optional[list[int]],
        None,
    ]

    send_ether: Symbol[
        Optional[list[int]],
        None,
    ]

    send_ip_frag: Symbol[
        Optional[list[int]],
        None,
    ]

    send_ip: Symbol[
        Optional[list[int]],
        None,
    ]

    send_ping: Symbol[
        Optional[list[int]],
        None,
    ]

    send_udp: Symbol[
        Optional[list[int]],
        None,
    ]

    send_tcp: Symbol[
        Optional[list[int]],
        None,
    ]

    reply_arp: Symbol[
        Optional[list[int]],
        None,
    ]

    dispatch_arp: Symbol[
        Optional[list[int]],
        None,
    ]

    reply_icmp: Symbol[
        Optional[list[int]],
        None,
    ]

    process_icmp_reply: Symbol[
        Optional[list[int]],
        None,
    ]

    valid_ip: Symbol[
        Optional[list[int]],
        None,
    ]

    dispatch_icmp: Symbol[
        Optional[list[int]],
        None,
    ]

    check_listener: Symbol[
        Optional[list[int]],
        None,
    ]

    check_socket: Symbol[
        Optional[list[int]],
        None,
    ]

    find_socket: Symbol[
        Optional[list[int]],
        None,
    ]

    parse_mss: Symbol[
        Optional[list[int]],
        None,
    ]

    no_need_inq: Symbol[
        Optional[list[int]],
        None,
    ]

    tcp_send_handshake: Symbol[
        Optional[list[int]],
        None,
    ]

    tcp_send_ack: Symbol[
        Optional[list[int]],
        None,
    ]

    tcp_send_finack: Symbol[
        Optional[list[int]],
        None,
    ]

    tcp_send_rst: Symbol[
        Optional[list[int]],
        None,
    ]

    dt_syn_listen: Symbol[
        Optional[list[int]],
        None,
    ]

    find_specific_socket: Symbol[
        Optional[list[int]],
        None,
    ]

    dt_syn: Symbol[
        Optional[list[int]],
        None,
    ]

    dt_synack: Symbol[
        Optional[list[int]],
        None,
    ]

    dt_ack: Symbol[
        Optional[list[int]],
        None,
    ]

    dt_fin: Symbol[
        Optional[list[int]],
        None,
    ]

    dt_rst: Symbol[
        Optional[list[int]],
        None,
    ]

    dispatch_tcp: Symbol[
        Optional[list[int]],
        None,
    ]

    dispatch_udp: Symbol[
        Optional[list[int]],
        None,
    ]

    check_frag: Symbol[
        Optional[list[int]],
        None,
    ]

    dispatch_ip: Symbol[
        Optional[list[int]],
        None,
    ]

    tcpip: Symbol[
        Optional[list[int]],
        None,
    ]

    Cps_SocGetEport: Symbol[
        Optional[list[int]],
        None,
    ]

    get_seqno: Symbol[
        Optional[list[int]],
        None,
    ]

    Cps_SocRegister: Symbol[
        Optional[list[int]],
        None,
    ]

    Cps_SocUnRegister: Symbol[
        Optional[list[int]],
        None,
    ]

    Cps_SocDatagramMode: Symbol[
        Optional[list[int]],
        None,
    ]

    Cps_SocBind: Symbol[
        Optional[list[int]],
        None,
    ]

    Cps_SocUse: Symbol[
        Optional[list[int]],
        None,
    ]

    Cps_SocRelease: Symbol[
        Optional[list[int]],
        None,
    ]

    Cps_SocDup: Symbol[
        Optional[list[int]],
        None,
    ]

    Cps_SetUdpCallback: Symbol[
        Optional[list[int]],
        None,
    ]

    Cpsi_TcpConnectRaw: Symbol[
        Optional[list[int]],
        None,
    ]

    Cps_TcpConnect: Symbol[
        Optional[list[int]],
        None,
    ]

    Cpsi_TcpShutdownRaw: Symbol[
        Optional[list[int]],
        None,
    ]

    Cps_TcpShutdown: Symbol[
        Optional[list[int]],
        None,
    ]

    Cps_TcpClose: Symbol[
        Optional[list[int]],
        None,
    ]

    udp_read_raw: Symbol[
        Optional[list[int]],
        None,
    ]

    Cpsi_TcpReadRaw: Symbol[
        Optional[list[int]],
        None,
    ]

    Cps_SocRead: Symbol[
        Optional[list[int]],
        None,
    ]

    Cpsi_SocConsumeRaw: Symbol[
        Optional[list[int]],
        None,
    ]

    Cps_SocConsume: Symbol[
        Optional[list[int]],
        None,
    ]

    tcp_write_do: Symbol[
        Optional[list[int]],
        None,
    ]

    tcp_write_do2: Symbol[
        Optional[list[int]],
        None,
    ]

    Cpsi_TcpWrite2Raw: Symbol[
        Optional[list[int]],
        None,
    ]

    Cpsi_SocWrite2: Symbol[
        Optional[list[int]],
        None,
    ]

    Cps_SocWrite: Symbol[
        Optional[list[int]],
        None,
    ]

    Cps_SocGetLength: Symbol[
        Optional[list[int]],
        None,
    ]

    Cps_SocFlush: Symbol[
        Optional[list[int]],
        None,
    ]

    set_fixed_ip: Symbol[
        Optional[list[int]],
        None,
    ]

    scavenger: Symbol[
        Optional[list[int]],
        None,
    ]

    dhcp_setcommon: Symbol[
        Optional[list[int]],
        None,
    ]

    pad_mem: Symbol[
        Optional[list[int]],
        None,
    ]

    dhcp_send_discover: Symbol[
        Optional[list[int]],
        None,
    ]

    dhcp_send_request: Symbol[
        Optional[list[int]],
        None,
    ]

    dhcp_analyze_response: Symbol[
        Optional[list[int]],
        None,
    ]

    dhcp_discover_server: Symbol[
        Optional[list[int]],
        None,
    ]

    dhcp_request_server: Symbol[
        Optional[list[int]],
        None,
    ]

    dhcp_release_server: Symbol[
        Optional[list[int]],
        None,
    ]

    dns_skipname: Symbol[
        Optional[list[int]],
        None,
    ]

    resolve_common: Symbol[
        Optional[list[int]],
        None,
    ]

    strtol10: Symbol[
        Optional[list[int]],
        None,
    ]

    rawip: Symbol[
        Optional[list[int]],
        None,
    ]

    resolve_sub: Symbol[
        Optional[list[int]],
        None,
    ]

    Cps_Resolve: Symbol[
        Optional[list[int]],
        None,
    ]

    Socl_Startup: Symbol[
        Optional[list[int]],
        None,
    ]

    Socli_StartupSocl: Symbol[
        Optional[list[int]],
        None,
    ]

    Socli_StartupCps: Symbol[
        Optional[list[int]],
        None,
    ]

    Socli_SetMyIP: Symbol[
        Optional[list[int]],
        None,
    ]

    Socli_DhcpTimeout: Symbol[
        Optional[list[int]],
        None,
    ]

    Socl_LinkIsOn: Symbol[
        Optional[list[int]],
        None,
    ]

    Socli_StartupCommandPacketQueue: Symbol[
        Optional[list[int]],
        None,
    ]

    Socli_CleanupCommandPacketQueue: Symbol[
        Optional[list[int]],
        None,
    ]

    Socli_AllocCommandPacket: Symbol[
        Optional[list[int]],
        None,
    ]

    Socli_CreateCommandPacket: Symbol[
        Optional[list[int]],
        None,
    ]

    Socli_FreeCommandPacket: Symbol[
        Optional[list[int]],
        None,
    ]

    Socli_GetCtrlPipe: Symbol[
        Optional[list[int]],
        None,
    ]

    Socli_SendCommandPacket: Symbol[
        Optional[list[int]],
        None,
    ]

    Socli_SendCommandPacketToCtrlPipe: Symbol[
        Optional[list[int]],
        None,
    ]

    Socli_ExecCommandPacket: Symbol[
        Optional[list[int]],
        None,
    ]

    Socli_ExecCommandPacketInRecvPipe: Symbol[
        Optional[list[int]],
        None,
    ]

    Socli_ExecCommandPacketInSendPipe: Symbol[
        Optional[list[int]],
        None,
    ]

    Socli_ExecCommandPacketInCtrlPipe: Symbol[
        Optional[list[int]],
        None,
    ]

    Socli_CommandPacketHandler: Symbol[
        Optional[list[int]],
        None,
    ]

    Socl_CreateSocket: Symbol[
        Optional[list[int]],
        None,
    ]

    Socli_CreateSocketCallBack: Symbol[
        Optional[list[int]],
        None,
    ]

    Socli_StartupSocket: Symbol[
        Optional[list[int]],
        None,
    ]

    Socli_GetSizeSocket: Symbol[
        Optional[list[int]],
        None,
    ]

    Socli_GetSizeCommandPipe: Symbol[
        Optional[list[int]],
        None,
    ]

    Socli_InitSocket: Symbol[
        Optional[list[int]],
        None,
    ]

    Socli_InitSocketBuffer: Symbol[
        Optional[list[int]],
        None,
    ]

    Socli_InitCommandPipe: Symbol[
        Optional[list[int]],
        None,
    ]

    Socl_Bind: Symbol[
        Optional[list[int]],
        None,
    ]

    Socl_Connect: Symbol[
        Optional[list[int]],
        None,
    ]

    Socli_ExecBindCommand: Symbol[
        Optional[list[int]],
        None,
    ]

    Socli_BindCallBack: Symbol[
        Optional[list[int]],
        None,
    ]

    Socl_ReadFrom: Symbol[
        Optional[list[int]],
        None,
    ]

    Socli_ReadAndConsumeBuffer: Symbol[
        Optional[list[int]],
        None,
    ]

    Socli_ReadBuffer: Symbol[
        Optional[list[int]],
        None,
    ]

    Socli_CopyCpsBuffer: Symbol[
        Optional[list[int]],
        None,
    ]

    Socli_ReadCpsBuffer: Symbol[
        Optional[list[int]],
        None,
    ]

    Socli_ExecReadCommand: Symbol[
        Optional[list[int]],
        None,
    ]

    Socli_ReadCallBack: Symbol[
        Optional[list[int]],
        None,
    ]

    Socli_ConsumeBuffer: Symbol[
        Optional[list[int]],
        None,
    ]

    Socli_ConsumeCallBack: Symbol[
        Optional[list[int]],
        None,
    ]

    Socli_ConsumeCpsBuffer: Symbol[
        Optional[list[int]],
        None,
    ]

    Socli_ReadUdpBuffer: Symbol[
        Optional[list[int]],
        None,
    ]

    Socli_UdpRecvCallback: Symbol[
        Optional[list[int]],
        None,
    ]

    Socl_WriteTo: Symbol[
        Optional[list[int]],
        None,
    ]

    Socli_WriteBuffer: Symbol[
        Optional[list[int]],
        None,
    ]

    Socli_AllocWriteBuffer: Symbol[
        Optional[list[int]],
        None,
    ]

    Socli_GetWriteBufferFreeSize: Symbol[
        Optional[list[int]],
        None,
    ]

    Socli_ExecWriteCommand: Symbol[
        Optional[list[int]],
        None,
    ]

    Socli_WriteCallBack: Symbol[
        Optional[list[int]],
        None,
    ]

    Socli_GetOptimumSendBufLen: Symbol[
        Optional[list[int]],
        None,
    ]

    Socli_MemCpy: Symbol[
        Optional[list[int]],
        None,
    ]

    Socl_Shutdown: Symbol[
        Optional[list[int]],
        None,
    ]

    Socli_ShutdownCallBack: Symbol[
        Optional[list[int]],
        None,
    ]

    Socl_IsClosed: Symbol[
        Optional[list[int]],
        None,
    ]

    close: Symbol[
        Optional[list[int]],
        None,
    ]

    Socli_CloseCallBack: Symbol[
        Optional[list[int]],
        None,
    ]

    Socli_CleanupSocket: Symbol[
        Optional[list[int]],
        None,
    ]

    Socli_FreeCommandPipe: Symbol[
        Optional[list[int]],
        None,
    ]

    Socli_TrashSocket: Symbol[
        Optional[list[int]],
        None,
    ]

    Soc_Cleanup: Symbol[
        Optional[list[int]],
        None,
    ]

    Socl_CloseAll: Symbol[
        Optional[list[int]],
        None,
    ]

    Socl_CalmDown: Symbol[
        Optional[list[int]],
        None,
    ]

    Socl_Resolve: Symbol[
        Optional[list[int]],
        None,
    ]

    Socl_InetAtoH: Symbol[
        Optional[list[int]],
        None,
    ]

    Socl_SetResolver: Symbol[
        Optional[list[int]],
        None,
    ]

    Socl_GetHostID: Symbol[
        Optional[list[int]],
        None,
    ]

    Socl_GetStatus: Symbol[
        Optional[list[int]],
        None,
    ]

    Socli_GetReadBufferOccpiedSize: Symbol[
        Optional[list[int]],
        None,
    ]

    Socli_RoundUp4: Symbol[
        Optional[list[int]],
        None,
    ]

    Socli_SocketRegister: Symbol[
        Optional[list[int]],
        None,
    ]

    Socli_SocketRegisterList: Symbol[
        Optional[list[int]],
        None,
    ]

    Socli_SocketRegisterTrash: Symbol[
        Optional[list[int]],
        None,
    ]

    Socli_SocketUnregister: Symbol[
        Optional[list[int]],
        None,
    ]

    Socli_SocketUnregisterList: Symbol[
        Optional[list[int]],
        None,
    ]

    Socli_SocketGetNextPtr: Symbol[
        Optional[list[int]],
        None,
    ]

    Socli_SocketUnregisterTrash: Symbol[
        Optional[list[int]],
        None,
    ]

    Socl_SocketIsInvalid: Symbol[
        Optional[list[int]],
        None,
    ]

    Socl_SocketIsInTrash: Symbol[
        Optional[list[int]],
        None,
    ]

    Soc_Socket: Symbol[
        Optional[list[int]],
        None,
    ]

    Soc_Bind: Symbol[
        Optional[list[int]],
        None,
    ]

    Soc_Connect: Symbol[
        Optional[list[int]],
        None,
    ]

    Soc_Recv: Symbol[
        Optional[list[int]],
        None,
    ]

    Soc_RecvFrom: Symbol[
        Optional[list[int]],
        None,
    ]

    Soc_Send: Symbol[
        Optional[list[int]],
        None,
    ]

    Soc_SendTo: Symbol[
        Optional[list[int]],
        None,
    ]

    Soc_Shutdown: Symbol[
        Optional[list[int]],
        None,
    ]

    Soc_Close: Symbol[
        Optional[list[int]],
        None,
    ]

    Soc_GetHostByName: Symbol[
        Optional[list[int]],
        None,
    ]

    Soc_GetSockName: Symbol[
        Optional[list[int]],
        None,
    ]

    Soc_GetHostID: Symbol[
        Optional[list[int]],
        None,
    ]

    Soc_SetResolver: Symbol[
        Optional[list[int]],
        None,
    ]

    Soc_Fcntl: Symbol[
        Optional[list[int]],
        None,
    ]

    AllocFunc_Socl: Symbol[
        Optional[list[int]],
        None,
    ]

    FreeFunc_Socl: Symbol[
        Optional[list[int]],
        None,
    ]

    Soc_Startup: Symbol[
        Optional[list[int]],
        None,
    ]

    Soc_InetNtoA: Symbol[
        Optional[list[int]],
        None,
    ]

    Soc_InetAtoN: Symbol[
        Optional[list[int]],
        None,
    ]

    Soc_InetNtoP: Symbol[
        Optional[list[int]],
        None,
    ]

    Soc_U32to4U8: Symbol[
        Optional[list[int]],
        None,
    ]

    Soc_Poll: Symbol[
        Optional[list[int]],
        None,
    ]

    Socl_EnableSsl: Symbol[
        Optional[list[int]],
        None,
    ]

    Socli_ExecEnableSslCommand: Symbol[
        Optional[list[int]],
        None,
    ]

    Socli_EnableSslCallBack: Symbol[
        Optional[list[int]],
        None,
    ]

    find_session_from_id: Symbol[
        Optional[list[int]],
        None,
    ]

    find_session_from_ip: Symbol[
        Optional[list[int]],
        None,
    ]

    cache_session: Symbol[
        Optional[list[int]],
        None,
    ]

    purge_session: Symbol[
        Optional[list[int]],
        None,
    ]

    date2sec: Symbol[
        Optional[list[int]],
        None,
    ]

    Cps_GetSslLowThreadPriority: Symbol[
        Optional[list[int]],
        None,
    ]

    Cps_SetSslLowThreadPriority: Symbol[
        Optional[list[int]],
        None,
    ]

    enter_computebound: Symbol[
        Optional[list[int]],
        None,
    ]

    exit_computebound: Symbol[
        Optional[list[int]],
        None,
    ]

    Cps_SetRootCa: Symbol[
        Optional[list[int]],
        None,
    ]

    Get_RootCA: Symbol[
        Optional[list[int]],
        None,
    ]

    cert_item_len: Symbol[
        Optional[list[int]],
        None,
    ]

    make_dn: Symbol[
        Optional[list[int]],
        None,
    ]

    parse_time: Symbol[
        Optional[list[int]],
        None,
    ]

    cert_item: Symbol[
        Optional[list[int]],
        None,
    ]

    validate_signature: Symbol[
        Optional[list[int]],
        None,
    ]

    auth_cert: Symbol[
        Optional[list[int]],
        None,
    ]

    chars_till_end: Symbol[
        Optional[list[int]],
        None,
    ]

    compare_fqdn: Symbol[
        Optional[list[int]],
        None,
    ]

    rcv_certificate: Symbol[
        Optional[list[int]],
        None,
    ]

    rcv_server_hello: Symbol[
        Optional[list[int]],
        None,
    ]

    has_method: Symbol[
        Optional[list[int]],
        None,
    ]

    select_method: Symbol[
        Optional[list[int]],
        None,
    ]

    version_ok: Symbol[
        Optional[list[int]],
        None,
    ]

    client_hello_v2: Symbol[
        Optional[list[int]],
        None,
    ]

    decrypt_premaster_secret: Symbol[
        Optional[list[int]],
        None,
    ]

    create_ms_sub: Symbol[
        Optional[list[int]],
        None,
    ]

    create_master_secret: Symbol[
        Optional[list[int]],
        None,
    ]

    create_key_block: Symbol[
        Optional[list[int]],
        None,
    ]

    rcv_client_key_exchange: Symbol[
        Optional[list[int]],
        None,
    ]

    finished_md5: Symbol[
        Optional[list[int]],
        None,
    ]

    finished_sha1: Symbol[
        Optional[list[int]],
        None,
    ]

    rcv_finished: Symbol[
        Optional[list[int]],
        None,
    ]

    add1_be8: Symbol[
        Optional[list[int]],
        None,
    ]

    decrypt: Symbol[
        Optional[list[int]],
        None,
    ]

    make_plaintext: Symbol[
        Optional[list[int]],
        None,
    ]

    make_ciphertext: Symbol[
        Optional[list[int]],
        None,
    ]

    tcp_read_raw_nbytes: Symbol[
        Optional[list[int]],
        None,
    ]

    update_digest: Symbol[
        Optional[list[int]],
        None,
    ]

    parse_record_in_buf: Symbol[
        Optional[list[int]],
        None,
    ]

    parse_record: Symbol[
        Optional[list[int]],
        None,
    ]

    set_random: Symbol[
        Optional[list[int]],
        None,
    ]

    Cps_SslAddRandomSeed: Symbol[
        Optional[list[int]],
        None,
    ]

    send_change_cipher_spec_and_finished: Symbol[
        Optional[list[int]],
        None,
    ]

    send_client_hello: Symbol[
        Optional[list[int]],
        None,
    ]

    send_client_key_exchange: Symbol[
        Optional[list[int]],
        None,
    ]

    mustget_change_cipher_spec_and_finished: Symbol[
        Optional[list[int]],
        None,
    ]

    ssl_listen_try: Symbol[
        Optional[list[int]],
        None,
    ]

    Cpsi_SslConnect: Symbol[
        Optional[list[int]],
        None,
    ]

    Cpsi_SslRead: Symbol[
        Optional[list[int]],
        None,
    ]

    Cpsi_SslConsume: Symbol[
        Optional[list[int]],
        None,
    ]

    try_fill_record: Symbol[
        Optional[list[int]],
        None,
    ]

    Cpsi_SslGetLength: Symbol[
        Optional[list[int]],
        None,
    ]

    Cpsi_SslWrite2: Symbol[
        Optional[list[int]],
        None,
    ]

    Cpsi_SslShutdown: Symbol[
        Optional[list[int]],
        None,
    ]

    Cpsi_SslClose: Symbol[
        Optional[list[int]],
        None,
    ]

    Cps_SetSsl: Symbol[
        Optional[list[int]],
        None,
    ]

    Cpsi_SslPeriodical: Symbol[
        Optional[list[int]],
        None,
    ]

    Cpsi_SslCleanup: Symbol[
        Optional[list[int]],
        None,
    ]

    char_from_long_md5: Symbol[
        Optional[list[int]],
        None,
    ]

    long_from_char_md5: Symbol[
        Optional[list[int]],
        None,
    ]

    Cpsi_Md5_Block: Symbol[
        Optional[list[int]],
        None,
    ]

    Cpsi_Md5_Init: Symbol[
        Optional[list[int]],
        None,
    ]

    Cpsi_Md5_Calc: Symbol[
        Optional[list[int]],
        None,
    ]

    Cpsi_Md5_Result: Symbol[
        Optional[list[int]],
        None,
    ]

    Cpsi_Sha1_Block_Helper: Symbol[
        Optional[list[int]],
        None,
    ]

    char_from_long_sha1: Symbol[
        Optional[list[int]],
        None,
    ]

    long_from_char_sha1: Symbol[
        Optional[list[int]],
        None,
    ]

    Cpsi_Sha1_Block: Symbol[
        Optional[list[int]],
        None,
    ]

    Cpsi_Sha1_Init: Symbol[
        Optional[list[int]],
        None,
    ]

    Cpsi_Sha1_Calc: Symbol[
        Optional[list[int]],
        None,
    ]

    Cpsi_Sha1_Result: Symbol[
        Optional[list[int]],
        None,
    ]

    Cpsi_Sha1_Result_Prng: Symbol[
        Optional[list[int]],
        None,
    ]

    Cpsi_Rc4_Init: Symbol[
        Optional[list[int]],
        None,
    ]

    Cpsi_Rc4_Crypt: Symbol[
        Optional[list[int]],
        None,
    ]

    count_digits: Symbol[
        Optional[list[int]],
        None,
    ]

    Cpsi_Big_Sign: Symbol[
        Optional[list[int]],
        None,
    ]

    Cpsi_Big_Add: Symbol[
        Optional[list[int]],
        None,
    ]

    Cpsi_Big_Add_Small: Symbol[
        Optional[list[int]],
        None,
    ]

    Cpsi_Big_Negate: Symbol[
        Optional[list[int]],
        None,
    ]

    Cpsi_Big_Sub: Symbol[
        Optional[list[int]],
        None,
    ]

    Cpsi_Big_Sub_Small: Symbol[
        Optional[list[int]],
        None,
    ]

    Cpsi_Big_Compare: Symbol[
        Optional[list[int]],
        None,
    ]

    Cpsi_Big_Add_Part: Symbol[
        Optional[list[int]],
        None,
    ]

    Cpsi_Big_Mult: Symbol[
        Optional[list[int]],
        None,
    ]

    Cpsi_Big_Mult_Small: Symbol[
        Optional[list[int]],
        None,
    ]

    Cpsi_Big_Sqr: Symbol[
        Optional[list[int]],
        None,
    ]

    get48bits_1: Symbol[
        Optional[list[int]],
        None,
    ]

    get48bits_2: Symbol[
        Optional[list[int]],
        None,
    ]

    get48bits_3: Symbol[
        Optional[list[int]],
        None,
    ]

    get64bits: Symbol[
        Optional[list[int]],
        None,
    ]

    Cpsi_Big_Div: Symbol[
        Optional[list[int]],
        None,
    ]

    Cpsi_Big_Power: Symbol[
        Optional[list[int]],
        None,
    ]

    Cpsi_Big_Modinv: Symbol[
        Optional[list[int]],
        None,
    ]

    Cpsi_Big_Montmult: Symbol[
        Optional[list[int]],
        None,
    ]

    Cpsi_Big_Montpower: Symbol[
        Optional[list[int]],
        None,
    ]

    Cpsi_Big_From_Char: Symbol[
        Optional[list[int]],
        None,
    ]

    Cpsi_Char_From_Big: Symbol[
        Optional[list[int]],
        None,
    ]

    MD5Init_Ghi: Symbol[
        Optional[list[int]],
        None,
    ]

    MD5Update_Ghi: Symbol[
        Optional[list[int]],
        None,
    ]

    MD5Final_Ghi: Symbol[
        Optional[list[int]],
        None,
    ]

    Wcm_Init: Symbol[
        Optional[list[int]],
        None,
    ]

    Wcm_Finish: Symbol[
        Optional[list[int]],
        None,
    ]

    Wcm_StartupAsync: Symbol[
        Optional[list[int]],
        None,
    ]

    Wcm_CleanupAsync: Symbol[
        Optional[list[int]],
        None,
    ]

    Wcm_SearchAsync: Symbol[
        Optional[list[int]],
        None,
    ]

    Wcm_BeginSearchAsync: Symbol[
        Optional[list[int]],
        None,
    ]

    Wcm_EndSearchAsync: Symbol[
        Optional[list[int]],
        None,
    ]

    Wcm_ConnectAsync: Symbol[
        Optional[list[int]],
        None,
    ]

    Wcm_DisconnectAsync: Symbol[
        Optional[list[int]],
        None,
    ]

    Wcm_TerminateAsync: Symbol[
        Optional[list[int]],
        None,
    ]

    Wcm_GetPhase: Symbol[
        Optional[list[int]],
        None,
    ]

    Wcm_UpdateOption: Symbol[
        Optional[list[int]],
        None,
    ]

    Wcmi_GetSystemWork: Symbol[
        Optional[list[int]],
        None,
    ]

    WcmConfigure: Symbol[
        Optional[list[int]],
        None,
    ]

    WcmEditScanExParam: Symbol[
        Optional[list[int]],
        None,
    ]

    WcmInitOption: Symbol[
        Optional[list[int]],
        None,
    ]

    WcmGetNextScanChannel: Symbol[
        Optional[list[int]],
        None,
    ]

    WcmNotify: Symbol[
        Optional[list[int]],
        None,
    ]

    WcmNotifyEx: Symbol[
        Optional[list[int]],
        None,
    ]

    WcmSetPhase: Symbol[
        Optional[list[int]],
        None,
    ]

    Wcmi_ResetKeepAliveAlarm: Symbol[
        Optional[list[int]],
        None,
    ]

    WcmKeepAliveAlarm: Symbol[
        Optional[list[int]],
        None,
    ]

    WcmCountBits: Symbol[
        Optional[list[int]],
        None,
    ]

    WcmCountLeadingZero: Symbol[
        Optional[list[int]],
        None,
    ]

    WcmWmReset: Symbol[
        Optional[list[int]],
        None,
    ]

    WcmWmcbIndication: Symbol[
        Optional[list[int]],
        None,
    ]

    WcmWmcbCommon: Symbol[
        Optional[list[int]],
        None,
    ]

    WcmWmcbScanEx: Symbol[
        Optional[list[int]],
        None,
    ]

    WcmWmcbEndScan: Symbol[
        Optional[list[int]],
        None,
    ]

    WcmWmcbConnect: Symbol[
        Optional[list[int]],
        None,
    ]

    WcmWmcbDisconnect: Symbol[
        Optional[list[int]],
        None,
    ]

    WcmWmcbStartDcf: Symbol[
        Optional[list[int]],
        None,
    ]

    WcmWmcbEndDcf: Symbol[
        Optional[list[int]],
        None,
    ]

    WcmWmcbReset: Symbol[
        Optional[list[int]],
        None,
    ]

    Wcm_ClearApList: Symbol[
        Optional[list[int]],
        None,
    ]

    Wcm_CountApList: Symbol[
        Optional[list[int]],
        None,
    ]

    Wcm_LockApList: Symbol[
        Optional[list[int]],
        None,
    ]

    Wcm_PointApList: Symbol[
        Optional[list[int]],
        None,
    ]

    Wcmi_EntryApList: Symbol[
        Optional[list[int]],
        None,
    ]

    WcmAllocApList: Symbol[
        Optional[list[int]],
        None,
    ]

    WcmGetOldestApList: Symbol[
        Optional[list[int]],
        None,
    ]

    WcmSearchApList: Symbol[
        Optional[list[int]],
        None,
    ]

    WcmSearchIndexedApList: Symbol[
        Optional[list[int]],
        None,
    ]

    WcmAppendApList: Symbol[
        Optional[list[int]],
        None,
    ]

    Wcmi_InitCpsif: Symbol[
        Optional[list[int]],
        None,
    ]

    Wcmi_CpsifRecvCallback: Symbol[
        Optional[list[int]],
        None,
    ]

    Wcmi_CpsifSendNullPacket: Symbol[
        Optional[list[int]],
        None,
    ]

    Wcm_GetApMacAddress: Symbol[
        Optional[list[int]],
        None,
    ]

    Wcm_GetApEssid: Symbol[
        Optional[list[int]],
        None,
    ]

    Wcm_SetRecvDcfCallback: Symbol[
        Optional[list[int]],
        None,
    ]

    Wcm_SendDcfData: Symbol[
        Optional[list[int]],
        None,
    ]

    WcmCpsifWmCallback: Symbol[
        Optional[list[int]],
        None,
    ]

    WcmCpsifKaCallback: Symbol[
        Optional[list[int]],
        None,
    ]

    WcmCpsifTryLockMutexInIrq: Symbol[
        Optional[list[int]],
        None,
    ]

    WcmCpsifUnlockMutexInIrq: Symbol[
        Optional[list[int]],
        None,
    ]

    Wcm_CompareBssID: Symbol[
        Optional[list[int]],
        None,
    ]

    Wcm_GetLinkLevel: Symbol[
        Optional[list[int]],
        None,
    ]

    Wcmi_GetRssiAverage: Symbol[
        Optional[list[int]],
        None,
    ]

    WcmGetLinkLevel: Symbol[
        Optional[list[int]],
        None,
    ]

    Wcmi_ShelterRssi: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwc_AC_Create: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwc_AC_Process: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwc_AC_GetStatus: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwc_AC_GetApType: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwc_AC_GetApSpotInfo: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwc_AC_Destroy: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwc_AC_SetSpecifyAp: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwc_AC_SetSpecifyApEx: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_AC_InsertApInfo: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_AC_Alloc: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_AC_Free: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_AC_FreeAll: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_AC_GetMemPtr: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_AC_SetPhase: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_AC_GetPhase: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_AC_SetError: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_AC_GetError: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_AC_SetApType: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_ConvConnectApType: Symbol[
        Optional[list[int]],
        None,
    ]

    Free_Disused_Dwc: Symbol[
        Optional[list[int]],
        None,
    ]

    CheckDuplicate_Dwc: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_AC_GetBeacon: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_AC_CheckNintendoSsid: Symbol[
        Optional[list[int]],
        None,
    ]

    CompareList_Dwc: Symbol[
        Optional[list[int]],
        None,
    ]

    CompareListDiff_Dwc: Symbol[
        Optional[list[int]],
        None,
    ]

    AddList_Dwc: Symbol[
        Optional[list[int]],
        None,
    ]

    SetDataListTail_Dwc: Symbol[
        Optional[list[int]],
        None,
    ]

    UpDateList_Dwc: Symbol[
        Optional[list[int]],
        None,
    ]

    SortList_Dwc: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_AC_CallBackWcm: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_AC_ConnectAP: Symbol[
        Optional[list[int]],
        None,
    ]

    ConnectStart_Dwc: Symbol[
        Optional[list[int]],
        None,
    ]

    ConnectAP_Dwc: Symbol[
        Optional[list[int]],
        None,
    ]

    GetConnectType_Dwc: Symbol[
        Optional[list[int]],
        None,
    ]

    GetPowerMode_Dwc: Symbol[
        Optional[list[int]],
        None,
    ]

    GetAuthMode_Dwc: Symbol[
        Optional[list[int]],
        None,
    ]

    GetWepKey_Dwc: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_AC_CloseNetwork: Symbol[
        Optional[list[int]],
        None,
    ]

    DisConnectAP_Dwc: Symbol[
        Optional[list[int]],
        None,
    ]

    CloseSocket_Dwc: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_AC_Error: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_AC_GetResult: Symbol[
        Optional[list[int]],
        None,
    ]

    GetProgramaError_Dwc: Symbol[
        Optional[list[int]],
        None,
    ]

    GetIrregularError_Dwc: Symbol[
        Optional[list[int]],
        None,
    ]

    GetNotFoundAP_Dwc: Symbol[
        Optional[list[int]],
        None,
    ]

    GetNotFoundInet_Dwc: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_AC_MakeSearchList: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_AC_CheckFreespot: Symbol[
        Optional[list[int]],
        None,
    ]

    MakeAroundList_Dwc: Symbol[
        Optional[list[int]],
        None,
    ]

    MakeStealthList_Dwc: Symbol[
        Optional[list[int]],
        None,
    ]

    MakeUserList_Dwc: Symbol[
        Optional[list[int]],
        None,
    ]

    MakeDifferChannelList_Dwc: Symbol[
        Optional[list[int]],
        None,
    ]

    CheckDifferChannelStart_Dwc: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_AC_ConnectRetryAP: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_AC_SearchAP: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_AC_SetStealthChannel: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_AC_GetStealthChannel: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_AC_SearchReStart: Symbol[
        Optional[list[int]],
        None,
    ]

    SearchStart_Dwc: Symbol[
        Optional[list[int]],
        None,
    ]

    SearchAround_Dwc: Symbol[
        Optional[list[int]],
        None,
    ]

    SearchAround2ndLap_Dwc: Symbol[
        Optional[list[int]],
        None,
    ]

    SearchDifferChannel_Dwc: Symbol[
        Optional[list[int]],
        None,
    ]

    SearchStealth_Dwc: Symbol[
        Optional[list[int]],
        None,
    ]

    NextSearchCheck_Dwc: Symbol[
        Optional[list[int]],
        None,
    ]

    SearchEndCheck_Dwc: Symbol[
        Optional[list[int]],
        None,
    ]

    CheckStartStealthSearch_Dwc: Symbol[
        Optional[list[int]],
        None,
    ]

    ScanStart_Dwc: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_AC_Start: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_AC_ConnectTest: Symbol[
        Optional[list[int]],
        None,
    ]

    ConnectTestStart_Dwc: Symbol[
        Optional[list[int]],
        None,
    ]

    GetIpAddress_Dwc: Symbol[
        Optional[list[int]],
        None,
    ]

    ConnectTestCreate_Dwc: Symbol[
        Optional[list[int]],
        None,
    ]

    ConnectTestProcess_Dwc: Symbol[
        Optional[list[int]],
        None,
    ]

    ConnectTestEnd_Dwc: Symbol[
        Optional[list[int]],
        None,
    ]

    ConnectTestRetry_Dwc: Symbol[
        Optional[list[int]],
        None,
    ]

    MakeSocConfig_Dwc: Symbol[
        Optional[list[int]],
        None,
    ]

    ConvAddress_Dwc: Symbol[
        Optional[list[int]],
        None,
    ]

    ConvNetMask_Dwc: Symbol[
        Optional[list[int]],
        None,
    ]

    CheckSetDns_Dwc: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_AC_CheckNintendoShopAP: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_AC_GetNintendoShopWepKey: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_AC_GetPostalCode: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_AC_CheckNintendoUsbAP: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_AC_GetNintendoUsbWepKey: Symbol[
        Optional[list[int]],
        None,
    ]

    DecodeSsid_Dwc: Symbol[
        Optional[list[int]],
        None,
    ]

    MakeShopWepKey_Dwc: Symbol[
        Optional[list[int]],
        None,
    ]

    MakeUsbWepKey_Dwc: Symbol[
        Optional[list[int]],
        None,
    ]

    CodeToValue_Dwc: Symbol[
        Optional[list[int]],
        None,
    ]

    Db64_Dwc: Symbol[
        Optional[list[int]],
        None,
    ]

    WdsGetRssi8: Symbol[
        Optional[list[int]],
        None,
    ]

    WdsScanCallback: Symbol[
        Optional[list[int]],
        None,
    ]

    Wds_GetWorkAreaSize: Symbol[
        Optional[list[int]],
        None,
    ]

    Wds_Initialize: Symbol[
        Optional[list[int]],
        None,
    ]

    Wds_End: Symbol[
        Optional[list[int]],
        None,
    ]

    Wds_StartScan: Symbol[
        Optional[list[int]],
        None,
    ]

    Wds_EndScan: Symbol[
        Optional[list[int]],
        None,
    ]

    Wds_GetApInfoByIndex: Symbol[
        Optional[list[int]],
        None,
    ]

    Wds_GetApInfoAll: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwc_AC_StartupGetWdsInfo: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwc_AC_ProcessGetWdsInfo: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwc_AC_CancelGetWdsInfo: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwc_AC_CleanupGetWdsInfo: Symbol[
        Optional[list[int]],
        None,
    ]

    IsValidApnum: Symbol[
        Optional[list[int]],
        None,
    ]

    Wds_Initialize_CB: Symbol[
        Optional[list[int]],
        None,
    ]

    Wds_StartScan_CB: Symbol[
        Optional[list[int]],
        None,
    ]

    Wds_EndScan_CB: Symbol[
        Optional[list[int]],
        None,
    ]

    Wds_End_CB: Symbol[
        Optional[list[int]],
        None,
    ]

    Wds_Error_End_CB: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwc_Init: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_Acc_SetMaskBits: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_Acc_GetUserId: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_Acc_GetPlayerId: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_Acc_GetFriendKey: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_Acc_GetGsProfileId: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_Acc_SetUserId: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_Acc_SetPlayerId: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_Acc_SetFriendKey: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_Acc_SetGsProfileId: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_Acc_GetFlags: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_Acc_GetFlag_DataType: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwc_IsBuddyFriendData: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_IsBuddyFriendData: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_IsReverseBuddyFriendData: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_IsBuddyMsgAlreadySent: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwc_GetFriendDataType: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_Acc_SetFlags: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_Acc_SetFlag_DataType: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_SetBuddyFriendData: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_SetReverseBuddyFlag: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_SetExpIsBuddyFriendFlag: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_SetSentBuddyReqFlag: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwc_Acc_CreateFriendKey: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwc_CheckFriendKey: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwc_Acc_CheckFriendKey: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwc_Acc_FriendKeyToGsProfileId: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwc_FriendKeyToString: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_Acc_U64ToString32: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_Acc_LoginIdToUserName: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_Acc_CreateUserData: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_Acc_CreateTempLoginId: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_Acc_CheckConsoleUserId: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_Acc_IsValidLoginId: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_Acc_IsAuthentic: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwc_IsValidFriendData: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_Acc_IsValidFriendData: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwc_CreateUserData: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwc_CheckUserData: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwc_CheckHasProfile: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwc_CheckValidConsole: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_Acc_SetLoginIdToUserData: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwc_CheckDirtyFlag: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_Acc_IsDirty: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwc_ClearDirtyFlag: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_Acc_ClearDirty: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwc_GetFriendKey: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwc_GetGsProfileId: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwc_CreateFriendKey: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwc_CreateFriendKeyToken: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwc_CreateExchangeToken: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwc_SetGsProfileId: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwc_LoginIdToUserName: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwc_IsEqualFriendData: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwc_ReportFriendData: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwc_ReportUserData: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwc_Auth_SetCustomNas: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwc_Auth_GetCustomNas: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwc_Auth_Create: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_Auth_StartThread: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwc_Auth_Abort: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwc_Auth_Destroy: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwc_Auth_Join: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwc_Auth_GetError: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwc_Auth_GetResult: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_Auth_Start: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_Auth_Thread: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_Auth_ParseHttp: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_Auth_FillResult: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_Auth_Prepare_FirstPost: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_Auth_SetError: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwc_Auth_GetCalInfoFromNVram: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwc_Auth_GetCalInfoFromWiFiInfo: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwc_Auth_SetCalInfoToHttp: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwc_Http_Create: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwc_Http_FinishHeader: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwc_Http_StartThread: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwc_Http_Abort: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_Http_Yield: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_Http_InitCpsSocket: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_Http_Resolve: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_Http_CheckHeaderReceived: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_Http_Thread: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwc_Http_Destroy: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_Http_WriteBasicHeader: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwc_Http_Add_HeaderItem: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwc_Http_Add_PostBase64Item: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwc_Http_Add_Body: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_Http_CpsCallback: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_Http_AllocBuffer: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_Http_FreeBuffer: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_Http_ReallocBuffer: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_Http_SetHostinfo: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwc_Http_AddResult: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwc_Http_ParseResult: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwc_Http_GetResult: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwc_Http_GetBase64DecodedResult: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwc_Http_GetRawResult: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwc_Http_Disconnect: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwc_Netcheck_Create: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwc_Netcheck_Destroy: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwc_Netcheck_Abort: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwc_Netcheck_GetError: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwc_Netcheck_GetReturnCode: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_Netcheck_StartThread: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_Netcheck_Thread: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_Netcheck_SetError: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwc_Auth_SetNasTimeDiff: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwc_Svl_Init: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwc_Svl_Cleanup: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwc_Svl_GetTokenAsync: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwc_Svl_Process: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_Svl_ParseHttp: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwc_Auth_Base64Encode: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwc_Auth_Base64Decode: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwc_GetLastError: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwc_GetLastErrorEx: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwc_ClearError: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_IsError: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_SetError: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_GetAllocateHeader: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_SetAllocateHeader: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_GetAllocateSize: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwc_SetMemFunc: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwc_Alloc: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwc_AllocEx: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwc_Free: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwc_Realloc: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwc_ReallocEx: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_GsMalloc: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_GsRealloc: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_GsFree: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_GsMemalign: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwc_InitInetEx: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwc_InitInet: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwc_SetAuthServer: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwc_ConnectInetAsync: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwc_DebugConnectInetAsync: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwc_CheckInet: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwc_ProcessInet: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwc_GetInetStatus: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwc_CleanupInet: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwc_CleanupInetAsync: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_CheckDisconnected: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwc_GetLinkLevel: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwc_GetApInfo: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwc_UpdateConnection: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwc_GetIngamesnCheckResult: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwc_SvlGetTokenAsync: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwc_SvlProcess: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_NdAlloc: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_NdFree: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_NdCallback: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_NdCleanupCallback: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_SvlTokenWaitThread: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwc_NdInitAsync: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwc_NdCleanupAsync: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwc_NdSetAttr: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwc_NdGetFileListNumAsync: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwc_NdGetFileListAsync: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwc_NdGetFileAsync: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwc_NdCancelAsync: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwc_SetCommonKeyValueString: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwc_AddCommonKeyValueString: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwc_GetCommonValueString: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_GetMathRand32: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_WStrLen: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwc_InitFriendsMatch: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwc_ShutdownFriendsMatch: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwc_ProcessFriendsMatch: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwc_LoginAsync: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwc_UpdateServersAsync: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwc_CloseConnectionHard: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwc_GetMyAid: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwc_GetAidList: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwc_IsValidAid: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwc_GetState: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_GT2Startup: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_GetGT2Connection: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_GetConnectionAid: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_GetConnectionIndex: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_GT2GetConnectionListIdx: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_ClearGT2ConnectionList: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_GetGT2ConnectionByIdx: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_GetGT2ConnectionByProfileID: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_GetConnectionInfoByIdx: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_IsValidAid: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_ResetMyAid: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwcs_ForceShutdown: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_SetState: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_DeleteAid: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_HandleGpError_Common: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_HandleGT2Error: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_LoginCallback: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_UpdateServersCallback: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_GpErrorCallback: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_GpRecvBuddyMessageCallback: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_GT2ReceivedCallback: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_GT2ClosedCallback: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_GT2PingCallback: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_GT2SocketErrorCallback: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_LoginInit: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_LoginAsync: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_LoginProcess: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_GetUserData: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_StopLogin: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_ShutdownLogin: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_CloseLogin: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_HandleGpError_Login: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_GpConnectCallback: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_RemoteAuthCallback: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_GpConnect: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_RemoteLogin: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_RemoteLoginProcess: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_GpGetInfoCallback: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_CheckLogin: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwc_GetFriendStatus: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwc_GetFriendStatusSC: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwc_DeleteBuddyFriendData: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwc_SetBuddyFriendCallback: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_FriendInit: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_FriendProcess: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_UpdateServersAsync: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_StopFriendProcess: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_GpRecvBuddyRequestCallback: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_GpRecvBuddyAuthCallback: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_GpRecvBuddyStatusCallback: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_GetProfileIdFromList: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_GetFriendListIndex: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_InitGpProcessCount: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_SetGpStatus: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_GetGpStatus: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_ShutdownFriend: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_GpProcess: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_CloseFriendProcess: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_UpdateFriendReq: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_EndUpdateServers: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_DeleteFriendFromList: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_RefreshFriendListForth: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_RefreshFriendListAll: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_GpSendBuddyRequest: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_GetFriendBuddyStatus: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_HandleGpError_Friend: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_GpProfileSearchCallback: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_GpGetInfoCallback_RecvBuddyRequest: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_GpGetInfoCallback_RecvAuthMessage: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_GetPersCallbackLevel: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_BeginCloseStatsConnection: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_EndCloseStatsConnection: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_GetReverseBuddiesCallback: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_NnFreeNegotiateList: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_MatchInit: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_QR2Startup: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_SendStateChanged: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_MatchProcess: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_GT2UnrecognizedMessageCallback: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_GT2ConnectAttemptCallback: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_GT2ConnectedCallback: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_MatchGpRecvBuddyMsgCallback: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_StopResendingMatchCommand: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_StopMatching: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_ClearQR2Key: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_ProcessMatchSynPacket: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_ProcessMatchClosing: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_ProcessMatchScClosing: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_DeleteHostByProfileID: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_DeleteHostByIndex: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_SetNumValidConnection: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_GetAllAidList: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_GetValidAidList: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_GpSetServerStatus: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_ShutdownMatch: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_IsShutdownMatch: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_ResetMatchParam: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_CloseMatching: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_SbUpdateAsync: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_GetDefaultMatchFilter: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_NnStartupAsync: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_DoNatNegotiationAsync: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_SendMatchCommand: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_SendSbMsgCommand: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_SendGpBuddyMsgCommand: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_GetGpBuddyAdditionalMsg: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_ProcessRecvMatchCommand: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_CheckResvCommand: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_ProcessResvOK: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_MakeBackupServerData: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_HandleMatchCommandError: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_SendResvCommand: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_SendResvCommandToFriend: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_RetryReserving: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_CancelReservation: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_CancelPreConnectedServerProcess: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_CancelPreConnectedClientProcess: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_ChangeToClient: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_PostProcessConnection: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_AreAllBuddies: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_FinishCancelMatching: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_InvalidateReservation: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_RestartFromCancel: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_RestartFromTimeout: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_ResumeMatching: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_CloseCancelHostAsync: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_CloseAllConnectionsByTimeout: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_CloseShutdownClientSC: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_SendMatchSynPacket: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_ProcessMatchSynTimeout: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_SendCancelMatchSynCommand: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_ProcessCancelMatchSynCommand: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_ProcessCancelMatchSynTimeout: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_ClearGameMatchKeys: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_GetAidFromList: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_IsFriendByIdxList: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_GetAidFromProfileID: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_GetAidBitmask: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_InitClWaitTimeout: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_InitOptMinCompParam: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_ProcessOptMinComp: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_HandleGpError_Match: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_HandleSbError_Match: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_HandleQR2Error: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_HandleNnError: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_HandleNnResult: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_HandleGT2Error_Match: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_QR2ServerKeyCallback: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_QR2PlayerKeyCallback: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_QR2TeamKeyCallback: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_QR2KeyListCallback: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_QR2CountCallback: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_QR2AddErrorCallback: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_QR2PublicAddrCallback: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_QR2NatnegCallback: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_QR2ClientMsgCallback: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_NnProgressCallback: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_NnCompletedCallback: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_ProcessNnFailure: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_SetMatchCnt: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_GetMatchCnt: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_SetMatchStatus: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_InitReliableQueue: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_CleanupReliableQueue: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_IsReliableQueueFree: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_ProcessReliableQueue: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_ProcessReliableQueueEx: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_InsertReliableQueue: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwc_IsSendableReliable: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_SendReliable: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwcs_EncodeHeader: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwcs_DecodeHeader: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwcs_GetRequiredHeaderSize: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_InitTransport: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_RecvCallback: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_PingCallback: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_TransportProcess: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_ClearTransConnection: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_ShutdownTransport: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwcs_GetTransConnection: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwcs_GetSendState: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwcs_GetRecvState: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwcs_Send: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwcs_HandleReliableMessage: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwcs_HandleUnreliableMessage: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwcs_RecvDataHeader: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwcs_RecvDataBody: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwcs_RecvSystemDataBody: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwcs_GetOutgoingBufferFreeSize: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwc_InitGhttp: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwc_ShutdownGhttp: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwc_ProcessGhttp: Symbol[
        Optional[list[int]],
        None,
    ]

    GhttpCompletedCallback: Symbol[
        Optional[list[int]],
        None,
    ]

    GhttpProgressCallback: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_GhttpGetEx: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwc_GetGhttpDataEx2: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwc_CancelGhttpRequest: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_HandleGhttpError: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_AppendDwcGhttpParam: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_RemoveDwcGHttpParamEntry: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_FindDwcGhttpParamEntryByReq: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_RemoveAllDwcGhttpParamEntry: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_BM_GetApInfo: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_BM_GetWiFiInfo: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_BM_SetWiFiInfo: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_BackuplInit: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_BackuplRead: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_BackuplWritePage: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_BackuplWriteAll: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_BackuplSetWiFi: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_BackuplConvMaskCidr: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_BackuplConvMaskAddr: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwc_BackuplCheckSsid: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwc_BackuplCheckIp: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwc_BackuplCheckAddress: Symbol[
        Optional[list[int]],
        None,
    ]

    NVramm_ExecuteCommand: Symbol[
        Optional[list[int]],
        None,
    ]

    ReadNvram_Dwc: Symbol[
        Optional[list[int]],
        None,
    ]

    WriteNvram_Dwc: Symbol[
        Optional[list[int]],
        None,
    ]

    Verify_Dwc: Symbol[
        Optional[list[int]],
        None,
    ]

    WriteDisable_Dwc: Symbol[
        Optional[list[int]],
        None,
    ]

    Callback_NVram: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_BackuplConvWifiInfo: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_BackuplGetWifi: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwc_BM_Init: Symbol[
        Optional[list[int]],
        None,
    ]

    CheckAp_Dwc: Symbol[
        Optional[list[int]],
        None,
    ]

    Init_Dwc: Symbol[
        Optional[list[int]],
        None,
    ]

    InitPage_Dwc: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_Util_WiFiId_ScrambleUid: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_Auth_GetNewWiFiInfo: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_Auth_MakeWiFiID: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_Auth_UpDateWiFiID: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_Auth_RemakeWiFiID: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwc_Auth_GetId: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwc_Auth_CheckWiFiIdNeedCreate: Symbol[
        Optional[list[int]],
        None,
    ]

    b64size: Symbol[
        Optional[list[int]],
        None,
    ]

    my_randinit: Symbol[
        Optional[list[int]],
        None,
    ]

    my_rand: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_RankingValidateKey: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_RankingSessionCompleteCallback_Helper: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_RankingSessionProgressCallback: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_RankingSessionCompleteCallback: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_RankingSessionEncrypt: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_RankingSessionInitialize: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_RankingSessionProcess: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_RankingSessionCancel: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_RankingSessionShutdown: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_RankingSessionGetResponse: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_RankingSessionPutAsync: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_RankingSessionGetAsync: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_Ndi_FreeAttr: Symbol[
        Optional[list[int]],
        None,
    ]

    SetAttr_Dwc: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_NdSetAttr: Symbol[
        Optional[list[int]],
        None,
    ]

    GetNChar_Dwc: Symbol[
        Optional[list[int]],
        None,
    ]

    DecodeChar_Dwc: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_Ndi_GetDecodeLenBase64: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_Ndi_GetEncodeLenBase64: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_Ndi_EncodeBase64: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_Ndi_EecodeBase64: Symbol[
        Optional[list[int]],
        None,
    ]

    StrAlloc_Dwc: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_NdStartup: Symbol[
        Optional[list[int]],
        None,
    ]

    NhttpCleanupCallback: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_NdCleanupAsync: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_NdCancelAsync: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_Ndi_GetApInfo: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_Ndi_GetDSdesc: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_Ndi_GetUserAgent: Symbol[
        Optional[list[int]],
        None,
    ]

    Req_Callback_Dwc: Symbol[
        Optional[list[int]],
        None,
    ]

    FreeHttp: Symbol[
        Optional[list[int]],
        None,
    ]

    SetupHttp: Symbol[
        Optional[list[int]],
        None,
    ]

    RunHttp: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_NdGetFileListNumAsync: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_NdGetFileListAsync: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_NdGetFileAsync: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_Ndi_Response_Count: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_Ndi_Response_Contents: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_Ndi_Response_List: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_Ndi_InitLockGlobal: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_Ndi_ExitLockGlobal: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_Ndi_LockGlobal: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_Ndi_UnlockGlobal: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_Ndi_InitHttpCallback: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_Ndi_ExitHttpCallback: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_Ndi_PrepareHttpCallback: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_Ndi_UnprepareHttpCallback: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_Ndi_KickThread: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_Ndi_GetMacAddress: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_Ndi_Strlen: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_Ndi_Strncmp: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_Ndi_Memclr: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_Ndi_Memcpy: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_Ndi_StrToInt: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_Ndi_IntToStr: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_Ndi_IntToStrFigure: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_Ndi_HexToStrFigure: Symbol[
        Optional[list[int]],
        None,
    ]

    Nhttp_Startup: Symbol[
        Optional[list[int]],
        None,
    ]

    Nhttp_CleanupAsync: Symbol[
        Optional[list[int]],
        None,
    ]

    Nhttpi_CleanupThreadProc: Symbol[
        Optional[list[int]],
        None,
    ]

    AddHdrList_Nhttp: Symbol[
        Optional[list[int]],
        None,
    ]

    Nhttpi_GetHdrFromList: Symbol[
        Optional[list[int]],
        None,
    ]

    IncAscii_Nhttp: Symbol[
        Optional[list[int]],
        None,
    ]

    CheckTagPost_Nhttp: Symbol[
        Optional[list[int]],
        None,
    ]

    Nhttp_AddHeaderField: Symbol[
        Optional[list[int]],
        None,
    ]

    Nhttp_AddPostDataAscii: Symbol[
        Optional[list[int]],
        None,
    ]

    Nhttp_SetCaChain: Symbol[
        Optional[list[int]],
        None,
    ]

    Nhttpi_SetReqQueue: Symbol[
        Optional[list[int]],
        None,
    ]

    Nhttpi_FindReqQueue: Symbol[
        Optional[list[int]],
        None,
    ]

    Nhttpi_FreeReqQueue: Symbol[
        Optional[list[int]],
        None,
    ]

    Nhttpi_AllFreeReqQueue: Symbol[
        Optional[list[int]],
        None,
    ]

    Nhttpi_GetReqFromReqQueue: Symbol[
        Optional[list[int]],
        None,
    ]

    Nhttpi_InitLockReqList: Symbol[
        Optional[list[int]],
        None,
    ]

    Nhttpi_ExitLockReqList: Symbol[
        Optional[list[int]],
        None,
    ]

    Nhttpi_LockReqList: Symbol[
        Optional[list[int]],
        None,
    ]

    Nhttpi_UnlockReqList: Symbol[
        Optional[list[int]],
        None,
    ]

    Nhttpi_CreateCommThread: Symbol[
        Optional[list[int]],
        None,
    ]

    Nhttpi_DestroyCommThread: Symbol[
        Optional[list[int]],
        None,
    ]

    Nhttpi_IdleCommThread: Symbol[
        Optional[list[int]],
        None,
    ]

    Nhttpi_KickCommThread: Symbol[
        Optional[list[int]],
        None,
    ]

    SetupGetcharFromHdrRecvBuf: Symbol[
        Optional[list[int]],
        None,
    ]

    GetcharFromHdrRecvBuf: Symbol[
        Optional[list[int]],
        None,
    ]

    Nhttpi_FindNextLineHdrRecvBuf: Symbol[
        Optional[list[int]],
        None,
    ]

    Nhttpi_SkipSpaceHdrRecvBuf: Symbol[
        Optional[list[int]],
        None,
    ]

    Nhttpi_CompareTokenN_HdrRecvBuf: Symbol[
        Optional[list[int]],
        None,
    ]

    Nhttpi_LoadFromHdrRecvBuf: Symbol[
        Optional[list[int]],
        None,
    ]

    Nhttpi_IsRecvBufFull: Symbol[
        Optional[list[int]],
        None,
    ]

    Nhttpi_RecvBuf: Symbol[
        Optional[list[int]],
        None,
    ]

    Nhttpi_RecvBufN: Symbol[
        Optional[list[int]],
        None,
    ]

    Nhttp_CreateRequest: Symbol[
        Optional[list[int]],
        None,
    ]

    Nhttp_DestroyRequest: Symbol[
        Optional[list[int]],
        None,
    ]

    DeleteStrList: Symbol[
        Optional[list[int]],
        None,
    ]

    Nhttpi_DestroyRequestObject: Symbol[
        Optional[list[int]],
        None,
    ]

    Nhttp_SendRequestAsync: Symbol[
        Optional[list[int]],
        None,
    ]

    Nhttp_CancelRequestAsync: Symbol[
        Optional[list[int]],
        None,
    ]

    Nhttpi_CancelAllRequests: Symbol[
        Optional[list[int]],
        None,
    ]

    Nhttpi_ResolveHostname: Symbol[
        Optional[list[int]],
        None,
    ]

    Nhttp_DestroyResponse: Symbol[
        Optional[list[int]],
        None,
    ]

    Nhttpi_GetHeaderValue: Symbol[
        Optional[list[int]],
        None,
    ]

    Nhttp_GetHeaderField: Symbol[
        Optional[list[int]],
        None,
    ]

    Nhttp_GetBodyAll: Symbol[
        Optional[list[int]],
        None,
    ]

    SslAuthCallback: Symbol[
        Optional[list[int]],
        None,
    ]

    Nhttpi_SetSslseed: Symbol[
        Optional[list[int]],
        None,
    ]

    Nhttpi_SocOpen: Symbol[
        Optional[list[int]],
        None,
    ]

    Nhttpi_SocClose: Symbol[
        Optional[list[int]],
        None,
    ]

    Nhttpi_SocCloseWait: Symbol[
        Optional[list[int]],
        None,
    ]

    Nhttpi_SocConnect: Symbol[
        Optional[list[int]],
        None,
    ]

    Nhttpi_SocRecv: Symbol[
        Optional[list[int]],
        None,
    ]

    Nhttpi_SocSend: Symbol[
        Optional[list[int]],
        None,
    ]

    Nhttpi_SocCancel: Symbol[
        Optional[list[int]],
        None,
    ]

    Nhttpi_Strcmp: Symbol[
        Optional[list[int]],
        None,
    ]

    Nhttpi_Strnicmp: Symbol[
        Optional[list[int]],
        None,
    ]

    Nhttpi_Strlen: Symbol[
        Optional[list[int]],
        None,
    ]

    Nhttpi_Memclr: Symbol[
        Optional[list[int]],
        None,
    ]

    Nhttpi_Memcpy: Symbol[
        Optional[list[int]],
        None,
    ]

    SaveBuf: Symbol[
        Optional[list[int]],
        None,
    ]

    SkipLineBuf: Symbol[
        Optional[list[int]],
        None,
    ]

    FreeSslConnection: Symbol[
        Optional[list[int]],
        None,
    ]

    PutSocketToCloseQue: Symbol[
        Optional[list[int]],
        None,
    ]

    ClearCloseQue: Symbol[
        Optional[list[int]],
        None,
    ]

    Nhttpi_CommThreadProc: Symbol[
        Optional[list[int]],
        None,
    ]

    Nhttpi_GetUrlEncodedSize: Symbol[
        Optional[list[int]],
        None,
    ]

    Nhttpi_EncodeUrlChar: Symbol[
        Optional[list[int]],
        None,
    ]

    Nhttpi_StrToHex: Symbol[
        Optional[list[int]],
        None,
    ]

    Nhttpi_StrToInt: Symbol[
        Optional[list[int]],
        None,
    ]

    Nhttpi_IntToStr: Symbol[
        Optional[list[int]],
        None,
    ]

    Nhttpi_CompareToken: Symbol[
        Optional[list[int]],
        None,
    ]

    Nhttpi_StrToNum: Symbol[
        Optional[list[int]],
        None,
    ]

    Nhttpi_MemFind: Symbol[
        Optional[list[int]],
        None,
    ]

    FreeElement_Gsi: Symbol[
        Optional[list[int]],
        None,
    ]

    ArrayGrow_Gsi: Symbol[
        Optional[list[int]],
        None,
    ]

    SetElement_Gsi: Symbol[
        Optional[list[int]],
        None,
    ]

    ArrayNew_Gsi: Symbol[
        Optional[list[int]],
        None,
    ]

    ArrayFree_Gsi: Symbol[
        Optional[list[int]],
        None,
    ]

    ArrayLength_Gsi: Symbol[
        Optional[list[int]],
        None,
    ]

    ArrayNth_Gsi: Symbol[
        Optional[list[int]],
        None,
    ]

    ArrayAppend_Gsi: Symbol[
        Optional[list[int]],
        None,
    ]

    ArrayInsertAt_Gsi: Symbol[
        Optional[list[int]],
        None,
    ]

    ArrayInsertSorted_Gsi: Symbol[
        Optional[list[int]],
        None,
    ]

    ArrayRemoveAt_Gsi: Symbol[
        Optional[list[int]],
        None,
    ]

    ArrayDeleteAt_Gsi: Symbol[
        Optional[list[int]],
        None,
    ]

    ArrayReplaceAt_Gsi: Symbol[
        Optional[list[int]],
        None,
    ]

    ArraySearch_Gsi: Symbol[
        Optional[list[int]],
        None,
    ]

    ArrayMap_Gsi: Symbol[
        Optional[list[int]],
        None,
    ]

    ArrayMapBackwards_Gsi: Symbol[
        Optional[list[int]],
        None,
    ]

    ArrayClear_Gsi: Symbol[
        Optional[list[int]],
        None,
    ]

    mylsearch_gsi: Symbol[
        Optional[list[int]],
        None,
    ]

    mybsearch_gsi: Symbol[
        Optional[list[int]],
        None,
    ]

    TableNew_Gsi: Symbol[
        Optional[list[int]],
        None,
    ]

    TableNew2_Gsi: Symbol[
        Optional[list[int]],
        None,
    ]

    TableFree_Gsi: Symbol[
        Optional[list[int]],
        None,
    ]

    TableCount_Gsi: Symbol[
        Optional[list[int]],
        None,
    ]

    TableEnter_Gsi: Symbol[
        Optional[list[int]],
        None,
    ]

    TableRemove_Gsi: Symbol[
        Optional[list[int]],
        None,
    ]

    TableLookup_Gsi: Symbol[
        Optional[list[int]],
        None,
    ]

    TableMap_Gsi: Symbol[
        Optional[list[int]],
        None,
    ]

    TableMapSafe2_Gsi: Symbol[
        Optional[list[int]],
        None,
    ]

    MD5Print_Gsi: Symbol[
        Optional[list[int]],
        None,
    ]

    MD5Digest_Gsi: Symbol[
        Optional[list[int]],
        None,
    ]

    CheckRCode_Gsi: Symbol[
        Optional[list[int]],
        None,
    ]

    socket_gsi: Symbol[
        Optional[list[int]],
        None,
    ]

    closesocket_gsi: Symbol[
        Optional[list[int]],
        None,
    ]

    shutdown_gsi: Symbol[
        Optional[list[int]],
        None,
    ]

    bind_gsi: Symbol[
        Optional[list[int]],
        None,
    ]

    connect_gsi: Symbol[
        Optional[list[int]],
        None,
    ]

    recv_gsi: Symbol[
        Optional[list[int]],
        None,
    ]

    recvfrom_gsi: Symbol[
        Optional[list[int]],
        None,
    ]

    send_gsi: Symbol[
        Optional[list[int]],
        None,
    ]

    sendto_gsi: Symbol[
        Optional[list[int]],
        None,
    ]

    setsockopt_gsi: Symbol[
        Optional[list[int]],
        None,
    ]

    getsockname_gsi: Symbol[
        Optional[list[int]],
        None,
    ]

    inet_addr_gsi: Symbol[
        Optional[list[int]],
        None,
    ]

    GoaGetLastError: Symbol[
        Optional[list[int]],
        None,
    ]

    GsiSocketSelect: Symbol[
        Optional[list[int]],
        None,
    ]

    SetSockBlocking: Symbol[
        Optional[list[int]],
        None,
    ]

    SetReceiveBufferSize: Symbol[
        Optional[list[int]],
        None,
    ]

    CanReceiveOnSocket: Symbol[
        Optional[list[int]],
        None,
    ]

    CanSendOnSocket: Symbol[
        Optional[list[int]],
        None,
    ]

    getlocalhost_gsi: Symbol[
        Optional[list[int]],
        None,
    ]

    IsPrivateIP: Symbol[
        Optional[list[int]],
        None,
    ]

    time_gsi: Symbol[
        Optional[list[int]],
        None,
    ]

    GsiStartResolvingHostname: Symbol[
        Optional[list[int]],
        None,
    ]

    GsiCancelResolvingHostname: Symbol[
        Optional[list[int]],
        None,
    ]

    GsiGetResolvedIP: Symbol[
        Optional[list[int]],
        None,
    ]

    goastrdup: Symbol[
        Optional[list[int]],
        None,
    ]

    strlwr: Symbol[
        Optional[list[int]],
        None,
    ]

    SocketStartUp_Ghi: Symbol[
        Optional[list[int]],
        None,
    ]

    SocketShutDown_Gsi: Symbol[
        Optional[list[int]],
        None,
    ]

    current_time_gsi: Symbol[
        Optional[list[int]],
        None,
    ]

    current_time_hires_gsi: Symbol[
        Optional[list[int]],
        None,
    ]

    msleep_gsi: Symbol[
        Optional[list[int]],
        None,
    ]

    nextlongrand_gsi: Symbol[
        Optional[list[int]],
        None,
    ]

    longrand_gsi: Symbol[
        Optional[list[int]],
        None,
    ]

    Util_RandSeed: Symbol[
        Optional[list[int]],
        None,
    ]

    Util_RandInt: Symbol[
        Optional[list[int]],
        None,
    ]

    QuartToTrip: Symbol[
        Optional[list[int]],
        None,
    ]

    TripToQuart: Symbol[
        Optional[list[int]],
        None,
    ]

    B64Decode: Symbol[
        Optional[list[int]],
        None,
    ]

    B64Encode: Symbol[
        Optional[list[int]],
        None,
    ]

    GsDebugAssert: Symbol[
        Optional[list[int]],
        None,
    ]

    GsiMemoryCallbacksSet: Symbol[
        Optional[list[int]],
        None,
    ]

    gsimalloc: Symbol[
        Optional[list[int]],
        None,
    ]

    gsirealloc: Symbol[
        Optional[list[int]],
        None,
    ]

    gsifree: Symbol[
        Optional[list[int]],
        None,
    ]

    get_sockaddrin: Symbol[
        Optional[list[int]],
        None,
    ]

    SendPacket_Gsi: Symbol[
        Optional[list[int]],
        None,
    ]

    GsiStartAvailableCheckA: Symbol[
        Optional[list[int]],
        None,
    ]

    HandlePacket: Symbol[
        Optional[list[int]],
        None,
    ]

    GsiAvailableCheckThink: Symbol[
        Optional[list[int]],
        None,
    ]

    GsiCryptRsaGeneratePad: Symbol[
        Optional[list[int]],
        None,
    ]

    GsCryptRsaEncryptBuffer: Symbol[
        Optional[list[int]],
        None,
    ]

    GsCryptRsaPkcs1EncryptBuffer: Symbol[
        Optional[list[int]],
        None,
    ]

    GsiLargeIntTimerEnter: Symbol[
        Optional[list[int]],
        None,
    ]

    GsiLargeIntTimerExit: Symbol[
        Optional[list[int]],
        None,
    ]

    GsiLargeIntCompare: Symbol[
        Optional[list[int]],
        None,
    ]

    GsiLargeIntStripLeadingZeroes: Symbol[
        Optional[list[int]],
        None,
    ]

    GsiLargeIntAdd: Symbol[
        Optional[list[int]],
        None,
    ]

    GsiLargeIntSub: Symbol[
        Optional[list[int]],
        None,
    ]

    GsiLargeIntMult: Symbol[
        Optional[list[int]],
        None,
    ]

    GsLargeIntDiv: Symbol[
        Optional[list[int]],
        None,
    ]

    GsiLargeIntDiv: Symbol[
        Optional[list[int]],
        None,
    ]

    GsiLargeIntSubDivide: Symbol[
        Optional[list[int]],
        None,
    ]

    GsLargeIntSquareMod: Symbol[
        Optional[list[int]],
        None,
    ]

    GsLargeIntPowerMod: Symbol[
        Optional[list[int]],
        None,
    ]

    GsiLargeIntMultM: Symbol[
        Optional[list[int]],
        None,
    ]

    GsiLargeIntInverseMod: Symbol[
        Optional[list[int]],
        None,
    ]

    GsLargeIntReverseBytes: Symbol[
        Optional[list[int]],
        None,
    ]

    GsLargeIntSetFromMemoryStream: Symbol[
        Optional[list[int]],
        None,
    ]

    GsLargeIntWriteToMemoryStream: Symbol[
        Optional[list[int]],
        None,
    ]

    swap_byte_gsi: Symbol[
        Optional[list[int]],
        None,
    ]

    RC4Init_Gsi: Symbol[
        Optional[list[int]],
        None,
    ]

    RC4Encrypt_Gsi: Symbol[
        Optional[list[int]],
        None,
    ]

    Sha1Reset_Gsi: Symbol[
        Optional[list[int]],
        None,
    ]

    Sha1Result_Gsi: Symbol[
        Optional[list[int]],
        None,
    ]

    Sha1Input_Ghi: Symbol[
        Optional[list[int]],
        None,
    ]

    Sha1ProcessMessageBlock: Symbol[
        Optional[list[int]],
        None,
    ]

    Sha1PadMessage: Symbol[
        Optional[list[int]],
        None,
    ]

    GsUdpEngineGetEngine: Symbol[
        Optional[list[int]],
        None,
    ]

    GsUdpMsgHandlerFree: Symbol[
        Optional[list[int]],
        None,
    ]

    GsUdpMsgHandlerCompare: Symbol[
        Optional[list[int]],
        None,
    ]

    GsUdpMsgHandlerCompare2: Symbol[
        Optional[list[int]],
        None,
    ]

    GsUdpRemotePeerCompare: Symbol[
        Optional[list[int]],
        None,
    ]

    GsUdpRemotePeerCompare2: Symbol[
        Optional[list[int]],
        None,
    ]

    GsUdpSocketError: Symbol[
        Optional[list[int]],
        None,
    ]

    GsUdpClosedRoutingCB: Symbol[
        Optional[list[int]],
        None,
    ]

    GsUdpConnectedRoutingCB: Symbol[
        Optional[list[int]],
        None,
    ]

    GsUdpPingRoutingCB: Symbol[
        Optional[list[int]],
        None,
    ]

    GsUdpReceivedRoutingCB: Symbol[
        Optional[list[int]],
        None,
    ]

    GsUdpUnrecognizedMsgCB: Symbol[
        Optional[list[int]],
        None,
    ]

    GsUdpConnAttemptCB: Symbol[
        Optional[list[int]],
        None,
    ]

    GsUdpEngineIsInitialized: Symbol[
        Optional[list[int]],
        None,
    ]

    GsUdpEngineInitialize: Symbol[
        Optional[list[int]],
        None,
    ]

    GsUdpEngineGetPeerState: Symbol[
        Optional[list[int]],
        None,
    ]

    GsUdpEngineStartTalkingToPeer: Symbol[
        Optional[list[int]],
        None,
    ]

    GsUdpEngineSendMessage: Symbol[
        Optional[list[int]],
        None,
    ]

    GsUdpEngineThink: Symbol[
        Optional[list[int]],
        None,
    ]

    GsUdpEngineShutdown: Symbol[
        Optional[list[int]],
        None,
    ]

    GsUdpEngineGetLocalPort: Symbol[
        Optional[list[int]],
        None,
    ]

    GsUdpEngineAddMsgHandler: Symbol[
        Optional[list[int]],
        None,
    ]

    GsUdpEngineRemoveMsgHandler: Symbol[
        Optional[list[int]],
        None,
    ]

    GsUdpEngineNoMoreMsgHandlers: Symbol[
        Optional[list[int]],
        None,
    ]

    GsUdpEngineNoApp: Symbol[
        Optional[list[int]],
        None,
    ]

    GsUdpEngineGetPeerOutBufferFreeSpace: Symbol[
        Optional[list[int]],
        None,
    ]

    GsXmlWriterGetData: Symbol[
        Optional[list[int]],
        None,
    ]

    GsXmlWriterGetDataLength: Symbol[
        Optional[list[int]],
        None,
    ]

    GhiResizeBuffer: Symbol[
        Optional[list[int]],
        None,
    ]

    GhiInitBuffer: Symbol[
        Optional[list[int]],
        None,
    ]

    GhiInitFixedBuffer: Symbol[
        Optional[list[int]],
        None,
    ]

    GhiInitReadOnlyBuffer: Symbol[
        Optional[list[int]],
        None,
    ]

    GhiFreeBuffer: Symbol[
        Optional[list[int]],
        None,
    ]

    GhiAppendDataToBuffer: Symbol[
        Optional[list[int]],
        None,
    ]

    GhiEncryptDataToBuffer: Symbol[
        Optional[list[int]],
        None,
    ]

    GhiAppendHeaderToBuffer: Symbol[
        Optional[list[int]],
        None,
    ]

    GhiAppendCharToBuffer: Symbol[
        Optional[list[int]],
        None,
    ]

    GhiAppendIntToBuffer: Symbol[
        Optional[list[int]],
        None,
    ]

    GhiResetBuffer: Symbol[
        Optional[list[int]],
        None,
    ]

    GhiSendBufferedData: Symbol[
        Optional[list[int]],
        None,
    ]

    GhiReadDataFromBufferFixed: Symbol[
        Optional[list[int]],
        None,
    ]

    GhiCallCompletedCallback: Symbol[
        Optional[list[int]],
        None,
    ]

    GhiCallProgressCallback: Symbol[
        Optional[list[int]],
        None,
    ]

    GhiCallPostCallback: Symbol[
        Optional[list[int]],
        None,
    ]

    GhiCreateLock: Symbol[
        Optional[list[int]],
        None,
    ]

    GhiFreeLock: Symbol[
        Optional[list[int]],
        None,
    ]

    GhiLock: Symbol[
        Optional[list[int]],
        None,
    ]

    GhiUnlock: Symbol[
        Optional[list[int]],
        None,
    ]

    GhiDecryptReceivedData: Symbol[
        Optional[list[int]],
        None,
    ]

    GhiDoReceive: Symbol[
        Optional[list[int]],
        None,
    ]

    GhiDoSend: Symbol[
        Optional[list[int]],
        None,
    ]

    GhiTrySendThenBuffer: Symbol[
        Optional[list[int]],
        None,
    ]

    GhiFindFreeSlot: Symbol[
        Optional[list[int]],
        None,
    ]

    GhiNewConnection: Symbol[
        Optional[list[int]],
        None,
    ]

    GhiFreeConnection: Symbol[
        Optional[list[int]],
        None,
    ]

    GhiRequestToConnection: Symbol[
        Optional[list[int]],
        None,
    ]

    GhiEnumConnections: Symbol[
        Optional[list[int]],
        None,
    ]

    GhiRedirectConnection: Symbol[
        Optional[list[int]],
        None,
    ]

    GhiCleanupConnections: Symbol[
        Optional[list[int]],
        None,
    ]

    GhttpSetRequestEncryptionEngine: Symbol[
        Optional[list[int]],
        None,
    ]

    GhiEncryptorWriteNboLength: Symbol[
        Optional[list[int]],
        None,
    ]

    GhiEncryptorReadNboLength: Symbol[
        Optional[list[int]],
        None,
    ]

    GhiEncryptorParseAsn1Sequence: Symbol[
        Optional[list[int]],
        None,
    ]

    GhttpEncryptorGenerateEncryptionKeys: Symbol[
        Optional[list[int]],
        None,
    ]

    GhttpEncryptorSslInitFunc: Symbol[
        Optional[list[int]],
        None,
    ]

    GhttpEncryptorSslCleanupFunc: Symbol[
        Optional[list[int]],
        None,
    ]

    GhttpEncryptorSslEncryptFunc: Symbol[
        Optional[list[int]],
        None,
    ]

    GhttpEncryptorSslDecryptFunc: Symbol[
        Optional[list[int]],
        None,
    ]

    GhiCertificateChainIsValid: Symbol[
        Optional[list[int]],
        None,
    ]

    GhttpEncryptorProcessSslHandshake: Symbol[
        Optional[list[int]],
        None,
    ]

    GhiHandleStatus: Symbol[
        Optional[list[int]],
        None,
    ]

    GhiProcessConnection: Symbol[
        Optional[list[int]],
        None,
    ]

    GhttpStartup: Symbol[
        Optional[list[int]],
        None,
    ]

    GhttpCleanup: Symbol[
        Optional[list[int]],
        None,
    ]

    GHttpGetExA: Symbol[
        Optional[list[int]],
        None,
    ]

    GhttpThink: Symbol[
        Optional[list[int]],
        None,
    ]

    GHttpCancelRequest: Symbol[
        Optional[list[int]],
        None,
    ]

    GhiIsPostAutoFree: Symbol[
        Optional[list[int]],
        None,
    ]

    GhiFreePost: Symbol[
        Optional[list[int]],
        None,
    ]

    GhiPostGetContentType: Symbol[
        Optional[list[int]],
        None,
    ]

    GhiPostGetNoFilesContentLength: Symbol[
        Optional[list[int]],
        None,
    ]

    GhiPostGetHasFilesContentLength: Symbol[
        Optional[list[int]],
        None,
    ]

    GhiPostGetContentLength: Symbol[
        Optional[list[int]],
        None,
    ]

    GhiPostStateInit: Symbol[
        Optional[list[int]],
        None,
    ]

    GhiPostStateCleanup: Symbol[
        Optional[list[int]],
        None,
    ]

    GhiPostInitState: Symbol[
        Optional[list[int]],
        None,
    ]

    GhiPostCleanupState: Symbol[
        Optional[list[int]],
        None,
    ]

    GhiPostStringStateDoPosting: Symbol[
        Optional[list[int]],
        None,
    ]

    GhiPostXmlStateDoPosting: Symbol[
        Optional[list[int]],
        None,
    ]

    GhiPostFileDiskStateDoPosting: Symbol[
        Optional[list[int]],
        None,
    ]

    GhiPostFileMemoryStateDoPosting: Symbol[
        Optional[list[int]],
        None,
    ]

    GhiPostStateDoPosting: Symbol[
        Optional[list[int]],
        None,
    ]

    GhiPostDoPosting: Symbol[
        Optional[list[int]],
        None,
    ]

    GhiParseUrl: Symbol[
        Optional[list[int]],
        None,
    ]

    GhiDoSocketInit: Symbol[
        Optional[list[int]],
        None,
    ]

    GhiDoHostLookup: Symbol[
        Optional[list[int]],
        None,
    ]

    GhiDoLookupPending: Symbol[
        Optional[list[int]],
        None,
    ]

    GhiDoConnecting: Symbol[
        Optional[list[int]],
        None,
    ]

    GhiDoSecuringSession: Symbol[
        Optional[list[int]],
        None,
    ]

    GhiDoSendingRequest: Symbol[
        Optional[list[int]],
        None,
    ]

    GhiDoPosting: Symbol[
        Optional[list[int]],
        None,
    ]

    GhiDoWaiting: Symbol[
        Optional[list[int]],
        None,
    ]

    GhiParseStatus: Symbol[
        Optional[list[int]],
        None,
    ]

    GhiDoReceivingStatus: Symbol[
        Optional[list[int]],
        None,
    ]

    GhiDeliverIncomingFileData: Symbol[
        Optional[list[int]],
        None,
    ]

    GhiParseChunkSize: Symbol[
        Optional[list[int]],
        None,
    ]

    GhiAppendToChunkHeaderBuffer: Symbol[
        Optional[list[int]],
        None,
    ]

    GhiProcessIncomingFileData: Symbol[
        Optional[list[int]],
        None,
    ]

    GhiDoReceivingHeaders: Symbol[
        Optional[list[int]],
        None,
    ]

    GhiDoReceivingFile: Symbol[
        Optional[list[int]],
        None,
    ]

    GpInitialize: Symbol[
        Optional[list[int]],
        None,
    ]

    GpDestroy: Symbol[
        Optional[list[int]],
        None,
    ]

    GpProcess: Symbol[
        Optional[list[int]],
        None,
    ]

    GpSetCallback: Symbol[
        Optional[list[int]],
        None,
    ]

    GpConnectPreAuthenticatedA: Symbol[
        Optional[list[int]],
        None,
    ]

    GpDisconnect: Symbol[
        Optional[list[int]],
        None,
    ]

    GpProfileSearchA: Symbol[
        Optional[list[int]],
        None,
    ]

    GpGetInfo: Symbol[
        Optional[list[int]],
        None,
    ]

    GpGetInfoNoWait: Symbol[
        Optional[list[int]],
        None,
    ]

    GpSendBuddyRequestA: Symbol[
        Optional[list[int]],
        None,
    ]

    GpAuthBuddyRequest: Symbol[
        Optional[list[int]],
        None,
    ]

    GpDenyBuddyRequest: Symbol[
        Optional[list[int]],
        None,
    ]

    GpGetNumBuddies: Symbol[
        Optional[list[int]],
        None,
    ]

    GpGetBuddyStatus: Symbol[
        Optional[list[int]],
        None,
    ]

    GpGetBuddyIndex: Symbol[
        Optional[list[int]],
        None,
    ]

    GpIsBuddy: Symbol[
        Optional[list[int]],
        None,
    ]

    GpDeleteBuddy: Symbol[
        Optional[list[int]],
        None,
    ]

    GpSetStatusA: Symbol[
        Optional[list[int]],
        None,
    ]

    GpSendBuddyMessageA: Symbol[
        Optional[list[int]],
        None,
    ]

    GpGetReversBuddiesList: Symbol[
        Optional[list[int]],
        None,
    ]

    GpiInitialize: Symbol[
        Optional[list[int]],
        None,
    ]

    GpiDestroy: Symbol[
        Optional[list[int]],
        None,
    ]

    GpiResetProfile: Symbol[
        Optional[list[int]],
        None,
    ]

    GpiReset: Symbol[
        Optional[list[int]],
        None,
    ]

    GpiProcessConnectionManager: Symbol[
        Optional[list[int]],
        None,
    ]

    GpiProcess: Symbol[
        Optional[list[int]],
        None,
    ]

    GpiSendAuthBuddyRequest: Symbol[
        Optional[list[int]],
        None,
    ]

    GpiProcessRecvBuddyMessage: Symbol[
        Optional[list[int]],
        None,
    ]

    GpiProcessRecvBuddyStatusInfo: Symbol[
        Optional[list[int]],
        None,
    ]

    GpiSendServerBuddyMessage: Symbol[
        Optional[list[int]],
        None,
    ]

    GpiSendBuddyMessage: Symbol[
        Optional[list[int]],
        None,
    ]

    GpiBuddyHandleKeyRequest: Symbol[
        Optional[list[int]],
        None,
    ]

    GpiBuddyHandleKeyReply: Symbol[
        Optional[list[int]],
        None,
    ]

    GpiAuthBuddyRequest: Symbol[
        Optional[list[int]],
        None,
    ]

    GpiFixBuddyIndices: Symbol[
        Optional[list[int]],
        None,
    ]

    GpiDeleteBuddy: Symbol[
        Optional[list[int]],
        None,
    ]

    GpiAppendCharToBuffer: Symbol[
        Optional[list[int]],
        None,
    ]

    GpiAppendStringToBufferLen: Symbol[
        Optional[list[int]],
        None,
    ]

    GpiAppendStringToBuffer: Symbol[
        Optional[list[int]],
        None,
    ]

    GpiAppendIntToBuffer: Symbol[
        Optional[list[int]],
        None,
    ]

    GpiSendData: Symbol[
        Optional[list[int]],
        None,
    ]

    GpiSendOrBufferChar: Symbol[
        Optional[list[int]],
        None,
    ]

    GpiSendOrBufferStringLenToPeer: Symbol[
        Optional[list[int]],
        None,
    ]

    GpiSendOrBufferString: Symbol[
        Optional[list[int]],
        None,
    ]

    GpiRecvToBuffer: Symbol[
        Optional[list[int]],
        None,
    ]

    GpiSendFromBuffer: Symbol[
        Optional[list[int]],
        None,
    ]

    GpiSendBufferToPeer: Symbol[
        Optional[list[int]],
        None,
    ]

    GpiReadMessageFromBuffer: Symbol[
        Optional[list[int]],
        None,
    ]

    GpiClipBufferToPosition: Symbol[
        Optional[list[int]],
        None,
    ]

    GpiCallErrorCallback: Symbol[
        Optional[list[int]],
        None,
    ]

    GpiAddCallback: Symbol[
        Optional[list[int]],
        None,
    ]

    GpiCallCallback: Symbol[
        Optional[list[int]],
        None,
    ]

    GpiProcessCallbacks: Symbol[
        Optional[list[int]],
        None,
    ]

    RandomString: Symbol[
        Optional[list[int]],
        None,
    ]

    GpiStartConnect: Symbol[
        Optional[list[int]],
        None,
    ]

    GpiConnect: Symbol[
        Optional[list[int]],
        None,
    ]

    GpiSendLogin: Symbol[
        Optional[list[int]],
        None,
    ]

    GpiSendNewuser: Symbol[
        Optional[list[int]],
        None,
    ]

    GpiProcessConnect: Symbol[
        Optional[list[int]],
        None,
    ]

    GpiCheckConnect: Symbol[
        Optional[list[int]],
        None,
    ]

    GpiDisconnectCleanupProfile: Symbol[
        Optional[list[int]],
        None,
    ]

    GpiDisconnect: Symbol[
        Optional[list[int]],
        None,
    ]

    GpiIsValidDate: Symbol[
        Optional[list[int]],
        None,
    ]

    GpiDateToInt: Symbol[
        Optional[list[int]],
        None,
    ]

    GpiInfoCacheToArg: Symbol[
        Optional[list[int]],
        None,
    ]

    GpiProcessGetInfo: Symbol[
        Optional[list[int]],
        None,
    ]

    GpiAddLocalInfo: Symbol[
        Optional[list[int]],
        None,
    ]

    GpiSendLocalInfo: Symbol[
        Optional[list[int]],
        None,
    ]

    GpiSendUserInfo: Symbol[
        Optional[list[int]],
        None,
    ]

    GpiSetInfoi: Symbol[
        Optional[list[int]],
        None,
    ]

    GpiSetInfos: Symbol[
        Optional[list[int]],
        None,
    ]

    GpiSendGetInfo: Symbol[
        Optional[list[int]],
        None,
    ]

    GpiGetInfo: Symbol[
        Optional[list[int]],
        None,
    ]

    GpiSetInfoCache: Symbol[
        Optional[list[int]],
        None,
    ]

    GpiFreeInfoCache: Symbol[
        Optional[list[int]],
        None,
    ]

    GpiStatusInfoKeyFree: Symbol[
        Optional[list[int]],
        None,
    ]

    GpiStatusInfoKeysInit: Symbol[
        Optional[list[int]],
        None,
    ]

    GpiStatusInfoKeysDestroy: Symbol[
        Optional[list[int]],
        None,
    ]

    GpiStatusInfoKeyCompFunc: Symbol[
        Optional[list[int]],
        None,
    ]

    GpiStatusInfoAddKey: Symbol[
        Optional[list[int]],
        None,
    ]

    GpiStatusInfoSetKey: Symbol[
        Optional[list[int]],
        None,
    ]

    GpiStatusInfoCheckKey: Symbol[
        Optional[list[int]],
        None,
    ]

    GpiSaveKeysToBuffer: Symbol[
        Optional[list[int]],
        None,
    ]

    GpiFailedOpCallback: Symbol[
        Optional[list[int]],
        None,
    ]

    GpiAddOperation: Symbol[
        Optional[list[int]],
        None,
    ]

    GpiDestroyOperation: Symbol[
        Optional[list[int]],
        None,
    ]

    GpiRemoveOperation: Symbol[
        Optional[list[int]],
        None,
    ]

    GpiFindOperationByID: Symbol[
        Optional[list[int]],
        None,
    ]

    GpiOperationsAreBlocking: Symbol[
        Optional[list[int]],
        None,
    ]

    GpiProcessOperation: Symbol[
        Optional[list[int]],
        None,
    ]

    GpiProcessPeerInitiatingConnection: Symbol[
        Optional[list[int]],
        None,
    ]

    GpiProcessPeerAcceptingConnection: Symbol[
        Optional[list[int]],
        None,
    ]

    GpiPeerSendMessages: Symbol[
        Optional[list[int]],
        None,
    ]

    GpiProcessPeerConnected: Symbol[
        Optional[list[int]],
        None,
    ]

    GpiCheckTimedOutPeerOperations: Symbol[
        Optional[list[int]],
        None,
    ]

    GpiProcessPeer: Symbol[
        Optional[list[int]],
        None,
    ]

    GpiDestroyPeer: Symbol[
        Optional[list[int]],
        None,
    ]

    GpiRemovePeer: Symbol[
        Optional[list[int]],
        None,
    ]

    GpiProcessPeers: Symbol[
        Optional[list[int]],
        None,
    ]

    GpiGetPeerByProfile: Symbol[
        Optional[list[int]],
        None,
    ]

    GpiGetPeerByAddr: Symbol[
        Optional[list[int]],
        None,
    ]

    GpiFreeMessage: Symbol[
        Optional[list[int]],
        None,
    ]

    GpiAddPeer: Symbol[
        Optional[list[int]],
        None,
    ]

    GpiPeerGetSig: Symbol[
        Optional[list[int]],
        None,
    ]

    GpiPeerStartConnect: Symbol[
        Optional[list[int]],
        None,
    ]

    GpiPeerAddMessage: Symbol[
        Optional[list[int]],
        None,
    ]

    GpiPeerStartTransferMessage: Symbol[
        Optional[list[int]],
        None,
    ]

    GpiPeerFinishTransferMessage: Symbol[
        Optional[list[int]],
        None,
    ]

    GpiPeerLeftCallback: Symbol[
        Optional[list[int]],
        None,
    ]

    GpiPeerMessageCallback: Symbol[
        Optional[list[int]],
        None,
    ]

    GpiPeerAcceptedCallback: Symbol[
        Optional[list[int]],
        None,
    ]

    GpiPeerPingReplyCallback: Symbol[
        Optional[list[int]],
        None,
    ]

    GpiPeerAddOp: Symbol[
        Optional[list[int]],
        None,
    ]

    GpiPeerRemoveOp: Symbol[
        Optional[list[int]],
        None,
    ]

    GpiProfilesTableHash: Symbol[
        Optional[list[int]],
        None,
    ]

    GpiProfilesTableCompare: Symbol[
        Optional[list[int]],
        None,
    ]

    GpiProfilesTableFree: Symbol[
        Optional[list[int]],
        None,
    ]

    GpiInitProfiles: Symbol[
        Optional[list[int]],
        None,
    ]

    GpiProcessNewProfile: Symbol[
        Optional[list[int]],
        None,
    ]

    GpiProfileListAdd: Symbol[
        Optional[list[int]],
        None,
    ]

    GpiGetProfile: Symbol[
        Optional[list[int]],
        None,
    ]

    GpiProcessDeleteProfle: Symbol[
        Optional[list[int]],
        None,
    ]

    GpiRemoveProfileByID: Symbol[
        Optional[list[int]],
        None,
    ]

    GpiRemoveProfile: Symbol[
        Optional[list[int]],
        None,
    ]

    GpiCheckProfileForUser: Symbol[
        Optional[list[int]],
        None,
    ]

    GpiFindProfileByUser: Symbol[
        Optional[list[int]],
        None,
    ]

    GpiProfileMapCallback: Symbol[
        Optional[list[int]],
        None,
    ]

    GpiProfileMap: Symbol[
        Optional[list[int]],
        None,
    ]

    GpiCheckForBuddy: Symbol[
        Optional[list[int]],
        None,
    ]

    GpiFindBuddy: Symbol[
        Optional[list[int]],
        None,
    ]

    GpiRemoveBuddyStatus: Symbol[
        Optional[list[int]],
        None,
    ]

    GpiRemoveBuddyStatusInfo: Symbol[
        Optional[list[int]],
        None,
    ]

    GpiCanFreeProfile: Symbol[
        Optional[list[int]],
        None,
    ]

    GpiStartProfileSearch: Symbol[
        Optional[list[int]],
        None,
    ]

    GpiInitSearchData: Symbol[
        Optional[list[int]],
        None,
    ]

    GpiStartSearch: Symbol[
        Optional[list[int]],
        None,
    ]

    GpiProfileSearch: Symbol[
        Optional[list[int]],
        None,
    ]

    GpiOthersBuddyList: Symbol[
        Optional[list[int]],
        None,
    ]

    GpiProcessSearch: Symbol[
        Optional[list[int]],
        None,
    ]

    GpiProcessSearches: Symbol[
        Optional[list[int]],
        None,
    ]

    GpiSendTransferReply: Symbol[
        Optional[list[int]],
        None,
    ]

    GpiHandleTransferMessage: Symbol[
        Optional[list[int]],
        None,
    ]

    GpiProcessRegisterUniqueNick: Symbol[
        Optional[list[int]],
        None,
    ]

    GpiProcessRegisterCdKey: Symbol[
        Optional[list[int]],
        None,
    ]

    strzcpy_gsi: Symbol[
        Optional[list[int]],
        None,
    ]

    GpiCheckForError: Symbol[
        Optional[list[int]],
        None,
    ]

    GpiValueForKey: Symbol[
        Optional[list[int]],
        None,
    ]

    GpiCheckSocketConnect: Symbol[
        Optional[list[int]],
        None,
    ]

    GpiReadKeyAndValue: Symbol[
        Optional[list[int]],
        None,
    ]

    GpiSetError: Symbol[
        Optional[list[int]],
        None,
    ]

    GpiSetErrorString: Symbol[
        Optional[list[int]],
        None,
    ]

    GpiEncodeString: Symbol[
        Optional[list[int]],
        None,
    ]

    BucketNew: Symbol[
        Optional[list[int]],
        None,
    ]

    BucketSet: Symbol[
        Optional[list[int]],
        None,
    ]

    BucketAdd_Gsi: Symbol[
        Optional[list[int]],
        None,
    ]

    BucketSub_Gsi: Symbol[
        Optional[list[int]],
        None,
    ]

    BucketMult_Gsi: Symbol[
        Optional[list[int]],
        None,
    ]

    BucketDiv_Gsi: Symbol[
        Optional[list[int]],
        None,
    ]

    BucketConcat_Gsi: Symbol[
        Optional[list[int]],
        None,
    ]

    BucketAvg_Gsi: Symbol[
        Optional[list[int]],
        None,
    ]

    bint: Symbol[
        Optional[list[int]],
        None,
    ]

    bfloat: Symbol[
        Optional[list[int]],
        None,
    ]

    DumpMap_Gsi: Symbol[
        Optional[list[int]],
        None,
    ]

    DoSet_Gsi: Symbol[
        Optional[list[int]],
        None,
    ]

    DoGet_Gsi: Symbol[
        Optional[list[int]],
        None,
    ]

    DoFind_Gsi: Symbol[
        Optional[list[int]],
        None,
    ]

    CloseStatsConnection: Symbol[
        Optional[list[int]],
        None,
    ]

    IsStatsConnected: Symbol[
        Optional[list[int]],
        None,
    ]

    PersistThink: Symbol[
        Optional[list[int]],
        None,
    ]

    xcode_buf: Symbol[
        Optional[list[int]],
        None,
    ]

    value_for_key: Symbol[
        Optional[list[int]],
        None,
    ]

    value_for_key_safe: Symbol[
        Optional[list[int]],
        None,
    ]

    SocketReadable: Symbol[
        Optional[list[int]],
        None,
    ]

    FindFinal: Symbol[
        Optional[list[int]],
        None,
    ]

    FindRequest: Symbol[
        Optional[list[int]],
        None,
    ]

    ProcessPlayerAuth: Symbol[
        Optional[list[int]],
        None,
    ]

    ProcessGetPid: Symbol[
        Optional[list[int]],
        None,
    ]

    ProcessGetData: Symbol[
        Optional[list[int]],
        None,
    ]

    ProcessSetData: Symbol[
        Optional[list[int]],
        None,
    ]

    ProcessStatement: Symbol[
        Optional[list[int]],
        None,
    ]

    ProcessInBuffer: Symbol[
        Optional[list[int]],
        None,
    ]

    CallReqCallback: Symbol[
        Optional[list[int]],
        None,
    ]

    ClosePendingCallbacks: Symbol[
        Optional[list[int]],
        None,
    ]

    GetTeamIndex_Gsi: Symbol[
        Optional[list[int]],
        None,
    ]

    GetPlayerIndex_Gsi: Symbol[
        Optional[list[int]],
        None,
    ]

    ServerOpInt: Symbol[
        Optional[list[int]],
        None,
    ]

    ServerOpFloat: Symbol[
        Optional[list[int]],
        None,
    ]

    ServerOpString: Symbol[
        Optional[list[int]],
        None,
    ]

    TeamOpInt: Symbol[
        Optional[list[int]],
        None,
    ]

    TeamOpFloat: Symbol[
        Optional[list[int]],
        None,
    ]

    TeamOpString: Symbol[
        Optional[list[int]],
        None,
    ]

    PlayerOpInt: Symbol[
        Optional[list[int]],
        None,
    ]

    PlayerOpFloat: Symbol[
        Optional[list[int]],
        None,
    ]

    PlayerOpString: Symbol[
        Optional[list[int]],
        None,
    ]

    Gti2VerifyChallenge: Symbol[
        Optional[list[int]],
        None,
    ]

    Gti2GetChallenge: Symbol[
        Optional[list[int]],
        None,
    ]

    Gti2GetResponse: Symbol[
        Optional[list[int]],
        None,
    ]

    Gti2CheckResponse: Symbol[
        Optional[list[int]],
        None,
    ]

    Gti2AllocateBuffer: Symbol[
        Optional[list[int]],
        None,
    ]

    Gti2GetBufferFreeSpace: Symbol[
        Optional[list[int]],
        None,
    ]

    Gti2BufferWriteByte: Symbol[
        Optional[list[int]],
        None,
    ]

    Gti2BufferWriteUShort: Symbol[
        Optional[list[int]],
        None,
    ]

    Gti2BufferWriteData: Symbol[
        Optional[list[int]],
        None,
    ]

    Gti2BufferShorten: Symbol[
        Optional[list[int]],
        None,
    ]

    Gti2SocketErrorCallback: Symbol[
        Optional[list[int]],
        None,
    ]

    Gti2ConnectAttemptCallback: Symbol[
        Optional[list[int]],
        None,
    ]

    Gti2ConnectedCallback: Symbol[
        Optional[list[int]],
        None,
    ]

    Gti2ReceivedCallback: Symbol[
        Optional[list[int]],
        None,
    ]

    Gti2ClosedCallback: Symbol[
        Optional[list[int]],
        None,
    ]

    Gti2PingCallback: Symbol[
        Optional[list[int]],
        None,
    ]

    Gti2SendFilterCallback: Symbol[
        Optional[list[int]],
        None,
    ]

    Gti2ReceiveFilterCallback: Symbol[
        Optional[list[int]],
        None,
    ]

    Gti2DumpCallback: Symbol[
        Optional[list[int]],
        None,
    ]

    Gti2UnrecognizedMessageCallback: Symbol[
        Optional[list[int]],
        None,
    ]

    Gti2NewOutgoingConnection: Symbol[
        Optional[list[int]],
        None,
    ]

    Gti2NewIncomingConnection: Symbol[
        Optional[list[int]],
        None,
    ]

    Gti2StartConnectionAttempt: Symbol[
        Optional[list[int]],
        None,
    ]

    Gti2AcceptConnection: Symbol[
        Optional[list[int]],
        None,
    ]

    Gti2RejectConnection: Symbol[
        Optional[list[int]],
        None,
    ]

    Gti2ConnectionSendData: Symbol[
        Optional[list[int]],
        None,
    ]

    Gti2CheckTimeout: Symbol[
        Optional[list[int]],
        None,
    ]

    Gti2SendRetries: Symbol[
        Optional[list[int]],
        None,
    ]

    Gti2CheckPendingAck: Symbol[
        Optional[list[int]],
        None,
    ]

    Gti2CheckKeepAlive: Symbol[
        Optional[list[int]],
        None,
    ]

    Gti2ConnectionThink: Symbol[
        Optional[list[int]],
        None,
    ]

    Gti2CloseConnection: Symbol[
        Optional[list[int]],
        None,
    ]

    Gti2ConnectionClosed: Symbol[
        Optional[list[int]],
        None,
    ]

    Gti2ConnectionCleanup: Symbol[
        Optional[list[int]],
        None,
    ]

    Gt2CreateSocket: Symbol[
        Optional[list[int]],
        None,
    ]

    Gt2CloseSocket: Symbol[
        Optional[list[int]],
        None,
    ]

    Gt2Think: Symbol[
        Optional[list[int]],
        None,
    ]

    Gt2Listen: Symbol[
        Optional[list[int]],
        None,
    ]

    Gt2Accept: Symbol[
        Optional[list[int]],
        None,
    ]

    Gt2Reject: Symbol[
        Optional[list[int]],
        None,
    ]

    Gt2Connect: Symbol[
        Optional[list[int]],
        None,
    ]

    Gt2Send: Symbol[
        Optional[list[int]],
        None,
    ]

    Gt2CloseConnectionHard: Symbol[
        Optional[list[int]],
        None,
    ]

    Gti2CloseAllConnectionsHardMap: Symbol[
        Optional[list[int]],
        None,
    ]

    Gt2CloseAllConnectionsHard: Symbol[
        Optional[list[int]],
        None,
    ]

    Gt2GetConnectionState: Symbol[
        Optional[list[int]],
        None,
    ]

    Gt2GetRemoteIP: Symbol[
        Optional[list[int]],
        None,
    ]

    Gt2GetRemotePort: Symbol[
        Optional[list[int]],
        None,
    ]

    Gt2GetLocalIP: Symbol[
        Optional[list[int]],
        None,
    ]

    Gt2GetLocalPort: Symbol[
        Optional[list[int]],
        None,
    ]

    Gt2GetOutgoingBufferSize: Symbol[
        Optional[list[int]],
        None,
    ]

    Gt2GetOutgoingBufferFreeSpace: Symbol[
        Optional[list[int]],
        None,
    ]

    Gt2GetSocketSocket: Symbol[
        Optional[list[int]],
        None,
    ]

    Gt2SetUnrecognizedMessageCallback: Symbol[
        Optional[list[int]],
        None,
    ]

    Gt2SetConnectionData: Symbol[
        Optional[list[int]],
        None,
    ]

    Gt2GetConnectionData: Symbol[
        Optional[list[int]],
        None,
    ]

    Gti2UShortFromBuffer: Symbol[
        Optional[list[int]],
        None,
    ]

    Gti2UShortToBuffer: Symbol[
        Optional[list[int]],
        None,
    ]

    Gti2SnDiff: Symbol[
        Optional[list[int]],
        None,
    ]

    Gti2ConnectionError: Symbol[
        Optional[list[int]],
        None,
    ]

    Gti2ConnectionCommunicationError: Symbol[
        Optional[list[int]],
        None,
    ]

    Gti2ConnectionMemoryError: Symbol[
        Optional[list[int]],
        None,
    ]

    Gti2HandleEsn: Symbol[
        Optional[list[int]],
        None,
    ]

    Gti2HandleAppUnreliable: Symbol[
        Optional[list[int]],
        None,
    ]

    Gti2HandleAppReliable: Symbol[
        Optional[list[int]],
        None,
    ]

    Gti2HandleClientChallenge: Symbol[
        Optional[list[int]],
        None,
    ]

    Gti2HandleServerChallenge: Symbol[
        Optional[list[int]],
        None,
    ]

    Gti2HandleClientResponse: Symbol[
        Optional[list[int]],
        None,
    ]

    Gti2HandleAccept: Symbol[
        Optional[list[int]],
        None,
    ]

    Gti2HandleReject: Symbol[
        Optional[list[int]],
        None,
    ]

    Gti2HandleClose: Symbol[
        Optional[list[int]],
        None,
    ]

    Gti2DeliverReliableMessage: Symbol[
        Optional[list[int]],
        None,
    ]

    Gti2IncomingBufferMessageCompare: Symbol[
        Optional[list[int]],
        None,
    ]

    Gti2BufferIncomingMessage: Symbol[
        Optional[list[int]],
        None,
    ]

    Gti2RemoveHoldMessage: Symbol[
        Optional[list[int]],
        None,
    ]

    Gti2DeliverHoldMessages: Symbol[
        Optional[list[int]],
        None,
    ]

    Gti2SetPendingAck: Symbol[
        Optional[list[int]],
        None,
    ]

    Gti2HandleReliableMessage: Symbol[
        Optional[list[int]],
        None,
    ]

    Gti2HandleAck: Symbol[
        Optional[list[int]],
        None,
    ]

    Gti2HandleNack: Symbol[
        Optional[list[int]],
        None,
    ]

    Gti2HandlePing: Symbol[
        Optional[list[int]],
        None,
    ]

    Gti2HandlePong: Symbol[
        Optional[list[int]],
        None,
    ]

    Gti2HandleClosed: Symbol[
        Optional[list[int]],
        None,
    ]

    Gti2HandleUnreliableMessage: Symbol[
        Optional[list[int]],
        None,
    ]

    Gti2HandleMessage: Symbol[
        Optional[list[int]],
        None,
    ]

    Gti2HandleConnectionReset: Symbol[
        Optional[list[int]],
        None,
    ]

    Gti2HandleHostUnreachable: Symbol[
        Optional[list[int]],
        None,
    ]

    Gti2ReceiveMessages: Symbol[
        Optional[list[int]],
        None,
    ]

    Gti2StoreOutgoingReliableMessageInfo: Symbol[
        Optional[list[int]],
        None,
    ]

    Gti2BeginReliableMessage: Symbol[
        Optional[list[int]],
        None,
    ]

    Gti2EndReliableMessage: Symbol[
        Optional[list[int]],
        None,
    ]

    Gti2SendAppReliable: Symbol[
        Optional[list[int]],
        None,
    ]

    Gti2SendClientChallenge: Symbol[
        Optional[list[int]],
        None,
    ]

    Gti2SendServerChallenge: Symbol[
        Optional[list[int]],
        None,
    ]

    Gti2SendClientResponse: Symbol[
        Optional[list[int]],
        None,
    ]

    Gti2SendAccept: Symbol[
        Optional[list[int]],
        None,
    ]

    Gti2SendReject: Symbol[
        Optional[list[int]],
        None,
    ]

    Gti2SendClose: Symbol[
        Optional[list[int]],
        None,
    ]

    Gti2SendKeepAlive: Symbol[
        Optional[list[int]],
        None,
    ]

    Gti2SendAppUnreliable: Symbol[
        Optional[list[int]],
        None,
    ]

    Gti2SendAck: Symbol[
        Optional[list[int]],
        None,
    ]

    Gti2SendNack: Symbol[
        Optional[list[int]],
        None,
    ]

    Gti2SendPong: Symbol[
        Optional[list[int]],
        None,
    ]

    Gti2SendClosed: Symbol[
        Optional[list[int]],
        None,
    ]

    Gti2SendClosedOnSocket: Symbol[
        Optional[list[int]],
        None,
    ]

    Gti2ResendMessage: Symbol[
        Optional[list[int]],
        None,
    ]

    Gti2Send: Symbol[
        Optional[list[int]],
        None,
    ]

    Gti2ConnectionHash: Symbol[
        Optional[list[int]],
        None,
    ]

    Gti2ConnectionCompare: Symbol[
        Optional[list[int]],
        None,
    ]

    Gti2ConnectionFree: Symbol[
        Optional[list[int]],
        None,
    ]

    Gti2SocketFindConnection: Symbol[
        Optional[list[int]],
        None,
    ]

    Gti2CreateSocket: Symbol[
        Optional[list[int]],
        None,
    ]

    Gti2CloseSocket: Symbol[
        Optional[list[int]],
        None,
    ]

    Gti2Listen: Symbol[
        Optional[list[int]],
        None,
    ]

    Gti2CreateConnectionObject: Symbol[
        Optional[list[int]],
        None,
    ]

    Gti2NewSocketConnection: Symbol[
        Optional[list[int]],
        None,
    ]

    Gti2FreeSocketConnection: Symbol[
        Optional[list[int]],
        None,
    ]

    Gti2SocketSend: Symbol[
        Optional[list[int]],
        None,
    ]

    Gti2SocketConnectionsThinkMap: Symbol[
        Optional[list[int]],
        None,
    ]

    Gti2SocketConnectionsThink: Symbol[
        Optional[list[int]],
        None,
    ]

    Gti2FreeClosedConnections: Symbol[
        Optional[list[int]],
        None,
    ]

    Gti2SocketError: Symbol[
        Optional[list[int]],
        None,
    ]

    Gt2AddressToString: Symbol[
        Optional[list[int]],
        None,
    ]

    Gt2StringToAddress: Symbol[
        Optional[list[int]],
        None,
    ]

    Gti2MessageCheck: Symbol[
        Optional[list[int]],
        None,
    ]

    GetLocalIP_Gsi: Symbol[
        Optional[list[int]],
        None,
    ]

    GetLocalPort_Gsi: Symbol[
        Optional[list[int]],
        None,
    ]

    OutputMapping: Symbol[
        Optional[list[int]],
        None,
    ]

    Think_NN: Symbol[
        Optional[list[int]],
        None,
    ]

    NatifyThink: Symbol[
        Optional[list[int]],
        None,
    ]

    DetermineNatType: Symbol[
        Optional[list[int]],
        None,
    ]

    FindNegotiatorForCookie: Symbol[
        Optional[list[int]],
        None,
    ]

    AddNegotiator: Symbol[
        Optional[list[int]],
        None,
    ]

    RemoveNegotiator: Symbol[
        Optional[list[int]],
        None,
    ]

    NnFreeNegotiateList: Symbol[
        Optional[list[int]],
        None,
    ]

    CheckMagic_NN: Symbol[
        Optional[list[int]],
        None,
    ]

    SendPacket_NN: Symbol[
        Optional[list[int]],
        None,
    ]

    GetLocalIP_NN: Symbol[
        Optional[list[int]],
        None,
    ]

    GetLocalPort_NN: Symbol[
        Optional[list[int]],
        None,
    ]

    SendReportPacket: Symbol[
        Optional[list[int]],
        None,
    ]

    StartReport: Symbol[
        Optional[list[int]],
        None,
    ]

    SendInitPackets: Symbol[
        Optional[list[int]],
        None,
    ]

    SendPingPacket: Symbol[
        Optional[list[int]],
        None,
    ]

    CheckNatifyStatus: Symbol[
        Optional[list[int]],
        None,
    ]

    NameToIp_NN: Symbol[
        Optional[list[int]],
        None,
    ]

    ResolveServer_NN: Symbol[
        Optional[list[int]],
        None,
    ]

    ResolveServers_NN: Symbol[
        Optional[list[int]],
        None,
    ]

    NnBeginNegotiationWithSocket: Symbol[
        Optional[list[int]],
        None,
    ]

    NnCancel: Symbol[
        Optional[list[int]],
        None,
    ]

    NegotiateThink: Symbol[
        Optional[list[int]],
        None,
    ]

    NnThink: Symbol[
        Optional[list[int]],
        None,
    ]

    SendConnectAck: Symbol[
        Optional[list[int]],
        None,
    ]

    ProcessConnectPacket: Symbol[
        Optional[list[int]],
        None,
    ]

    ProcessPingPacket: Symbol[
        Optional[list[int]],
        None,
    ]

    ProcessInitPacket: Symbol[
        Optional[list[int]],
        None,
    ]

    NnProcessData: Symbol[
        Optional[list[int]],
        None,
    ]

    qr2_init_socketa: Symbol[
        Optional[list[int]],
        None,
    ]

    qr2_register_natneg_callback: Symbol[
        Optional[list[int]],
        None,
    ]

    qr2_register_clientmessage_callback: Symbol[
        Optional[list[int]],
        None,
    ]

    qr2_register_publicaddress_callback: Symbol[
        Optional[list[int]],
        None,
    ]

    qr2_think: Symbol[
        Optional[list[int]],
        None,
    ]

    qr2_check_queries: Symbol[
        Optional[list[int]],
        None,
    ]

    qr2_check_send_heartbeat: Symbol[
        Optional[list[int]],
        None,
    ]

    qr2_send_statechanged: Symbol[
        Optional[list[int]],
        None,
    ]

    qr2_shutdown: Symbol[
        Optional[list[int]],
        None,
    ]

    qr2_keybuffer_add: Symbol[
        Optional[list[int]],
        None,
    ]

    qr2_buffer_add_int: Symbol[
        Optional[list[int]],
        None,
    ]

    Qr2_Buffer_AddA: Symbol[
        Optional[list[int]],
        None,
    ]

    enum_local_ips: Symbol[
        Optional[list[int]],
        None,
    ]

    swap_byte_qr2: Symbol[
        Optional[list[int]],
        None,
    ]

    encode_ct: Symbol[
        Optional[list[int]],
        None,
    ]

    gs_encode: Symbol[
        Optional[list[int]],
        None,
    ]

    gs_encrypt: Symbol[
        Optional[list[int]],
        None,
    ]

    qr_add_packet_header: Symbol[
        Optional[list[int]],
        None,
    ]

    compute_challenge_response: Symbol[
        Optional[list[int]],
        None,
    ]

    handle_public_address: Symbol[
        Optional[list[int]],
        None,
    ]

    qr_build_partial_query_reply: Symbol[
        Optional[list[int]],
        None,
    ]

    qr_build_query_reply: Symbol[
        Optional[list[int]],
        None,
    ]

    qr_build_split_query_reply: Symbol[
        Optional[list[int]],
        None,
    ]

    qr_process_query: Symbol[
        Optional[list[int]],
        None,
    ]

    qr_process_client_message: Symbol[
        Optional[list[int]],
        None,
    ]

    qr_got_recent_message: Symbol[
        Optional[list[int]],
        None,
    ]

    qr2_process_ip_verify: Symbol[
        Optional[list[int]],
        None,
    ]

    qr2_check_ip_verify: Symbol[
        Optional[list[int]],
        None,
    ]

    qr2_expire_ip_verify: Symbol[
        Optional[list[int]],
        None,
    ]

    qr2_parse_querya: Symbol[
        Optional[list[int]],
        None,
    ]

    send_keepalive: Symbol[
        Optional[list[int]],
        None,
    ]

    send_heartbeat: Symbol[
        Optional[list[int]],
        None,
    ]

    qr2_internal_is_master_only_key: Symbol[
        Optional[list[int]],
        None,
    ]

    keyrand_goa: Symbol[
        Optional[list[int]],
        None,
    ]

    GoaHashInit: Symbol[
        Optional[list[int]],
        None,
    ]

    GoaCryptInit: Symbol[
        Optional[list[int]],
        None,
    ]

    GoaEncryptByte: Symbol[
        Optional[list[int]],
        None,
    ]

    GoaEncrypt: Symbol[
        Optional[list[int]],
        None,
    ]

    FifoAddRear: Symbol[
        Optional[list[int]],
        None,
    ]

    FifoAddFront: Symbol[
        Optional[list[int]],
        None,
    ]

    FifoRemove: Symbol[
        Optional[list[int]],
        None,
    ]

    FifoClear: Symbol[
        Optional[list[int]],
        None,
    ]

    QeStartQuery: Symbol[
        Optional[list[int]],
        None,
    ]

    SbEngineHaltUpdates: Symbol[
        Optional[list[int]],
        None,
    ]

    SbEngineCleanup: Symbol[
        Optional[list[int]],
        None,
    ]

    ParseSingleQR2Reply: Symbol[
        Optional[list[int]],
        None,
    ]

    ParseSingleGoaReply: Symbol[
        Optional[list[int]],
        None,
    ]

    ParseSingleIcmpReply: Symbol[
        Optional[list[int]],
        None,
    ]

    ProcessIncomingReplies: Symbol[
        Optional[list[int]],
        None,
    ]

    TimeoutOldQueries: Symbol[
        Optional[list[int]],
        None,
    ]

    QueueNextQueries: Symbol[
        Optional[list[int]],
        None,
    ]

    SbQueryEngineThink: Symbol[
        Optional[list[int]],
        None,
    ]

    SbQueryEngineAddQueryKey: Symbol[
        Optional[list[int]],
        None,
    ]

    RefStringHash: Symbol[
        Optional[list[int]],
        None,
    ]

    RefStringCompare: Symbol[
        Optional[list[int]],
        None,
    ]

    RefStringFree: Symbol[
        Optional[list[int]],
        None,
    ]

    SbRefStrHash: Symbol[
        Optional[list[int]],
        None,
    ]

    SbRefStrHashCleanup: Symbol[
        Optional[list[int]],
        None,
    ]

    SbServerFree: Symbol[
        Optional[list[int]],
        None,
    ]

    SbServerAddKeyValue: Symbol[
        Optional[list[int]],
        None,
    ]

    SbServerAddIntKeyValue: Symbol[
        Optional[list[int]],
        None,
    ]

    SbServerGetStringValueA: Symbol[
        Optional[list[int]],
        None,
    ]

    SbServerGetIntValueA: Symbol[
        Optional[list[int]],
        None,
    ]

    SbServerGetPublicInetAddress: Symbol[
        Optional[list[int]],
        None,
    ]

    SbServerGetPublicQueryPort: Symbol[
        Optional[list[int]],
        None,
    ]

    SbServerGetPublicQueryPortNbo: Symbol[
        Optional[list[int]],
        None,
    ]

    SbServerHasPrivateAddress: Symbol[
        Optional[list[int]],
        None,
    ]

    SbServerGetPrivateInetAddress: Symbol[
        Optional[list[int]],
        None,
    ]

    SbServerGetPrivateQueryPort: Symbol[
        Optional[list[int]],
        None,
    ]

    SbServerSetNext: Symbol[
        Optional[list[int]],
        None,
    ]

    SbServerGetNext: Symbol[
        Optional[list[int]],
        None,
    ]

    CheckValidKey: Symbol[
        Optional[list[int]],
        None,
    ]

    mytok: Symbol[
        Optional[list[int]],
        None,
    ]

    SbServerParseKeyVals: Symbol[
        Optional[list[int]],
        None,
    ]

    SbServerParseQR2FullKeysSingle: Symbol[
        Optional[list[int]],
        None,
    ]

    SbServerParseQR2FullKeysSplit: Symbol[
        Optional[list[int]],
        None,
    ]

    StringHash: Symbol[
        Optional[list[int]],
        None,
    ]

    KeyValFree: Symbol[
        Optional[list[int]],
        None,
    ]

    KeyValHashKey: Symbol[
        Optional[list[int]],
        None,
    ]

    KeyValCompareKey: Symbol[
        Optional[list[int]],
        None,
    ]

    SbServerGetPing: Symbol[
        Optional[list[int]],
        None,
    ]

    SbAllocServer: Symbol[
        Optional[list[int]],
        None,
    ]

    SbServerSetFlags: Symbol[
        Optional[list[int]],
        None,
    ]

    SbServerSetPublicAddr: Symbol[
        Optional[list[int]],
        None,
    ]

    SbServerSetIcmpIp: Symbol[
        Optional[list[int]],
        None,
    ]

    SbServerSetState: Symbol[
        Optional[list[int]],
        None,
    ]

    SbServerGetState: Symbol[
        Optional[list[int]],
        None,
    ]

    SbIsNullServer: Symbol[
        Optional[list[int]],
        None,
    ]

    ServerBrowserFree: Symbol[
        Optional[list[int]],
        None,
    ]

    ServerBrowserBeginUpdate2: Symbol[
        Optional[list[int]],
        None,
    ]

    ServerBrowserLimitUpdateA: Symbol[
        Optional[list[int]],
        None,
    ]

    ServerBrowserSendMessageToServerA: Symbol[
        Optional[list[int]],
        None,
    ]

    ServerBrowserSendNatNegotiateCookieToServerA: Symbol[
        Optional[list[int]],
        None,
    ]

    ServerBrowserThink: Symbol[
        Optional[list[int]],
        None,
    ]

    ServerBrowserHalt: Symbol[
        Optional[list[int]],
        None,
    ]

    ServerBrowserClear: Symbol[
        Optional[list[int]],
        None,
    ]

    ServerBrowserState: Symbol[
        Optional[list[int]],
        None,
    ]

    ServerBrowserGetServer: Symbol[
        Optional[list[int]],
        None,
    ]

    ServerBrowserGetMyPublicIpAddr: Symbol[
        Optional[list[int]],
        None,
    ]

    SbServerListAppendServer: Symbol[
        Optional[list[int]],
        None,
    ]

    SbServerListFindServerByIP: Symbol[
        Optional[list[int]],
        None,
    ]

    AddServerToDeadlist: Symbol[
        Optional[list[int]],
        None,
    ]

    SbServerListRemoveAt: Symbol[
        Optional[list[int]],
        None,
    ]

    SbServerListNth: Symbol[
        Optional[list[int]],
        None,
    ]

    SbFreeDeadList: Symbol[
        Optional[list[int]],
        None,
    ]

    SbServerListClear: Symbol[
        Optional[list[int]],
        None,
    ]

    SbRefStr: Symbol[
        Optional[list[int]],
        None,
    ]

    SbReleaseStr: Symbol[
        Optional[list[int]],
        None,
    ]

    NtsLengthSB: Symbol[
        Optional[list[int]],
        None,
    ]

    ErrorDisconnect: Symbol[
        Optional[list[int]],
        None,
    ]

    StringHash_Sb: Symbol[
        Optional[list[int]],
        None,
    ]

    ServerListConnect: Symbol[
        Optional[list[int]],
        None,
    ]

    BufferAddNtS: Symbol[
        Optional[list[int]],
        None,
    ]

    BufferAddByte: Symbol[
        Optional[list[int]],
        None,
    ]

    BufferAddInt: Symbol[
        Optional[list[int]],
        None,
    ]

    BufferAddIntLE: Symbol[
        Optional[list[int]],
        None,
    ]

    BufferAddData: Symbol[
        Optional[list[int]],
        None,
    ]

    SetupListChallenge: Symbol[
        Optional[list[int]],
        None,
    ]

    SendWithRetry: Symbol[
        Optional[list[int]],
        None,
    ]

    SbServerListConnectAndQuery: Symbol[
        Optional[list[int]],
        None,
    ]

    FreePopularValues: Symbol[
        Optional[list[int]],
        None,
    ]

    FreeKeyList: Symbol[
        Optional[list[int]],
        None,
    ]

    SbServerListDisconnect: Symbol[
        Optional[list[int]],
        None,
    ]

    SbServerListCleanup: Symbol[
        Optional[list[int]],
        None,
    ]

    InitCryptKey: Symbol[
        Optional[list[int]],
        None,
    ]

    ServerSizeForFlags: Symbol[
        Optional[list[int]],
        None,
    ]

    FullRulesPresent: Symbol[
        Optional[list[int]],
        None,
    ]

    AllKeysPresent: Symbol[
        Optional[list[int]],
        None,
    ]

    ParseServerIpPort: Symbol[
        Optional[list[int]],
        None,
    ]

    ParseServer: Symbol[
        Optional[list[int]],
        None,
    ]

    IncomingListParseServer: Symbol[
        Optional[list[int]],
        None,
    ]

    SbSetLastListErrorPtr: Symbol[
        Optional[list[int]],
        None,
    ]

    ProcessMainListData: Symbol[
        Optional[list[int]],
        None,
    ]

    ProcessPushKeyList: Symbol[
        Optional[list[int]],
        None,
    ]

    ProcessPlayerSearch: Symbol[
        Optional[list[int]],
        None,
    ]

    ProcessMaploop: Symbol[
        Optional[list[int]],
        None,
    ]

    ProcessDeleteServer: Symbol[
        Optional[list[int]],
        None,
    ]

    ProcessPushServer: Symbol[
        Optional[list[int]],
        None,
    ]

    ProcessAdHocData: Symbol[
        Optional[list[int]],
        None,
    ]

    ProcessIncomingData: Symbol[
        Optional[list[int]],
        None,
    ]

    SbSendMessageToServer: Symbol[
        Optional[list[int]],
        None,
    ]

    SbSendNatNegotiateCookieToServer: Symbol[
        Optional[list[int]],
        None,
    ]

    ProcessLanData: Symbol[
        Optional[list[int]],
        None,
    ]

    SbListThink: Symbol[
        Optional[list[int]],
        None,
    ]


class Overlay0DataProtocol(Protocol):

    OV0_STATIC_INITIALIZER: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    TOP_MENU_MUSIC_ID: Symbol[
        Optional[list[int]],
        None,
    ]


Overlay0Protocol = SectionProtocol[
    Overlay0FunctionsProtocol,
    Overlay0DataProtocol,
    Optional[int],
]


class Overlay1FunctionsProtocol(Protocol):

    CreateMainMenus: Symbol[
        Optional[list[int]],
        None,
    ]

    AddMainMenuOption: Symbol[
        Optional[list[int]],
        None,
    ]

    AddSubMenuOption: Symbol[
        Optional[list[int]],
        None,
    ]

    ProcessContinueScreenContents: Symbol[
        Optional[list[int]],
        None,
    ]


class Overlay1DataProtocol(Protocol):

    PRINTS_STRINGS: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    PRINTS_STRUCT: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    MAIN_MENU_WINDOW_PARAMS_1: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    MAIN_MENU_WINDOW_PARAMS_2: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    MAIN_MENU_WINDOW_PARAMS_3: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    MAIN_MENU_WINDOW_PARAMS_4: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    CONTINUE_CHOICE: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    SUBMENU: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    MAIN_MENU: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    MAIN_MENU_WINDOW_PARAMS_5: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    MAIN_MENU_WINDOW_PARAMS_6: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    MAIN_MENU_WINDOW_PARAMS_7: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    MAIN_MENU_ITEMS_CONFIRM: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    CLEAR_MARK_PERFORMANCE_PROGRESS_FLAGS: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    MAIN_MENU_WINDOW_PARAMS_8: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    MAIN_MENU_WINDOW_PARAMS_9: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    MAIN_DEBUG_MENU_ITEMS_1: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    MAIN_MENU_WINDOW_PARAMS_10: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    MAIN_DEBUG_MENU_ITEMS_2: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    OV1_STATIC_INITIALIZER: Symbol[
        Optional[list[int]],
        Optional[int],
    ]


Overlay1Protocol = SectionProtocol[
    Overlay1FunctionsProtocol,
    Overlay1DataProtocol,
    Optional[int],
]


class Overlay10FunctionsProtocol(Protocol):

    CreateInventoryMenu: Symbol[
        Optional[list[int]],
        None,
    ]

    SetInventoryMenuState0: Symbol[
        Optional[list[int]],
        None,
    ]

    SetInventoryMenuState6: Symbol[
        Optional[list[int]],
        None,
    ]

    CloseInventoryMenu: Symbol[
        Optional[list[int]],
        None,
    ]

    IsInventoryMenuActive: Symbol[
        Optional[list[int]],
        None,
    ]

    CheckInventoryMenuField0x1A0: Symbol[
        Optional[list[int]],
        None,
    ]

    PopInventoryMenuField0x1A3: Symbol[
        Optional[list[int]],
        None,
    ]

    UpdateInventoryMenu: Symbol[
        Optional[list[int]],
        None,
    ]

    IsInventoryMenuState3: Symbol[
        Optional[list[int]],
        None,
    ]

    SprintfStatic: Symbol[
        Optional[list[int]],
        None,
    ]

    GetEffectAnimationField0x19: Symbol[
        Optional[list[int]],
        None,
    ]

    AnimationHasMoreFrames: Symbol[
        Optional[list[int]],
        None,
    ]

    GetEffectAnimation: Symbol[
        Optional[list[int]],
        None,
    ]

    GetMoveAnimation: Symbol[
        Optional[list[int]],
        None,
    ]

    GetSpecialMonsterMoveAnimation: Symbol[
        Optional[list[int]],
        None,
    ]

    GetTrapAnimation: Symbol[
        Optional[list[int]],
        None,
    ]

    GetItemAnimation1: Symbol[
        Optional[list[int]],
        None,
    ]

    GetItemAnimation2: Symbol[
        Optional[list[int]],
        None,
    ]

    GetMoveAnimationSpeed: Symbol[
        Optional[list[int]],
        None,
    ]

    DrawTeamStats: Symbol[
        Optional[list[int]],
        None,
    ]

    UpdateTeamStats: Symbol[
        Optional[list[int]],
        None,
    ]

    FreeTeamStats: Symbol[
        Optional[list[int]],
        None,
    ]

    FreeMapAndTeam: Symbol[
        Optional[list[int]],
        None,
    ]

    ProcessTeamStatsLvHp: Symbol[
        Optional[list[int]],
        None,
    ]

    ProcessTeamStatsNameGender: Symbol[
        Optional[list[int]],
        None,
    ]

    IsBackgroundTileset: Symbol[
        Optional[list[int]],
        None,
    ]

    InitTilesetBuffer: Symbol[
        Optional[list[int]],
        None,
    ]

    MainGame: Symbol[
        Optional[list[int]],
        None,
    ]


class Overlay10DataProtocol(Protocol):

    INVENTORY_MENU_DEFAULT_WINDOW_PARAMS: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    FIRST_DUNGEON_WITH_MONSTER_HOUSE_TRAPS: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    FIERY_DRUM_RECRUIT_BOOST: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    BAD_POISON_DAMAGE_COOLDOWN: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    ICY_FLUTE_RECRUIT_BOOST: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    PROTEIN_STAT_BOOST: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    WATERFALL_CRINGE_CHANCE: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    AURORA_BEAM_LOWER_ATTACK_CHANCE: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    SPAWN_CAP_NO_MONSTER_HOUSE: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    OREN_BERRY_DAMAGE: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    GOLDEN_MASK_RECRUIT_BOOST: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    IRON_TAIL_LOWER_DEFENSE_CHANCE: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    TWINEEDLE_POISON_CHANCE: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    EXTRASENSORY_CRINGE_CHANCE: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    ROCK_SLIDE_CRINGE_CHANCE: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    CRUNCH_LOWER_DEFENSE_CHANCE: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    HURL_DAMAGE: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    TRAP_BUSTER_ACTIVATION_CHANCE: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    MAGNET_PULL_ACTIVATION_CHANCE: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    FOREWARN_FORCED_MISS_CHANCE: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    UNOWN_STONE_DROP_CHANCE: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    SITRUS_BERRY_HP_RESTORATION: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    AMBER_TEAR_RECRUIT_BOOST: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    MUDDY_WATER_LOWER_ACCURACY_CHANCE: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    SILVER_WIND_BOOST_CHANCE: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    POISON_TAIL_POISON_CHANCE: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    THUNDERSHOCK_PARALYZE_CHANCE: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    BOUNCE_PARALYZE_CHANCE: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    HEADBUTT_CRINGE_CHANCE: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    FIRE_FANG_CRINGE_CHANCE: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    SACRED_FIRE_BURN_CHANCE: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    WHIRLPOOL_CONSTRICTION_CHANCE: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    EXP_ELITE_EXP_BOOST: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    MONSTER_HOUSE_MAX_NON_MONSTER_SPAWNS: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    HEAL_ORDER_HP_RESTORATION: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    CURSE_DAMAGE_COOLDOWN: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    STEEL_WING_BOOST_DEFENSE_CHANCE: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    GOLD_THORN_POWER: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    BURN_DAMAGE: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    POISON_DAMAGE: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    SPAWN_COOLDOWN: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    MIST_BALL_LOWER_SPECIAL_ATTACK_CHANCE: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    PITFALL_TRAP_DAMAGE: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    EATEN_BLAST_SEED_DAMAGE_NORMAL: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    CHARGE_BEAM_BOOST_SPECIAL_ATTACK_CHANCE: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    ORAN_BERRY_FULL_HP_BOOST: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    LIFE_SEED_HP_BOOST: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    FRIEND_BOW_FAST_FRIEND_BOOST: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    OCTAZOOKA_LOWER_ACCURACY_CHANCE: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    LUSTER_PURGE_LOWER_SPECIAL_DEFENSE_CHANCE: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    SUPER_LUCK_CRIT_RATE_BOOST: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    CONSTRICT_LOWER_SPEED_CHANCE: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    ICE_FANG_FREEZE_CHANCE: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    SMOG_POISON_CHANCE: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    CUTE_CHARM_INFATUATE_CHANCE: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    LICK_PARALYZE_CHANCE: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    THUNDER_FANG_PARALYZE_CHANCE: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    BITE_CRINGE_CHANCE: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    SKY_ATTACK_CRINGE_CHANCE: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    ICE_FANG_CRINGE_CHANCE: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    BLAZE_KICK_BURN_CHANCE: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    FLAMETHROWER_BURN_CHANCE: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    DIZZY_PUNCH_CONFUSE_CHANCE: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    SECRET_POWER_EFFECT_CHANCE: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    METAL_CLAW_BOOST_ATTACK_CHANCE: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    TECHNICIAN_MOVE_POWER_THRESHOLD: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    ARENA_TRAP_ACTIVATION_CHANCE: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    SONICBOOM_FIXED_DAMAGE: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    RAIN_ABILITY_BONUS_REGEN: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    AI_CONFUSED_NO_ATTACK_CHANCE: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    LEECH_SEED_HP_DRAIN: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    EXCLUSIVE_ITEM_EXP_BOOST: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    INGRAIN_BONUS_REGEN: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    AFTERMATH_CHANCE: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    SET_DAMAGE_STATUS_DAMAGE: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    INTIMIDATOR_ACTIVATION_CHANCE: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    WRAP_DAMAGE: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    THROWN_BLAST_SEED_DAMAGE_NORMAL: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    THROWN_BLAST_SEED_DAMAGE_BOSS: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    EATEN_BLAST_SEED_DAMAGE_BOSS: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    TYPE_ADVANTAGE_MASTER_CRIT_RATE: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    INGRAIN_BONUS_REGEN_COOLDOWN: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    ORAN_BERRY_HP_RESTORATION: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    WRAP_DAMAGE_COOLDOWN: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    SITRUS_BERRY_FULL_HP_BOOST: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    SNORE_CRINGE_CHANCE: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    METEOR_MASH_BOOST_ATTACK_CHANCE: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    CRUSH_CLAW_LOWER_DEFENSE_CHANCE: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    BURN_DAMAGE_COOLDOWN: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    SHADOW_BALL_LOWER_SPECIAL_DEFENSE_CHANCE: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    AQUA_RING_HEALING_COUNTDOWN: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    STICK_POWER: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    AQUA_RING_BONUS_REGEN: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    BUBBLE_LOWER_SPEED_CHANCE: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    ICE_BODY_BONUS_REGEN: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    POWDER_SNOW_FREEZE_CHANCE: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    POISON_STING_POISON_CHANCE: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    SPAWN_COOLDOWN_THIEF_ALERT: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    POISON_FANG_POISON_CHANCE: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    CHATOT_SCARF_BOUNCE_CHANCE: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    WEATHER_MOVE_TURN_COUNT: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    THUNDER_PARALYZE_CHANCE: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    THUNDERBOLT_PARALYZE_CHANCE: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    MONSTER_HOUSE_MAX_MONSTER_SPAWNS: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    TWISTER_CRINGE_CHANCE: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    SPEED_BOOST_TURNS: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    FAKE_OUT_CRINGE_CHANCE: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    THUNDER_FANG_CRINGE_CHANCE: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    FLARE_BLITZ_BURN_CHANCE: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    FLAME_WHEEL_BURN_CHANCE: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    SHADOW_TAG_ACTIVATION_CHANCE: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    PSYBEAM_CONFUSE_CHANCE: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    TRI_ATTACK_STATUS_CHANCE: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    MIRACLE_CHEST_EXP_BOOST: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    WONDER_CHEST_EXP_BOOST: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    SHED_SKIN_ACTIVATION_CHANCE: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    SPAWN_CAP_WITH_MONSTER_HOUSE: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    POISON_DAMAGE_COOLDOWN: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    LEECH_SEED_DAMAGE_COOLDOWN: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    THROWN_ITEM_HIT_CHANCE: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    GEO_PEBBLE_DAMAGE: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    GRAVELEROCK_DAMAGE: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    RARE_FOSSIL_DAMAGE: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    GINSENG_CHANCE_3: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    ZINC_STAT_BOOST: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    IRON_STAT_BOOST: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    CALCIUM_STAT_BOOST: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    WISH_BONUS_REGEN: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    DRAGON_RAGE_FIXED_DAMAGE: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    CORSOLA_TWIG_POWER: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    CACNEA_SPIKE_POWER: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    GOLD_FANG_POWER: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    SILVER_SPIKE_POWER: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    IRON_THORN_POWER: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    BAD_WEATHER_DAMAGE: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    SCOPE_LENS_CRIT_RATE_BOOST: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    HEALING_WISH_HP_RESTORATION: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    SKY_MELODICA_RECRUIT_BOOST: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    GRASS_CORNET_RECRUIT_BOOST: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    ROCK_HORN_RECRUIT_BOOST: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    AQUA_MONICA_RECRUIT_BOOST: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    TERRA_CYMBAL_RECRUIT_BOOST: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    ME_FIRST_MULTIPLIER: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    FACADE_DAMAGE_MULTIPLIER: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    IMPRISON_TURN_RANGE: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    SLEEP_TURN_RANGE: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    NIGHTMARE_TURN_RANGE: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    SLEEPLESSNESS_TURN_RANGE: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    REFLECT_TURN_RANGE: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    LIGHT_SCREEN_TURN_RANGE: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    SAFEGUARD_TURN_RANGE: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    MIST_TURN_RANGE: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    MAGIC_COAT_TURN_RANGE: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    BURN_DAMAGE_MULTIPLIER: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    REST_TURN_RANGE: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    MATCHUP_SUPER_EFFECTIVE_MULTIPLIER_ERRATIC_PLAYER: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    SET_REFLECT_STATUS_TURN_RANGE: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    MATCHUP_IMMUNE_MULTIPLIER: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    GASTRO_ACID_TURN_RANGE: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    HEAL_BLOCK_TURN_RANGE: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    SPORT_CONDITION_TURN_RANGE: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    SURE_SHOT_TURN_RANGE: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    DETECT_BAND_MOVE_ACCURACY_DROP: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    DECOY_TURN_RANGE: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    TINTED_LENS_MULTIPLIER: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    SMOKESCREEN_TURN_RANGE: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    PERISH_SONG_TURN_RANGE: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    SHADOW_FORCE_DAMAGE_MULTIPLIER: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    DIG_DAMAGE_MULTIPLIER: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    DIVE_DAMAGE_MULTIPLIER: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    BOUNCE_DAMAGE_MULTIPLIER: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    POWER_PITCHER_DAMAGE_MULTIPLIER: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    QUICK_DODGER_MOVE_ACCURACY_DROP: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    MATCHUP_NOT_VERY_EFFECTIVE_MULTIPLIER: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    MATCHUP_SUPER_EFFECTIVE_MULTIPLIER: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    MATCHUP_NEUTRAL_MULTIPLIER: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    MATCHUP_IMMUNE_MULTIPLIER_ERRATIC_PLAYER: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    MATCHUP_NOT_VERY_EFFECTIVE_MULTIPLIER_ERRATIC_PLAYER: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    MATCHUP_NEUTRAL_MULTIPLIER_ERRATIC_PLAYER: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    MIRROR_MOVE_TURN_RANGE: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    AIR_BLADE_DAMAGE_MULTIPLIER: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    KECLEON_SHOP_BOOST_CHANCE_MULTIPLIER: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    HIDDEN_STAIRS_SPAWN_CHANCE_MULTIPLIER: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    YAWN_TURN_RANGE: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    CRINGE_TURN_RANGE: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    SPEED_BOOST_TURN_RANGE: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    SPEED_LOWER_TURN_RANGE: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    PARALYSIS_TURN_RANGE: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    SOLARBEAM_DAMAGE_MULTIPLIER: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    SKY_ATTACK_DAMAGE_MULTIPLIER: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    WRAP_TURN_RANGE: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    RAZOR_WIND_DAMAGE_MULTIPLIER: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    FOCUS_PUNCH_DAMAGE_MULTIPLIER: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    INGRAIN_TURN_RANGE: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    SKULL_BASH_DAMAGE_MULTIPLIER: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    FLY_DAMAGE_MULTIPLIER: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    WEATHER_BALL_TYPE_TABLE: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    AI_REGULAR_ATTACK_WEIGHTS: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    LAST_RESORT_DAMAGE_MULT_TABLE: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    SYNTHESIS_HP_RESTORATION_TABLE: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    ROOST_HP_RESTORATION_TABLE: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    MOONLIGHT_HP_RESTORATION_TABLE: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    MORNING_SUN_HP_RESTORATION_TABLE: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    REVERSAL_DAMAGE_MULT_TABLE: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    WATER_SPOUT_DAMAGE_MULT_TABLE: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    WRING_OUT_DAMAGE_MULT_TABLE: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    ERUPTION_DAMAGE_MULT_TABLE: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    WEATHER_BALL_DAMAGE_MULT_TABLE: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    EAT_ITEM_EFFECT_IGNORE_LIST: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    CASTFORM_WEATHER_ATTRIBUTE_TABLE: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    BAD_POISON_DAMAGE_TABLE: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    TYPE_MATCHUP_COMBINATOR_TABLE: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    OFFENSIVE_STAT_STAGE_MULTIPLIERS: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    DEFENSIVE_STAT_STAGE_MULTIPLIERS: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    NATURE_POWER_TABLE: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    APPLES_AND_BERRIES_ITEM_IDS: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    RECRUITMENT_LEVEL_BOOST_TABLE: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    NATURAL_GIFT_ITEM_TABLE: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    RANDOM_MUSIC_ID_TABLE: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    SHOP_ITEM_CHANCES: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    MALE_ACCURACY_STAGE_MULTIPLIERS: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    MALE_EVASION_STAGE_MULTIPLIERS: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    FEMALE_ACCURACY_STAGE_MULTIPLIERS: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    FEMALE_EVASION_STAGE_MULTIPLIERS: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    MUSIC_ID_TABLE: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    TYPE_MATCHUP_TABLE: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    FIXED_ROOM_MONSTER_SPAWN_STATS_TABLE: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    METRONOME_TABLE: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    TILESET_PROPERTIES: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    FIXED_ROOM_PROPERTIES_TABLE: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    TRAP_ANIMATION_INFO: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    ITEM_ANIMATION_INFO: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    MOVE_ANIMATION_INFO: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    EFFECT_ANIMATION_INFO: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    SPECIAL_MONSTER_MOVE_ANIMATION_INFO: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    OV10_STATIC_INITIALIZER: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    DEFEAT_ITEM_LOSS_CHANCE: Symbol[
        Optional[list[int]],
        None,
    ]


Overlay10Protocol = SectionProtocol[
    Overlay10FunctionsProtocol,
    Overlay10DataProtocol,
    Optional[int],
]


class Overlay11FunctionsProtocol(Protocol):

    InitScriptRoutineState: Symbol[
        Optional[list[int]],
        None,
    ]

    InitScriptRoutine: Symbol[
        Optional[list[int]],
        None,
    ]

    LockRoutine: Symbol[
        Optional[list[int]],
        None,
    ]

    UnlockRoutine: Symbol[
        Optional[list[int]],
        None,
    ]

    UnlockScriptingLock: Symbol[
        Optional[list[int]],
        None,
    ]

    FuncThatCallsRunNextOpcode: Symbol[
        Optional[list[int]],
        None,
    ]

    RunNextOpcode: Symbol[
        Optional[list[int]],
        None,
    ]

    GetSsbString: Symbol[
        Optional[list[int]],
        None,
    ]

    HandleUnlocks: Symbol[
        Optional[list[int]],
        None,
    ]

    ScriptCaseProcess: Symbol[
        Optional[list[int]],
        None,
    ]

    LoadFileFromRomVeneer: Symbol[
        Optional[list[int]],
        None,
    ]

    SsbLoad2: Symbol[
        Optional[list[int]],
        None,
    ]

    ScriptParamToInt: Symbol[
        Optional[list[int]],
        None,
    ]

    ScriptParamToFixedPoint16: Symbol[
        Optional[list[int]],
        None,
    ]

    StationLoadHanger: Symbol[
        Optional[list[int]],
        None,
    ]

    ScriptStationLoadTalk: Symbol[
        Optional[list[int]],
        None,
    ]

    SsbLoad1: Symbol[
        Optional[list[int]],
        None,
    ]

    ScriptSpecialProcessCall: Symbol[
        Optional[list[int]],
        None,
    ]

    GetCoroutineInfo: Symbol[
        Optional[list[int]],
        None,
    ]

    GetSpecialRecruitmentSpecies: Symbol[
        Optional[list[int]],
        None,
    ]

    PrepareMenuAcceptTeamMember: Symbol[
        Optional[list[int]],
        None,
    ]

    InitRandomNpcJobs: Symbol[
        Optional[list[int]],
        None,
    ]

    GetRandomNpcJobType: Symbol[
        Optional[list[int]],
        None,
    ]

    GetRandomNpcJobSubtype: Symbol[
        Optional[list[int]],
        None,
    ]

    GetRandomNpcJobStillAvailable: Symbol[
        Optional[list[int]],
        None,
    ]

    AcceptRandomNpcJob: Symbol[
        Optional[list[int]],
        None,
    ]

    GroundMainLoop: Symbol[
        Optional[list[int]],
        None,
    ]

    GetAllocArenaGround: Symbol[
        Optional[list[int]],
        None,
    ]

    GetFreeArenaGround: Symbol[
        Optional[list[int]],
        None,
    ]

    GroundMainReturnDungeon: Symbol[
        Optional[list[int]],
        None,
    ]

    GroundMainNextDay: Symbol[
        Optional[list[int]],
        None,
    ]

    JumpToTitleScreen: Symbol[
        Optional[list[int]],
        None,
    ]

    ReturnToTitleScreen: Symbol[
        Optional[list[int]],
        None,
    ]

    ScriptSpecialProcess0x16: Symbol[
        Optional[list[int]],
        None,
    ]

    IsScreenFadeInProgress: Symbol[
        Optional[list[int]],
        None,
    ]

    LoadBackgroundAttributes: Symbol[
        Optional[list[int]],
        None,
    ]

    GroundBgInit: Symbol[
        Optional[list[int]],
        None,
    ]

    GroundBgFreeAll: Symbol[
        Optional[list[int]],
        None,
    ]

    GroundBgCloseOpenedFiles: Symbol[
        Optional[list[int]],
        None,
    ]

    LoadMapType10: Symbol[
        Optional[list[int]],
        None,
    ]

    LoadMapType11: Symbol[
        Optional[list[int]],
        None,
    ]

    BmaLayerNrlDecompressor: Symbol[
        Optional[list[int]],
        None,
    ]

    GetSpecialLayoutBackground: Symbol[
        Optional[list[int]],
        None,
    ]

    SetAnimDataFields: Symbol[
        Optional[list[int]],
        None,
    ]

    SetAnimDataFieldsWrapper: Symbol[
        Optional[list[int]],
        None,
    ]

    InitAnimDataFromOtherAnimData: Symbol[
        Optional[list[int]],
        None,
    ]

    SetAnimDataFields2: Symbol[
        Optional[list[int]],
        None,
    ]

    GetIdleAnimationType: Symbol[
        Optional[list[int]],
        None,
    ]

    LoadObjectAnimData: Symbol[
        Optional[list[int]],
        None,
    ]

    InitAnimDataFromOtherAnimDataVeneer: Symbol[
        Optional[list[int]],
        None,
    ]

    AnimRelatedFunction: Symbol[
        Optional[list[int]],
        None,
    ]

    UnlockMainRoutine: Symbol[
        Optional[list[int]],
        None,
    ]

    AllocAndInitPartnerFollowDataAndLiveActorList: Symbol[
        Optional[list[int]],
        None,
    ]

    InitPartnerFollowDataAndLiveActorList: Symbol[
        Optional[list[int]],
        None,
    ]

    GetLiveActorIdxFromScriptEntityId: Symbol[
        Optional[list[int]],
        None,
    ]

    DeleteLiveActor: Symbol[
        Optional[list[int]],
        None,
    ]

    SetAttributeBitfieldLiveActor: Symbol[
        Optional[list[int]],
        None,
    ]

    ResetAttributeBitfieldLiveActor: Symbol[
        Optional[list[int]],
        None,
    ]

    UnlockActorRoutines: Symbol[
        Optional[list[int]],
        None,
    ]

    GetCollidingActorId: Symbol[
        Optional[list[int]],
        None,
    ]

    ChangeActorAnimation: Symbol[
        Optional[list[int]],
        None,
    ]

    SetPositionLiveActor: Symbol[
        Optional[list[int]],
        None,
    ]

    GetIdLiveActor: Symbol[
        Optional[list[int]],
        None,
    ]

    GetCollisionBoxLiveActor: Symbol[
        Optional[list[int]],
        None,
    ]

    SetPositionInitialLiveActor: Symbol[
        Optional[list[int]],
        None,
    ]

    SetMovementRangeLiveActor: Symbol[
        Optional[list[int]],
        None,
    ]

    GetCollisionBoxCenterLiveActor: Symbol[
        Optional[list[int]],
        None,
    ]

    SetPositionLiveActorVeneer: Symbol[
        Optional[list[int]],
        None,
    ]

    GetHeightLiveActor: Symbol[
        Optional[list[int]],
        None,
    ]

    SetHeightLiveActor: Symbol[
        Optional[list[int]],
        None,
    ]

    GetDirectionLiveActor: Symbol[
        Optional[list[int]],
        None,
    ]

    SetDirectionLiveActor: Symbol[
        Optional[list[int]],
        None,
    ]

    SetAnimationLiveActor: Symbol[
        Optional[list[int]],
        None,
    ]

    SetEffectLiveActor: Symbol[
        Optional[list[int]],
        None,
    ]

    GetAnimationStatusLiveActor: Symbol[
        Optional[list[int]],
        None,
    ]

    GetEffectStatusLiveActor: Symbol[
        Optional[list[int]],
        None,
    ]

    GetAttributeBitfieldLiveActor: Symbol[
        Optional[list[int]],
        None,
    ]

    SetAttributeBitfieldLiveActorWrapper: Symbol[
        Optional[list[int]],
        None,
    ]

    ResetAttributeBitfieldLiveActorWrapper: Symbol[
        Optional[list[int]],
        None,
    ]

    SetBlinkLiveActor: Symbol[
        Optional[list[int]],
        None,
    ]

    SetPositionOffsetLiveActor: Symbol[
        Optional[list[int]],
        None,
    ]

    InitPartnerFollowData: Symbol[
        Optional[list[int]],
        None,
    ]

    DeleteLiveObject: Symbol[
        Optional[list[int]],
        None,
    ]

    SetAttributeBitfieldLiveObject: Symbol[
        Optional[list[int]],
        None,
    ]

    ResetAttributeBitfieldLiveObject: Symbol[
        Optional[list[int]],
        None,
    ]

    UnlockObjectRoutines: Symbol[
        Optional[list[int]],
        None,
    ]

    GetCollidingObjectId: Symbol[
        Optional[list[int]],
        None,
    ]

    SetPositionLiveObject: Symbol[
        Optional[list[int]],
        None,
    ]

    GetIdLiveObject: Symbol[
        Optional[list[int]],
        None,
    ]

    GetCollisionBoxLiveObject: Symbol[
        Optional[list[int]],
        None,
    ]

    SetPositionInitialLiveObject: Symbol[
        Optional[list[int]],
        None,
    ]

    SetMovementRangeLiveObject: Symbol[
        Optional[list[int]],
        None,
    ]

    GetCollisionBoxCenterLiveObject: Symbol[
        Optional[list[int]],
        None,
    ]

    SetPositionLiveObjectVeneer: Symbol[
        Optional[list[int]],
        None,
    ]

    GetHeightLiveObject: Symbol[
        Optional[list[int]],
        None,
    ]

    SetHeightLiveObject: Symbol[
        Optional[list[int]],
        None,
    ]

    GetDirectionLiveObject: Symbol[
        Optional[list[int]],
        None,
    ]

    SetDirectionLiveObject: Symbol[
        Optional[list[int]],
        None,
    ]

    SetAnimationLiveObject: Symbol[
        Optional[list[int]],
        None,
    ]

    SetEffectLiveObject: Symbol[
        Optional[list[int]],
        None,
    ]

    GetAnimationStatusLiveObject: Symbol[
        Optional[list[int]],
        None,
    ]

    GetEffectStatusLiveObject: Symbol[
        Optional[list[int]],
        None,
    ]

    GetAttributeBitfieldLiveObject: Symbol[
        Optional[list[int]],
        None,
    ]

    SetAttributeBitfieldLiveObjectWrapper: Symbol[
        Optional[list[int]],
        None,
    ]

    ResetAttributeBitfieldLiveObjectWrapper: Symbol[
        Optional[list[int]],
        None,
    ]

    SetBlinkLiveObject: Symbol[
        Optional[list[int]],
        None,
    ]

    SetPositionOffsetLiveObject: Symbol[
        Optional[list[int]],
        None,
    ]

    DeleteLivePerformer: Symbol[
        Optional[list[int]],
        None,
    ]

    SetAttributeBitfieldLivePerformer: Symbol[
        Optional[list[int]],
        None,
    ]

    ResetAttributeBitfieldLivePerformer: Symbol[
        Optional[list[int]],
        None,
    ]

    UnlockPerformerRoutines: Symbol[
        Optional[list[int]],
        None,
    ]

    SetPositionLivePerformer: Symbol[
        Optional[list[int]],
        None,
    ]

    GetIdLivePerformer: Symbol[
        Optional[list[int]],
        None,
    ]

    GetCollisionBoxLivePerformer: Symbol[
        Optional[list[int]],
        None,
    ]

    SetPositionInitialLivePerformer: Symbol[
        Optional[list[int]],
        None,
    ]

    SetMovementRangeLivePerformer: Symbol[
        Optional[list[int]],
        None,
    ]

    GetCollisionBoxCenterLivePerformer: Symbol[
        Optional[list[int]],
        None,
    ]

    SetPositionLivePerformerVeneer: Symbol[
        Optional[list[int]],
        None,
    ]

    GetHeightLivePerformer: Symbol[
        Optional[list[int]],
        None,
    ]

    SetHeightLivePerformer: Symbol[
        Optional[list[int]],
        None,
    ]

    GetDirectionLivePerformer: Symbol[
        Optional[list[int]],
        None,
    ]

    SetDirectionLivePerformer: Symbol[
        Optional[list[int]],
        None,
    ]

    SetAnimationLivePerformer: Symbol[
        Optional[list[int]],
        None,
    ]

    SetEffectLivePerformer: Symbol[
        Optional[list[int]],
        None,
    ]

    GetAnimationStatusLivePerformer: Symbol[
        Optional[list[int]],
        None,
    ]

    GetEffectStatusLivePerformer: Symbol[
        Optional[list[int]],
        None,
    ]

    GetAttributeBitfieldLivePerformer: Symbol[
        Optional[list[int]],
        None,
    ]

    SetAttributeBitfieldLivePerformerWrapper: Symbol[
        Optional[list[int]],
        None,
    ]

    ResetAttributeBitfieldLivePerformerWrapper: Symbol[
        Optional[list[int]],
        None,
    ]

    SetBlinkLivePerformer: Symbol[
        Optional[list[int]],
        None,
    ]

    SetPositionOffsetLivePerformer: Symbol[
        Optional[list[int]],
        None,
    ]

    DeleteLiveEvent: Symbol[
        Optional[list[int]],
        None,
    ]

    GetCollidingEventId: Symbol[
        Optional[list[int]],
        None,
    ]

    CreateTeamInfoBox: Symbol[
        Optional[list[int]],
        None,
    ]

    CloseTeamInfoBox: Symbol[
        Optional[list[int]],
        None,
    ]

    IsTeamInfoBoxActive: Symbol[
        Optional[list[int]],
        None,
    ]

    UpdateTeamInfoBox: Symbol[
        Optional[list[int]],
        None,
    ]

    CreateTopGroundMenu: Symbol[
        Optional[list[int]],
        None,
    ]

    CloseTopGroundMenu: Symbol[
        Optional[list[int]],
        None,
    ]

    UpdateTopGroundMenu: Symbol[
        Optional[list[int]],
        None,
    ]

    IsBagNotEmpty: Symbol[
        Optional[list[int]],
        None,
    ]

    SprintfStatic: Symbol[
        Optional[list[int]],
        None,
    ]

    GetExclusiveItemRequirements: Symbol[
        Optional[list[int]],
        None,
    ]

    SwapShopInventoryManager: Symbol[
        Optional[list[int]],
        None,
    ]

    HandleControlsTopScreenGround: Symbol[
        Optional[list[int]],
        None,
    ]

    GetDungeonMapPos: Symbol[
        Optional[list[int]],
        None,
    ]

    WorldMapSetMode: Symbol[
        Optional[list[int]],
        None,
    ]

    WorldMapSetCamera: Symbol[
        Optional[list[int]],
        None,
    ]

    StatusUpdate: Symbol[
        Optional[list[int]],
        None,
    ]

    HandleTeamStatsGround: Symbol[
        Optional[list[int]],
        None,
    ]


class Overlay11DataProtocol(Protocol):

    OVERLAY11_UNKNOWN_TABLE__NA_2316A38: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    SCRIPT_COMMAND_PARSING_DATA: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    SCRIPT_OP_CODE_NAMES: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    SCRIPT_OP_CODES: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    OVERLAY11_DEBUG_STRINGS: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    C_ROUTINE_NAMES: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    C_ROUTINES: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    GROUND_WEATHER_TABLE: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    GROUND_WAN_FILES_TABLE: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    OBJECTS: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    RECRUITMENT_TABLE_LOCATIONS: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    RECRUITMENT_TABLE_LEVELS: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    RECRUITMENT_TABLE_SPECIES: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    POSITION_ZERO: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    LEVEL_TILEMAP_LIST: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    ACTOR_FUNCTION_TABLE: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    SETANIMATION_TABLE: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    OBJECT_FUNCTION_TABLE: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    PERFORMER_FUNCTION_TABLE: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    TEAM_INFO_BOX_DEFAULT_WINDOW_PARAMS: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    OVERLAY11_OVERLAY_LOAD_TABLE: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    OV11_STATIC_INITIALIZER: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    UNIONALL_RAM_ADDRESS: Symbol[
        Optional[list[int]],
        None,
    ]

    GROUND_STATE_MAP: Symbol[
        Optional[list[int]],
        None,
    ]

    GROUND_STATE_WEATHER: Symbol[
        Optional[list[int]],
        None,
    ]

    GROUND_STATE_PTRS: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    SWAP_SHOP_INVENTORY_PTRS: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    WORLD_MAP_MODE: Symbol[
        Optional[list[int]],
        Optional[int],
    ]


Overlay11Protocol = SectionProtocol[
    Overlay11FunctionsProtocol,
    Overlay11DataProtocol,
    Optional[int],
]


class Overlay12FunctionsProtocol(Protocol):

    pass


class Overlay12DataProtocol(Protocol):

    OV12_STATIC_INITIALIZER: Symbol[
        Optional[list[int]],
        Optional[int],
    ]


Overlay12Protocol = SectionProtocol[
    Overlay12FunctionsProtocol,
    Overlay12DataProtocol,
    Optional[int],
]


class Overlay13FunctionsProtocol(Protocol):

    PersonalityTestEntryPoint: Symbol[
        Optional[list[int]],
        None,
    ]

    PersonalityTestDestructor: Symbol[
        Optional[list[int]],
        None,
    ]

    PersonalityTestFrameUpdate: Symbol[
        Optional[list[int]],
        None,
    ]

    PersonalityTestMainManager: Symbol[
        Optional[list[int]],
        None,
    ]

    GetPersonality: Symbol[
        Optional[list[int]],
        None,
    ]

    GetPartnerOptionString: Symbol[
        Optional[list[int]],
        None,
    ]

    WaitForNextStep: Symbol[
        Optional[list[int]],
        None,
    ]

    DrawPersonalityTestDebug: Symbol[
        Optional[list[int]],
        None,
    ]


class Overlay13DataProtocol(Protocol):

    QUIZ_BORDER_COLOR_TABLE: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    PARTNER_PORTRAIT_OFFSET: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    PLAY_OLD_GAME_BOOST: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    OVERLAY13_LOAD_ENTRY: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    MAIN_DBOX_WINDOW_PARAMS: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    AURA_BOW_DBOX_WINDOW_PARAMS: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    DEBUG_WINDOW_PARAMS: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    QUIZ_INTRO_WINDOW_PARAMS: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    CONFIRM_PARTNER_MENU_ITEMS: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    STARTERS_PARTNER_IDS: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    STARTERS_HERO_IDS: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    STARTERS_TYPE_INCOMPATIBILITY_TABLE: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    STARTERS_STRINGS: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    QUIZ_QUESTION_STRINGS: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    QUIZ_ANSWER_STRINGS: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    QUIZ_ANSWER_POINTS: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    OV13_STATIC_INITIALIZER: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    PERSONALITY_TEST_PTR: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    PARTNER_SELECT_MENU_OPTION_TRACKER: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    PARTNER_SELECT_MENU_OPTION_TIMER: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    QUESTION_ANSWER_WINDOW_PARAMS: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    CHOOSE_PARTNER_WINDOW_PARAMS: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    QUIZ_QUESTION_MENU_ITEMS: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    OVERLAY13_UNKNOWN_STRUCT__NA_238CF14: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    QUIZ_ANSWER_ASSOCIATIONS: Symbol[
        Optional[list[int]],
        Optional[int],
    ]


Overlay13Protocol = SectionProtocol[
    Overlay13FunctionsProtocol,
    Overlay13DataProtocol,
    Optional[int],
]


class Overlay14FunctionsProtocol(Protocol):

    SentrySetupState: Symbol[
        Optional[list[int]],
        None,
    ]

    SentryUpdateDisplay: Symbol[
        Optional[list[int]],
        None,
    ]

    SentrySetExitingState: Symbol[
        Optional[list[int]],
        None,
    ]

    SentryRunState: Symbol[
        Optional[list[int]],
        None,
    ]

    SentrySetStateIntermediate: Symbol[
        Optional[list[int]],
        None,
    ]

    SentryState0: Symbol[
        Optional[list[int]],
        None,
    ]

    SentryState1: Symbol[
        Optional[list[int]],
        None,
    ]

    SentryState2: Symbol[
        Optional[list[int]],
        None,
    ]

    SentryState3: Symbol[
        Optional[list[int]],
        None,
    ]

    SentryState4: Symbol[
        Optional[list[int]],
        None,
    ]

    SentryStateExit: Symbol[
        Optional[list[int]],
        None,
    ]

    SentryState6: Symbol[
        Optional[list[int]],
        None,
    ]

    SentryState7: Symbol[
        Optional[list[int]],
        None,
    ]

    SentryState8: Symbol[
        Optional[list[int]],
        None,
    ]

    SentryState9: Symbol[
        Optional[list[int]],
        None,
    ]

    SentryStateA: Symbol[
        Optional[list[int]],
        None,
    ]

    SentryStateB: Symbol[
        Optional[list[int]],
        None,
    ]

    SentryStateGenerateChoices: Symbol[
        Optional[list[int]],
        None,
    ]

    SentryStateGetUserChoice: Symbol[
        Optional[list[int]],
        None,
    ]

    SentryStateFinalizeRound: Symbol[
        Optional[list[int]],
        None,
    ]

    SentryStateF: Symbol[
        Optional[list[int]],
        None,
    ]

    SentryState10: Symbol[
        Optional[list[int]],
        None,
    ]

    SentryState11: Symbol[
        Optional[list[int]],
        None,
    ]

    SentryState12: Symbol[
        Optional[list[int]],
        None,
    ]

    SentryState13: Symbol[
        Optional[list[int]],
        None,
    ]

    SentryState14: Symbol[
        Optional[list[int]],
        None,
    ]

    SentryState15: Symbol[
        Optional[list[int]],
        None,
    ]

    SentryState16: Symbol[
        Optional[list[int]],
        None,
    ]

    SentryState17: Symbol[
        Optional[list[int]],
        None,
    ]

    SentryState18: Symbol[
        Optional[list[int]],
        None,
    ]

    SentryState19: Symbol[
        Optional[list[int]],
        None,
    ]

    SentryState1A: Symbol[
        Optional[list[int]],
        None,
    ]

    SentryStateFinalizePoints: Symbol[
        Optional[list[int]],
        None,
    ]

    SentryState1C: Symbol[
        Optional[list[int]],
        None,
    ]

    SentryState1D: Symbol[
        Optional[list[int]],
        None,
    ]

    SentryState1E: Symbol[
        Optional[list[int]],
        None,
    ]

    SentryState1F: Symbol[
        Optional[list[int]],
        None,
    ]

    SentryState20: Symbol[
        Optional[list[int]],
        None,
    ]

    SentryState21: Symbol[
        Optional[list[int]],
        None,
    ]


class Overlay14DataProtocol(Protocol):

    SENTRY_DUTY_STRUCT_SIZE: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    SENTRY_LOUDRED_MONSTER_ID: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    STRING_ID_SENTRY_TOP_SESSIONS: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    STRING_ID_SENTRY_INSTRUCTIONS: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    STRING_ID_SENTRY_HERE_COMES: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    STRING_ID_SENTRY_WHOSE_FOOTPRINT: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    STRING_ID_SENTRY_TRY_AGAIN: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    STRING_ID_SENTRY_OUT_OF_TIME: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    STRING_ID_SENTRY_FOOTPRINT_IS_6EE: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    STRING_ID_SENTRY_COME_IN_6EF: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    STRING_ID_SENTRY_WRONG: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    STRING_ID_SENTRY_BUCK_UP: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    STRING_ID_SENTRY_FOOTPRINT_IS_6EC: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    STRING_ID_SENTRY_COME_IN_6ED: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    STRING_ID_SENTRY_KEEP_YOU_WAITING: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    STRING_ID_SENTRY_THATLL_DO_IT: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    SENTRY_CHATOT_MONSTER_ID: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    STRING_ID_SENTRY_NO_MORE_VISITORS: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    STRING_ID_SENTRY_THATS_ALL: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    SENTRY_GROVYLE_MONSTER_ID: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    SENTRY_DEBUG_MENU_ITEMS: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    OV14_STATIC_INITIALIZER: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    SENTRY_DUTY_PTR: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    SENTRY_DUTY_STATE_HANDLER_TABLE: Symbol[
        Optional[list[int]],
        Optional[int],
    ]


Overlay14Protocol = SectionProtocol[
    Overlay14FunctionsProtocol,
    Overlay14DataProtocol,
    Optional[int],
]


class Overlay15FunctionsProtocol(Protocol):

    pass


class Overlay15DataProtocol(Protocol):

    BANK_MAIN_MENU_ITEMS: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    BANK_WINDOW_PARAMS_1: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    BANK_WINDOW_PARAMS_2: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    BANK_WINDOW_PARAMS_3: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    BANK_WINDOW_PARAMS_4: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    BANK_WINDOW_PARAMS_5: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    OV15_STATIC_INITIALIZER: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    OVERLAY15_UNKNOWN_POINTER__NA_238B180: Symbol[
        Optional[list[int]],
        Optional[int],
    ]


Overlay15Protocol = SectionProtocol[
    Overlay15FunctionsProtocol,
    Overlay15DataProtocol,
    Optional[int],
]


class Overlay16FunctionsProtocol(Protocol):

    pass


class Overlay16DataProtocol(Protocol):

    EVO_MENU_ITEMS_CONFIRM: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    EVO_SUBMENU_ITEMS: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    EVO_MAIN_MENU_ITEMS: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    EVO_MENU_STRING_IDS: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    EVO_WINDOW_PARAMS_1: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    EVO_WINDOW_PARAMS_2: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    EVO_WINDOW_PARAMS_3: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    EVO_WINDOW_PARAMS_4: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    EVO_WINDOW_PARAMS_5: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    EVO_WINDOW_PARAMS_6: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    EVO_WINDOW_PARAMS_7: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    OV16_STATIC_INITIALIZER: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    OVERLAY16_UNKNOWN_POINTER__NA_238CE40: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    OVERLAY16_UNKNOWN_POINTER__NA_238CE58: Symbol[
        Optional[list[int]],
        Optional[int],
    ]


Overlay16Protocol = SectionProtocol[
    Overlay16FunctionsProtocol,
    Overlay16DataProtocol,
    Optional[int],
]


class Overlay17FunctionsProtocol(Protocol):

    pass


class Overlay17DataProtocol(Protocol):

    ASSEMBLY_WINDOW_PARAMS_1: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    ASSEMBLY_WINDOW_PARAMS_2: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    ASSEMBLY_WINDOW_PARAMS_3: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    ASSEMBLY_WINDOW_PARAMS_4: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    ASSEMBLY_WINDOW_PARAMS_5: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    ASSEMBLY_MENU_ITEMS_CONFIRM: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    ASSEMBLY_MAIN_MENU_ITEMS_1: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    ASSEMBLY_MAIN_MENU_ITEMS_2: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    ASSEMBLY_SUBMENU_ITEMS_1: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    ASSEMBLY_SUBMENU_ITEMS_2: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    ASSEMBLY_SUBMENU_ITEMS_3: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    ASSEMBLY_SUBMENU_ITEMS_4: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    ASSEMBLY_SUBMENU_ITEMS_5: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    ASSEMBLY_SUBMENU_ITEMS_6: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    ASSEMBLY_SUBMENU_ITEMS_7: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    OVERLAY17_FUNCTION_POINTER_TABLE: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    OV17_STATIC_INITIALIZER: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    OVERLAY17_UNKNOWN_POINTER__NA_238BE00: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    OVERLAY17_UNKNOWN_POINTER__NA_238BE04: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    OVERLAY17_UNKNOWN_POINTER__NA_238BE08: Symbol[
        Optional[list[int]],
        Optional[int],
    ]


Overlay17Protocol = SectionProtocol[
    Overlay17FunctionsProtocol,
    Overlay17DataProtocol,
    Optional[int],
]


class Overlay18FunctionsProtocol(Protocol):

    LinkShopEntryPoint: Symbol[
        Optional[list[int]],
        None,
    ]

    LinkShopDestructor: Symbol[
        Optional[list[int]],
        None,
    ]

    LinkShopMainManager: Symbol[
        Optional[list[int]],
        None,
    ]


class Overlay18DataProtocol(Protocol):

    LINK_SHOP_WINDOW_PARAMS_1: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    LINK_SHOP_WINDOW_PARAMS_2: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    LINK_SHOP_WINDOW_PARAMS_3: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    LINK_SHOP_WINDOW_PARAMS_4: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    LINK_SHOP_WINDOW_PARAMS_5: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    LINK_SHOP_WINDOW_PARAMS_6: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    LINK_SHOP_WINDOW_PARAMS_7: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    LINK_SHOP_WINDOW_PARAMS_8: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    LINK_SHOP_WINDOW_PARAMS_9: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    LINK_SHOP_WINDOW_PARAMS_10: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    LINK_SHOP_WINDOW_PARAMS_11: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    LINK_SHOP_MENU_ITEMS_CONFIRM: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    LINK_SHOP_SUBMENU_ITEMS_1: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    LINK_SHOP_SUBMENU_ITEMS_2: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    LINK_SHOP_MAIN_MENU_ITEMS: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    LINK_SHOP_SUBMENU_ITEMS_3: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    LINK_SHOP_SUBMENU_ITEMS_4: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    LINK_SHOP_SUBMENU_ITEMS_5: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    LINK_SHOP_SUBMENU_ITEMS_6: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    LINK_SHOP_SUBMENU_ITEMS_7: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    OVERLAY18_FUNCTION_POINTER_TABLE: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    OV18_STATIC_INITIALIZER: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    LINK_SHOP_PTR: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    OVERLAY18_UNKNOWN_POINTER__NA_238D624: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    OVERLAY18_UNKNOWN_POINTER__NA_238D628: Symbol[
        Optional[list[int]],
        Optional[int],
    ]


Overlay18Protocol = SectionProtocol[
    Overlay18FunctionsProtocol,
    Overlay18DataProtocol,
    Optional[int],
]


class Overlay19FunctionsProtocol(Protocol):

    GetBarItem: Symbol[
        Optional[list[int]],
        None,
    ]

    GetRecruitableMonsterAll: Symbol[
        Optional[list[int]],
        None,
    ]

    GetRecruitableMonsterList: Symbol[
        Optional[list[int]],
        None,
    ]

    GetRecruitableMonsterListRestricted: Symbol[
        Optional[list[int]],
        None,
    ]


class Overlay19DataProtocol(Protocol):

    OVERLAY19_UNKNOWN_TABLE__NA_238DAE0: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    BAR_UNLOCKABLE_DUNGEONS_TABLE: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    BAR_RECRUITABLE_MONSTER_TABLE: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    BAR_AVAILABLE_ITEMS: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    OVERLAY19_UNKNOWN_STRING_IDS__NA_238E178: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    OVERLAY19_UNKNOWN_STRUCT__NA_238E1A4: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    OVERLAY19_UNKNOWN_STRING_IDS__NA_238E1CC: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    BAR_WINDOW_PARAMS_1: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    BAR_WINDOW_PARAMS_2: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    BAR_WINDOW_PARAMS_3: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    BAR_MENU_ITEMS_CONFIRM_1: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    BAR_MENU_ITEMS_CONFIRM_2: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    OVERLAY19_UNKNOWN_STRING_IDS__NA_238E238: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    BAR_MAIN_MENU_ITEMS: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    BAR_SUBMENU_ITEMS_1: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    BAR_SUBMENU_ITEMS_2: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    OV19_STATIC_INITIALIZER: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    OVERLAY19_UNKNOWN_POINTER__NA_238E360: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    OVERLAY19_UNKNOWN_POINTER__NA_238E364: Symbol[
        Optional[list[int]],
        Optional[int],
    ]


Overlay19Protocol = SectionProtocol[
    Overlay19FunctionsProtocol,
    Overlay19DataProtocol,
    Optional[int],
]


class Overlay2FunctionsProtocol(Protocol):

    InitWfcSettingsOverlay: Symbol[
        Optional[list[int]],
        None,
    ]

    Nns_FndInitList: Symbol[
        Optional[list[int]],
        None,
    ]

    SetFirstObject: Symbol[
        Optional[list[int]],
        None,
    ]

    Nns_FndAppendListObject: Symbol[
        Optional[list[int]],
        None,
    ]

    Nns_FndPrependListObject: Symbol[
        Optional[list[int]],
        None,
    ]

    Nns_FndInsertListObject: Symbol[
        Optional[list[int]],
        None,
    ]

    Nns_FndRemoveListObject: Symbol[
        Optional[list[int]],
        None,
    ]

    Nns_FndGetNextListObject: Symbol[
        Optional[list[int]],
        None,
    ]

    Nns_FndGetPrevListObject: Symbol[
        Optional[list[int]],
        None,
    ]

    FindContainHeap: Symbol[
        Optional[list[int]],
        None,
    ]

    FindListContainHeap: Symbol[
        Optional[list[int]],
        None,
    ]

    Nnsi_FndInitHeapHead: Symbol[
        Optional[list[int]],
        None,
    ]

    Nnsi_FndFinalizeHeap: Symbol[
        Optional[list[int]],
        None,
    ]

    GetRegionOfMBlock: Symbol[
        Optional[list[int]],
        None,
    ]

    RemoveMBlock: Symbol[
        Optional[list[int]],
        None,
    ]

    InsertMBlock: Symbol[
        Optional[list[int]],
        None,
    ]

    InitMBlock: Symbol[
        Optional[list[int]],
        None,
    ]

    InitExpHeap: Symbol[
        Optional[list[int]],
        None,
    ]

    AllocUsedBlockFromFreeBlock: Symbol[
        Optional[list[int]],
        None,
    ]

    ExpHeap_AllocFromHead: Symbol[
        Optional[list[int]],
        None,
    ]

    ExpHeap_AllocFromTail: Symbol[
        Optional[list[int]],
        None,
    ]

    RecycleRegion: Symbol[
        Optional[list[int]],
        None,
    ]

    Nns_FndCreateExpHeapEx: Symbol[
        Optional[list[int]],
        None,
    ]

    Nns_FndDestroyExpHeap: Symbol[
        Optional[list[int]],
        None,
    ]

    Nns_FndAllocFromExpHeapEx: Symbol[
        Optional[list[int]],
        None,
    ]

    Nns_FndFreeToExpHeap: Symbol[
        Optional[list[int]],
        None,
    ]

    InitFrameHeap: Symbol[
        Optional[list[int]],
        None,
    ]

    FrmHeap_AllocFromHead: Symbol[
        Optional[list[int]],
        None,
    ]

    FrmHeap_AllocFromTail: Symbol[
        Optional[list[int]],
        None,
    ]

    FrmHeap_FreeHead: Symbol[
        Optional[list[int]],
        None,
    ]

    FrmHeap_FreeTail: Symbol[
        Optional[list[int]],
        None,
    ]

    Nns_FndCreateFrmHeapEx: Symbol[
        Optional[list[int]],
        None,
    ]

    Nns_FndDestroyFrmHeap: Symbol[
        Optional[list[int]],
        None,
    ]

    Nns_FndAllocFromFrmHeapEx: Symbol[
        Optional[list[int]],
        None,
    ]

    Nns_FndFreeToFrmHeap: Symbol[
        Optional[list[int]],
        None,
    ]

    Nns_G2dFindBinaryBlock: Symbol[
        Optional[list[int]],
        None,
    ]

    GetGlyphIndex: Symbol[
        Optional[list[int]],
        None,
    ]

    Nns_G2dFontInitUtf16: Symbol[
        Optional[list[int]],
        None,
    ]

    Nns_G2dFontFindGlyphIndex: Symbol[
        Optional[list[int]],
        None,
    ]

    Nns_G2dFontGetCharWidthsFromIndex: Symbol[
        Optional[list[int]],
        None,
    ]

    Nnsi_G2dFontGetStringWidth: Symbol[
        Optional[list[int]],
        None,
    ]

    Nnsi_G2dFontGetTextHeight: Symbol[
        Optional[list[int]],
        None,
    ]

    Nnsi_G2dFontGetTextWidth: Symbol[
        Optional[list[int]],
        None,
    ]

    GetCharIndex1D: Symbol[
        Optional[list[int]],
        None,
    ]

    ObjSizeToShape: Symbol[
        Optional[list[int]],
        None,
    ]

    ClearChar: Symbol[
        Optional[list[int]],
        None,
    ]

    LetterChar: Symbol[
        Optional[list[int]],
        None,
    ]

    DrawGlyphLine: Symbol[
        Optional[list[int]],
        None,
    ]

    DrawGlyph1D: Symbol[
        Optional[list[int]],
        None,
    ]

    ClearContinuous: Symbol[
        Optional[list[int]],
        None,
    ]

    ClearLine: Symbol[
        Optional[list[int]],
        None,
    ]

    ClearAreaLine: Symbol[
        Optional[list[int]],
        None,
    ]

    ClearArea1D: Symbol[
        Optional[list[int]],
        None,
    ]

    InitCharCanvas: Symbol[
        Optional[list[int]],
        None,
    ]

    Nns_G2dCharCanvasDrawChar: Symbol[
        Optional[list[int]],
        None,
    ]

    Nns_G2dCharCanvasInitForBG: Symbol[
        Optional[list[int]],
        None,
    ]

    Nns_G2dCharCanvasInitForObj1D: Symbol[
        Optional[list[int]],
        None,
    ]

    Nns_G2dMapScrToCharText: Symbol[
        Optional[list[int]],
        None,
    ]

    Nns_G2dMapScrToChar256x16Pltt: Symbol[
        Optional[list[int]],
        None,
    ]

    Nnsi_G2dCalcRequiredObj: Symbol[
        Optional[list[int]],
        None,
    ]

    Nns_G2dArrangeObj1D: Symbol[
        Optional[list[int]],
        None,
    ]

    Nnsi_G2dTextCanvasDrawString: Symbol[
        Optional[list[int]],
        None,
    ]

    Nnsi_G2dTextCanvasDrawTextAlign: Symbol[
        Optional[list[int]],
        None,
    ]

    Nnsi_G2dTextCanvasDrawText: Symbol[
        Optional[list[int]],
        None,
    ]

    Nnsi_G2dTextCanvasDrawTextRect: Symbol[
        Optional[list[int]],
        None,
    ]

    Nnsi_G2dGetUnpackedFont: Symbol[
        Optional[list[int]],
        None,
    ]

    Nnsi_G2dUnpackNft: Symbol[
        Optional[list[int]],
        None,
    ]

    Nnsi_G2dBitReaderRead: Symbol[
        Optional[list[int]],
        None,
    ]

    Nnsi_G2dSplitCharUtf16: Symbol[
        Optional[list[int]],
        None,
    ]

    Nns_SndInit: Symbol[
        Optional[list[int]],
        None,
    ]

    Nns_SndMain: Symbol[
        Optional[list[int]],
        None,
    ]

    BeginSleep: Symbol[
        Optional[list[int]],
        None,
    ]

    EndSleep: Symbol[
        Optional[list[int]],
        None,
    ]

    Nns_SndUnlockChannel: Symbol[
        Optional[list[int]],
        None,
    ]

    Nns_SndUnlockCapture: Symbol[
        Optional[list[int]],
        None,
    ]

    Nns_SndFreeAlarm: Symbol[
        Optional[list[int]],
        None,
    ]

    Nnsi_SndInitResourceMgr: Symbol[
        Optional[list[int]],
        None,
    ]

    Nns_SndPlayerSetPlayableSeqCount: Symbol[
        Optional[list[int]],
        None,
    ]

    Nns_SndPlayerSetAllocatableChannel: Symbol[
        Optional[list[int]],
        None,
    ]

    Nns_SndPlayerCreateHeap: Symbol[
        Optional[list[int]],
        None,
    ]

    Nns_SndPlayerStopSeq: Symbol[
        Optional[list[int]],
        None,
    ]

    Nns_SndHandleInit: Symbol[
        Optional[list[int]],
        None,
    ]

    Nns_SndHandleReleaseSeq: Symbol[
        Optional[list[int]],
        None,
    ]

    Nns_SndPlayerSetInitialVolume: Symbol[
        Optional[list[int]],
        None,
    ]

    Nns_SndPlayerSetChannelPriority: Symbol[
        Optional[list[int]],
        None,
    ]

    Nns_SndPlayerSetTrackPitch: Symbol[
        Optional[list[int]],
        None,
    ]

    Nns_SndPlayerSetSeqArcNo: Symbol[
        Optional[list[int]],
        None,
    ]

    Nnsi_SndPlayerInit: Symbol[
        Optional[list[int]],
        None,
    ]

    Nnsi_SndPlayerMain: Symbol[
        Optional[list[int]],
        None,
    ]

    Nnsi_SndPlayerAllocSeqPlayer: Symbol[
        Optional[list[int]],
        None,
    ]

    Nnsi_SndPlayerFreeSeqPlayer: Symbol[
        Optional[list[int]],
        None,
    ]

    Nnsi_SndPlayerStartSeq: Symbol[
        Optional[list[int]],
        None,
    ]

    Nnsi_SndPlayerStopSeq: Symbol[
        Optional[list[int]],
        None,
    ]

    Nnsi_SndPlayerAllocHeap: Symbol[
        Optional[list[int]],
        None,
    ]

    InitPlayer: Symbol[
        Optional[list[int]],
        None,
    ]

    InsertPlayerList: Symbol[
        Optional[list[int]],
        None,
    ]

    InsertPrioList: Symbol[
        Optional[list[int]],
        None,
    ]

    ForceStopSeq: Symbol[
        Optional[list[int]],
        None,
    ]

    AllocSeqPlayer: Symbol[
        Optional[list[int]],
        None,
    ]

    ShutdownPlayer: Symbol[
        Optional[list[int]],
        None,
    ]

    PlayerHeapDisposeCallback: Symbol[
        Optional[list[int]],
        None,
    ]

    SetPlayerPriority: Symbol[
        Optional[list[int]],
        None,
    ]

    Nns_SndStrmFreeChannel: Symbol[
        Optional[list[int]],
        None,
    ]

    Nns_SndStrmStart: Symbol[
        Optional[list[int]],
        None,
    ]

    Nns_SndStrmStop: Symbol[
        Optional[list[int]],
        None,
    ]

    Nns_SndStrmSetVolume: Symbol[
        Optional[list[int]],
        None,
    ]

    ForceStopStrm: Symbol[
        Optional[list[int]],
        None,
    ]

    ShutdownStrm: Symbol[
        Optional[list[int]],
        None,
    ]

    Nnsi_SndCaptureInit: Symbol[
        Optional[list[int]],
        None,
    ]

    Nnsi_SndCaptureMain: Symbol[
        Optional[list[int]],
        None,
    ]

    Nnsi_SndCaptureStop: Symbol[
        Optional[list[int]],
        None,
    ]

    Nnsi_SndCaptureBeginSleep: Symbol[
        Optional[list[int]],
        None,
    ]

    Nnsi_SndCaptureEndSleep: Symbol[
        Optional[list[int]],
        None,
    ]

    Nns_SndArcInitOnMemory: Symbol[
        Optional[list[int]],
        None,
    ]

    Nns_SndArcSetCurrent: Symbol[
        Optional[list[int]],
        None,
    ]

    Nns_SndArcGetCurrent: Symbol[
        Optional[list[int]],
        None,
    ]

    Nns_SndArcGetSeqArcInfo: Symbol[
        Optional[list[int]],
        None,
    ]

    Nns_SndArcGetBankInfo: Symbol[
        Optional[list[int]],
        None,
    ]

    Nns_SndArcGetWaveArcInfo: Symbol[
        Optional[list[int]],
        None,
    ]

    Nns_SndArcGetPlayerInfo: Symbol[
        Optional[list[int]],
        None,
    ]

    Nns_SndArcGetFileSize: Symbol[
        Optional[list[int]],
        None,
    ]

    Nns_SndArcReadFile: Symbol[
        Optional[list[int]],
        None,
    ]

    Nns_SndArcGetFileAddress: Symbol[
        Optional[list[int]],
        None,
    ]

    Nns_SndArcSetFileAddress: Symbol[
        Optional[list[int]],
        None,
    ]

    Nns_SndHeapCreate: Symbol[
        Optional[list[int]],
        None,
    ]

    Nns_SndHeapDestroy: Symbol[
        Optional[list[int]],
        None,
    ]

    Nns_SndHeapClear: Symbol[
        Optional[list[int]],
        None,
    ]

    Nns_SndHeapAlloc: Symbol[
        Optional[list[int]],
        None,
    ]

    InitHeapSection: Symbol[
        Optional[list[int]],
        None,
    ]

    InitHeap: Symbol[
        Optional[list[int]],
        None,
    ]

    NewSection: Symbol[
        Optional[list[int]],
        None,
    ]

    EraseSync: Symbol[
        Optional[list[int]],
        None,
    ]

    Nnsi_SndArcLoadBank: Symbol[
        Optional[list[int]],
        None,
    ]

    Nnsi_SndArcLoadWaveArc: Symbol[
        Optional[list[int]],
        None,
    ]

    Nnsi_SndArcLoadFile: Symbol[
        Optional[list[int]],
        None,
    ]

    LoadBank: Symbol[
        Optional[list[int]],
        None,
    ]

    LoadWaveArc: Symbol[
        Optional[list[int]],
        None,
    ]

    LoadWaveArcTable: Symbol[
        Optional[list[int]],
        None,
    ]

    DisposeCallback: Symbol[
        Optional[list[int]],
        None,
    ]

    BankDisposeCallback: Symbol[
        Optional[list[int]],
        None,
    ]

    WaveArcDisposeCallback: Symbol[
        Optional[list[int]],
        None,
    ]

    WaveArcTableDisposeCallback: Symbol[
        Optional[list[int]],
        None,
    ]

    SingleWaveDisposeCallback: Symbol[
        Optional[list[int]],
        None,
    ]

    LoadSingleWave: Symbol[
        Optional[list[int]],
        None,
    ]

    LoadSingleWaves: Symbol[
        Optional[list[int]],
        None,
    ]

    Nns_SndArcPlayerSetup: Symbol[
        Optional[list[int]],
        None,
    ]

    Nns_SndArcPlayerStartSeqArc: Symbol[
        Optional[list[int]],
        None,
    ]

    StartSeqArc: Symbol[
        Optional[list[int]],
        None,
    ]

    Nnsi_SndArcStrmMain: Symbol[
        Optional[list[int]],
        None,
    ]

    FreePlayer: Symbol[
        Optional[list[int]],
        None,
    ]

    ForceStopStrm_Arc: Symbol[
        Optional[list[int]],
        None,
    ]

    FreeChannel: Symbol[
        Optional[list[int]],
        None,
    ]

    RemoveCommandByPlayer: Symbol[
        Optional[list[int]],
        None,
    ]

    FreeCommandBuffer: Symbol[
        Optional[list[int]],
        None,
    ]

    Nnsi_SndSeqArcGetSeqInfo: Symbol[
        Optional[list[int]],
        None,
    ]

    Nnsi_SndFaderInit: Symbol[
        Optional[list[int]],
        None,
    ]

    Nnsi_SndFaderSet: Symbol[
        Optional[list[int]],
        None,
    ]

    Nnsi_SndFaderGet: Symbol[
        Optional[list[int]],
        None,
    ]

    Nnsi_SndFaderUpdate: Symbol[
        Optional[list[int]],
        None,
    ]

    Nnsi_SndFaderIsFinished: Symbol[
        Optional[list[int]],
        None,
    ]

    Aoss_Malloc: Symbol[
        Optional[list[int]],
        None,
    ]

    Aoss_Free: Symbol[
        Optional[list[int]],
        None,
    ]

    Aossi_Init: Symbol[
        Optional[list[int]],
        None,
    ]

    Aoss_Init_Old: Symbol[
        Optional[list[int]],
        None,
    ]

    aoss_ip_sta: Symbol[
        Optional[list[int]],
        None,
    ]

    aoss_release: Symbol[
        Optional[list[int]],
        None,
    ]

    aoss_data_init: Symbol[
        Optional[list[int]],
        None,
    ]

    aoss_set_error: Symbol[
        Optional[list[int]],
        None,
    ]

    aoss_get_error: Symbol[
        Optional[list[int]],
        None,
    ]

    aoss_seq_data_copy: Symbol[
        Optional[list[int]],
        None,
    ]

    aoss_check_str: Symbol[
        Optional[list[int]],
        None,
    ]

    CheckAP_Aoss: Symbol[
        Optional[list[int]],
        None,
    ]

    Aoss_Set_ApInfo: Symbol[
        Optional[list[int]],
        None,
    ]

    MakeSendSeqID: Symbol[
        Optional[list[int]],
        None,
    ]

    Aoss_StatusExclusion: Symbol[
        Optional[list[int]],
        None,
    ]

    RecvMessage: Symbol[
        Optional[list[int]],
        None,
    ]

    AstsSetInitRes: Symbol[
        Optional[list[int]],
        None,
    ]

    AstsSetSecureRes: Symbol[
        Optional[list[int]],
        None,
    ]

    AstsRestartRes: Symbol[
        Optional[list[int]],
        None,
    ]

    DecodePacket: Symbol[
        Optional[list[int]],
        None,
    ]

    CheckSeqID: Symbol[
        Optional[list[int]],
        None,
    ]

    CheckRecvSeqID: Symbol[
        Optional[list[int]],
        None,
    ]

    GetProductInfo: Symbol[
        Optional[list[int]],
        None,
    ]

    aoss_get_bin: Symbol[
        Optional[list[int]],
        None,
    ]

    GetWepData: Symbol[
        Optional[list[int]],
        None,
    ]

    GetWpaData: Symbol[
        Optional[list[int]],
        None,
    ]

    GetBssidData: Symbol[
        Optional[list[int]],
        None,
    ]

    GetSecurityData: Symbol[
        Optional[list[int]],
        None,
    ]

    GetSecurityType: Symbol[
        Optional[list[int]],
        None,
    ]

    SendMessage: Symbol[
        Optional[list[int]],
        None,
    ]

    AstsSetInitReq: Symbol[
        Optional[list[int]],
        None,
    ]

    AstsSetSecureReq: Symbol[
        Optional[list[int]],
        None,
    ]

    AstsRestartReq: Symbol[
        Optional[list[int]],
        None,
    ]

    SetStaData: Symbol[
        Optional[list[int]],
        None,
    ]

    PacketDataSet: Symbol[
        Optional[list[int]],
        None,
    ]

    SetPacketHeader: Symbol[
        Optional[list[int]],
        None,
    ]

    SendPacketUdp: Symbol[
        Optional[list[int]],
        None,
    ]

    EncodeRC4: Symbol[
        Optional[list[int]],
        None,
    ]

    DecodeRC4: Symbol[
        Optional[list[int]],
        None,
    ]

    RC4init: Symbol[
        Optional[list[int]],
        None,
    ]

    RC4encrypt: Symbol[
        Optional[list[int]],
        None,
    ]

    arcfour_byte: Symbol[
        Optional[list[int]],
        None,
    ]

    crc: Symbol[
        Optional[list[int]],
        None,
    ]

    update_crc: Symbol[
        Optional[list[int]],
        None,
    ]

    make_crc_table: Symbol[
        Optional[list[int]],
        None,
    ]

    CryptSeqNo: Symbol[
        Optional[list[int]],
        None,
    ]

    MakeKey: Symbol[
        Optional[list[int]],
        None,
    ]

    AddKey: Symbol[
        Optional[list[int]],
        None,
    ]

    Rotate: Symbol[
        Optional[list[int]],
        None,
    ]

    Aoss_SetIpAddr: Symbol[
        Optional[list[int]],
        None,
    ]

    Aoss_Disconnect: Symbol[
        Optional[list[int]],
        None,
    ]

    Aoss_Memcmp: Symbol[
        Optional[list[int]],
        None,
    ]

    Aoss_Memcpy: Symbol[
        Optional[list[int]],
        None,
    ]

    Aoss_Memset: Symbol[
        Optional[list[int]],
        None,
    ]

    Aoss_Recvfrom: Symbol[
        Optional[list[int]],
        None,
    ]

    Aoss_Select: Symbol[
        Optional[list[int]],
        None,
    ]

    Aoss_Sendto: Symbol[
        Optional[list[int]],
        None,
    ]

    Aoss_Setsockopt: Symbol[
        Optional[list[int]],
        None,
    ]

    Aoss_Socket: Symbol[
        Optional[list[int]],
        None,
    ]

    Aoss_Bind: Symbol[
        Optional[list[int]],
        None,
    ]

    Aoss_Close: Symbol[
        Optional[list[int]],
        None,
    ]

    Aoss_Htonl: Symbol[
        Optional[list[int]],
        None,
    ]

    Aoss_Htons: Symbol[
        Optional[list[int]],
        None,
    ]

    Aoss_Ntohl: Symbol[
        Optional[list[int]],
        None,
    ]

    Aoss_Ntohs: Symbol[
        Optional[list[int]],
        None,
    ]

    Aoss_Strlen: Symbol[
        Optional[list[int]],
        None,
    ]

    Aoss_Rand: Symbol[
        Optional[list[int]],
        None,
    ]

    Aoss_FD_Zero: Symbol[
        Optional[list[int]],
        None,
    ]

    Aoss_FD_Set: Symbol[
        Optional[list[int]],
        None,
    ]

    Set_Wlla_Bss_Info: Symbol[
        Optional[list[int]],
        None,
    ]

    Get_Wlla_Ssid_Param: Symbol[
        Optional[list[int]],
        None,
    ]

    Set_Wlla_Link_Stat: Symbol[
        Optional[list[int]],
        None,
    ]

    aoss_apc_callback: Symbol[
        Optional[list[int]],
        None,
    ]

    AlarmCallback: Symbol[
        Optional[list[int]],
        None,
    ]

    Aossi_InitLocal: Symbol[
        Optional[list[int]],
        None,
    ]

    Aossi_EndLocal: Symbol[
        Optional[list[int]],
        None,
    ]

    Aossi_Disconnect: Symbol[
        Optional[list[int]],
        None,
    ]

    Aossi_WlanGetBssList: Symbol[
        Optional[list[int]],
        None,
    ]

    Aossi_WlanConnect: Symbol[
        Optional[list[int]],
        None,
    ]

    Aossi_Sleep: Symbol[
        Optional[list[int]],
        None,
    ]

    Aossi_Status: Symbol[
        Optional[list[int]],
        None,
    ]

    Apci_Notify: Symbol[
        Optional[list[int]],
        None,
    ]

    Apci_MoveIdleState: Symbol[
        Optional[list[int]],
        None,
    ]

    Apc_GetApList: Symbol[
        Optional[list[int]],
        None,
    ]

    Apc_SearchStart: Symbol[
        Optional[list[int]],
        None,
    ]

    Apc_SearchEnd: Symbol[
        Optional[list[int]],
        None,
    ]

    Apc_Disconnect: Symbol[
        Optional[list[int]],
        None,
    ]

    Apc_End: Symbol[
        Optional[list[int]],
        None,
    ]

    Apc_Connect: Symbol[
        Optional[list[int]],
        None,
    ]

    Apc_Init: Symbol[
        Optional[list[int]],
        None,
    ]

    Apc_GetState: Symbol[
        Optional[list[int]],
        None,
    ]

    SoAlloc: Symbol[
        Optional[list[int]],
        None,
    ]

    SoFree: Symbol[
        Optional[list[int]],
        None,
    ]

    AtermApc_InitEventBuf: Symbol[
        Optional[list[int]],
        None,
    ]

    AtermApc_GetEvent: Symbol[
        Optional[list[int]],
        None,
    ]

    AtermApc_Callback: Symbol[
        Optional[list[int]],
        None,
    ]

    InitAtermApcNetwork: Symbol[
        Optional[list[int]],
        None,
    ]

    FreeAtermApcNetwork: Symbol[
        Optional[list[int]],
        None,
    ]

    ConnectAP: Symbol[
        Optional[list[int]],
        None,
    ]

    DisconnectAP: Symbol[
        Optional[list[int]],
        None,
    ]

    CheckAccessPoint: Symbol[
        Optional[list[int]],
        None,
    ]

    ScanAP: Symbol[
        Optional[list[int]],
        None,
    ]

    SendFrameViaInterface: Symbol[
        Optional[list[int]],
        None,
    ]

    SendBroadcast: Symbol[
        Optional[list[int]],
        None,
    ]

    SendFrame: Symbol[
        Optional[list[int]],
        None,
    ]

    GetFrameData: Symbol[
        Optional[list[int]],
        None,
    ]

    GetElementData: Symbol[
        Optional[list[int]],
        None,
    ]

    GetFirstElement: Symbol[
        Optional[list[int]],
        None,
    ]

    SetFrameData: Symbol[
        Optional[list[int]],
        None,
    ]

    SetElementData: Symbol[
        Optional[list[int]],
        None,
    ]

    SetSingleElement: Symbol[
        Optional[list[int]],
        None,
    ]

    IsSearchCommand: Symbol[
        Optional[list[int]],
        None,
    ]

    GetCommandElement: Symbol[
        Optional[list[int]],
        None,
    ]

    SetSearchRes: Symbol[
        Optional[list[int]],
        None,
    ]

    GetAdapterMac: Symbol[
        Optional[list[int]],
        None,
    ]

    GetMacEncKey: Symbol[
        Optional[list[int]],
        None,
    ]

    GetWLanSetElement: Symbol[
        Optional[list[int]],
        None,
    ]

    AsciiToHex: Symbol[
        Optional[list[int]],
        None,
    ]

    StoreNetParam: Symbol[
        Optional[list[int]],
        None,
    ]

    AutoConfigThreadEx: Symbol[
        Optional[list[int]],
        None,
    ]

    AutoConfigThread: Symbol[
        Optional[list[int]],
        None,
    ]

    keywrap_encrypt: Symbol[
        Optional[list[int]],
        None,
    ]

    keywrap_decrypt: Symbol[
        Optional[list[int]],
        None,
    ]

    aeskw_xor64: Symbol[
        Optional[list[int]],
        None,
    ]

    RijndaelKeySetupEnc: Symbol[
        Optional[list[int]],
        None,
    ]

    RijndaelKeySetupDec: Symbol[
        Optional[list[int]],
        None,
    ]

    RijndaelEncrypt: Symbol[
        Optional[list[int]],
        None,
    ]

    RijndaelDecrypt: Symbol[
        Optional[list[int]],
        None,
    ]

    MY_MD5Init: Symbol[
        Optional[list[int]],
        None,
    ]

    MY_MD5Update: Symbol[
        Optional[list[int]],
        None,
    ]

    MY_MD5Final: Symbol[
        Optional[list[int]],
        None,
    ]

    MD5Transform: Symbol[
        Optional[list[int]],
        None,
    ]

    Encode: Symbol[
        Optional[list[int]],
        None,
    ]

    Decode: Symbol[
        Optional[list[int]],
        None,
    ]

    MD5_Memcpy: Symbol[
        Optional[list[int]],
        None,
    ]

    MD5_Memset: Symbol[
        Optional[list[int]],
        None,
    ]

    MD5Encode: Symbol[
        Optional[list[int]],
        None,
    ]

    GetTickCount: Symbol[
        Optional[list[int]],
        None,
    ]

    Calloc: Symbol[
        Optional[list[int]],
        None,
    ]

    Free: Symbol[
        Optional[list[int]],
        None,
    ]

    PutHex: Symbol[
        Optional[list[int]],
        None,
    ]

    PutMac: Symbol[
        Optional[list[int]],
        None,
    ]

    Atermi_ApConfigStart: Symbol[
        Optional[list[int]],
        None,
    ]

    Atermi_ApConfigEnd: Symbol[
        Optional[list[int]],
        None,
    ]

    Atermi_ApConfigGetState: Symbol[
        Optional[list[int]],
        None,
    ]

    Atermi_ApConfigGetResult: Symbol[
        Optional[list[int]],
        None,
    ]

    SendNotify: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_AnimelInitEx: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_AnimelEnd: Symbol[
        Optional[list[int]],
        None,
    ]

    TaskAnime: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_BtnlInit: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_BtnlEnd: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_BtnlGet: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_BtnlSet: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_BtnlSetForce: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_BtnlIsEnd: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_BtnlEnable: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_BtnlDisable: Symbol[
        Optional[list[int]],
        None,
    ]

    Button_Disp: Symbol[
        Optional[list[int]],
        None,
    ]

    Button_TaskStart: Symbol[
        Optional[list[int]],
        None,
    ]

    Button_TaskStart1: Symbol[
        Optional[list[int]],
        None,
    ]

    Button_TaskMain: Symbol[
        Optional[list[int]],
        None,
    ]

    Button_TaskEnd: Symbol[
        Optional[list[int]],
        None,
    ]

    Button_TaskEnd1: Symbol[
        Optional[list[int]],
        None,
    ]

    Button_TaskRelease: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_CommentlInit: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_CommentlDispEx: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_CommentlDelete: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_Char: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_CmnlLoadResource: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_CmnlStep: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_CmnlButton: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_CmnlMsgDraw: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_CmnlMsgNameDraw: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_CmnlFontFlag: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_FocuslInit: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_FocuslEnd: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_FocuslDisp: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_FocuslDisp4: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_FocuslDelete: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_HLlInit: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_HLlEnd: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_HLlLoad: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_HLlLoadSet: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_HLlLoadList: Symbol[
        Optional[list[int]],
        None,
    ]

    Headline_TaskLoad: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_IconlInit: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_IconlEnd: Symbol[
        Optional[list[int]],
        None,
    ]

    Icon_TaskRenew: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_KBlInit: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_KBlEnd: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_KBlGet: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_KBlSetErase: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_KBlSetInput: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_KBlIsInit: Symbol[
        Optional[list[int]],
        None,
    ]

    Keyboard_TaskStart0: Symbol[
        Optional[list[int]],
        None,
    ]

    Keyboard_TaskStart1: Symbol[
        Optional[list[int]],
        None,
    ]

    Keyboard_TaskStart2: Symbol[
        Optional[list[int]],
        None,
    ]

    Keyboard_TaskStart3: Symbol[
        Optional[list[int]],
        None,
    ]

    Keyboard_TaskStart4: Symbol[
        Optional[list[int]],
        None,
    ]

    Keyboard_TaskMain: Symbol[
        Optional[list[int]],
        None,
    ]

    Keyboard_TouchTriger: Symbol[
        Optional[list[int]],
        None,
    ]

    Keyboard_TouchRelease: Symbol[
        Optional[list[int]],
        None,
    ]

    Keyboard_PushCaps: Symbol[
        Optional[list[int]],
        None,
    ]

    Keyboard_PushShift: Symbol[
        Optional[list[int]],
        None,
    ]

    Keyboard_Touch: Symbol[
        Optional[list[int]],
        None,
    ]

    Keyboard_ExchangeBack: Symbol[
        Optional[list[int]],
        None,
    ]

    Keyboard_Key: Symbol[
        Optional[list[int]],
        None,
    ]

    Keyboard_Disp: Symbol[
        Optional[list[int]],
        None,
    ]

    Keyboard_ChangePage: Symbol[
        Optional[list[int]],
        None,
    ]

    Keyboard_ChangeColor: Symbol[
        Optional[list[int]],
        None,
    ]

    Keyboard_DispFocus: Symbol[
        Optional[list[int]],
        None,
    ]

    Keyboard_MoveFocus: Symbol[
        Optional[list[int]],
        None,
    ]

    Keyboard_TaskEnd0: Symbol[
        Optional[list[int]],
        None,
    ]

    Keyboard_TaskEnd1: Symbol[
        Optional[list[int]],
        None,
    ]

    Keyboard_TaskEnd2: Symbol[
        Optional[list[int]],
        None,
    ]

    Keyboard_TaskEnd3: Symbol[
        Optional[list[int]],
        None,
    ]

    Keyboard_TaskEnd4: Symbol[
        Optional[list[int]],
        None,
    ]

    Keyboard_TaskEnd5: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_KB10lInit: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_KB10lEnd: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_KB10lGet: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_KB10lSetErase: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_KB10lSetInput: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_KB10lSetShift: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_KB10lIsInit: Symbol[
        Optional[list[int]],
        None,
    ]

    Keyboard10_TaskStart0: Symbol[
        Optional[list[int]],
        None,
    ]

    Keyboard10_TaskStart1: Symbol[
        Optional[list[int]],
        None,
    ]

    Keyboard10_TaskStart2: Symbol[
        Optional[list[int]],
        None,
    ]

    Keyboard10_TaskStart3: Symbol[
        Optional[list[int]],
        None,
    ]

    Keyboard10_TaskStart4: Symbol[
        Optional[list[int]],
        None,
    ]

    Keyboard10_TaskMain: Symbol[
        Optional[list[int]],
        None,
    ]

    Keyboard10_TouchTriger: Symbol[
        Optional[list[int]],
        None,
    ]

    Keyboard10_TouchRelease: Symbol[
        Optional[list[int]],
        None,
    ]

    Keyboard10_Touch: Symbol[
        Optional[list[int]],
        None,
    ]

    Keyboard10_ExchangeBack: Symbol[
        Optional[list[int]],
        None,
    ]

    Keyboard10_Key: Symbol[
        Optional[list[int]],
        None,
    ]

    Keyboard10_Disp: Symbol[
        Optional[list[int]],
        None,
    ]

    Keyboard10_ChangeColor: Symbol[
        Optional[list[int]],
        None,
    ]

    Keyboard10_DispFocus: Symbol[
        Optional[list[int]],
        None,
    ]

    Keyboard10_MoveFocus: Symbol[
        Optional[list[int]],
        None,
    ]

    Keyboard10_TaskEnd0: Symbol[
        Optional[list[int]],
        None,
    ]

    Keyboard10_TaskEnd1: Symbol[
        Optional[list[int]],
        None,
    ]

    Keyboard10_TaskEnd2: Symbol[
        Optional[list[int]],
        None,
    ]

    Keyboard10_TaskEnd3: Symbol[
        Optional[list[int]],
        None,
    ]

    Keyboard10_TaskEnd4: Symbol[
        Optional[list[int]],
        None,
    ]

    Keyboard10_TaskEnd5: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_AosslInit: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_AosslEnd: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_AosslStart: Symbol[
        Optional[list[int]],
        None,
    ]

    AossAlloc: Symbol[
        Optional[list[int]],
        None,
    ]

    AossFree: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwc_StartUtility: Symbol[
        Optional[list[int]],
        None,
    ]

    Main_CheckParam: Symbol[
        Optional[list[int]],
        None,
    ]

    Main_InitGame: Symbol[
        Optional[list[int]],
        None,
    ]

    Main_InitGraph: Symbol[
        Optional[list[int]],
        None,
    ]

    Main_ProcEnd: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_ChangeScene: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_SetParam: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_GetParam: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_SetParam2: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_GetParam2: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_Language: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_Entry: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_Flag: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_EndUtility: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_MsglInit: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_MsglEnd: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_MsglRead: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_MsglRelease: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_MsglGet: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_MsglGetEx: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_MovlInit: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_MovlEnd: Symbol[
        Optional[list[int]],
        None,
    ]

    Move_TaskEnd: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_MovlIsEnd: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_MovlChangeCallback: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_MovlAdmitChild: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_MovlGetChild: Symbol[
        Optional[list[int]],
        None,
    ]

    Move_TaskFramework: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_RakulInit: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_RakulEnd: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_RakulGetState: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_RakulSetResult: Symbol[
        Optional[list[int]],
        None,
    ]

    RakuRaku_MemAlloc: Symbol[
        Optional[list[int]],
        None,
    ]

    RakuRaku_MemFree: Symbol[
        Optional[list[int]],
        None,
    ]

    RakuRaku_CbConfig: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_SceneEnd: Symbol[
        Optional[list[int]],
        None,
    ]

    SceneEnd_EndScene: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_SceneInit: Symbol[
        Optional[list[int]],
        None,
    ]

    SceneInit_ProcFade: Symbol[
        Optional[list[int]],
        None,
    ]

    SceneInit_ProcWait: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_SceneMenu: Symbol[
        Optional[list[int]],
        None,
    ]

    SceneMenu_InitGraphics: Symbol[
        Optional[list[int]],
        None,
    ]

    SceneMenu_ProcInit: Symbol[
        Optional[list[int]],
        None,
    ]

    SceneMenu_ProcInit1: Symbol[
        Optional[list[int]],
        None,
    ]

    SceneMenu_ProcInit2: Symbol[
        Optional[list[int]],
        None,
    ]

    SceneMenu_ProcScene: Symbol[
        Optional[list[int]],
        None,
    ]

    SceneMenu_Input: Symbol[
        Optional[list[int]],
        None,
    ]

    SceneMenu_Draw: Symbol[
        Optional[list[int]],
        None,
    ]

    SceneMenu_Button: Symbol[
        Optional[list[int]],
        None,
    ]

    SceneMenu_EndScene: Symbol[
        Optional[list[int]],
        None,
    ]

    SceneMenu_EndScene1: Symbol[
        Optional[list[int]],
        None,
    ]

    SceneMenu_EndScene2: Symbol[
        Optional[list[int]],
        None,
    ]

    SceneMenu_MoveFocus: Symbol[
        Optional[list[int]],
        None,
    ]

    SceneMenu_DispPushButton: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_SceneOptErase: Symbol[
        Optional[list[int]],
        None,
    ]

    SceneOptErase_InitGraphics: Symbol[
        Optional[list[int]],
        None,
    ]

    SceneOptErase_ProcInit: Symbol[
        Optional[list[int]],
        None,
    ]

    SceneOptErase_ProcInit1: Symbol[
        Optional[list[int]],
        None,
    ]

    SceneOptErase_ProcInit2: Symbol[
        Optional[list[int]],
        None,
    ]

    SceneOptErase_ProcScene: Symbol[
        Optional[list[int]],
        None,
    ]

    SceneOptErase_Input: Symbol[
        Optional[list[int]],
        None,
    ]

    SceneOptErase_Draw: Symbol[
        Optional[list[int]],
        None,
    ]

    SceneOptErase_Button: Symbol[
        Optional[list[int]],
        None,
    ]

    SceneOptErase_EndScene: Symbol[
        Optional[list[int]],
        None,
    ]

    SceneOptErase_EndScene1: Symbol[
        Optional[list[int]],
        None,
    ]

    SceneOptErase_EndScene2: Symbol[
        Optional[list[int]],
        None,
    ]

    SceneOptErase_ProcConfirm: Symbol[
        Optional[list[int]],
        None,
    ]

    SceneOptErase_ProcConfirm1: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_SceneOptErase1: Symbol[
        Optional[list[int]],
        None,
    ]

    SceneOptErase1_InitGraphics: Symbol[
        Optional[list[int]],
        None,
    ]

    SceneOptErase1_ProcInit: Symbol[
        Optional[list[int]],
        None,
    ]

    SceneOptErase1_ProcInit1: Symbol[
        Optional[list[int]],
        None,
    ]

    SceneOptErase1_ProcInit2: Symbol[
        Optional[list[int]],
        None,
    ]

    SceneOptErase1_ProcScene: Symbol[
        Optional[list[int]],
        None,
    ]

    SceneOptErase1_Input: Symbol[
        Optional[list[int]],
        None,
    ]

    SceneOptErase1_Draw: Symbol[
        Optional[list[int]],
        None,
    ]

    SceneOptErase1_Button: Symbol[
        Optional[list[int]],
        None,
    ]

    SceneOptErase1_EndScene: Symbol[
        Optional[list[int]],
        None,
    ]

    SceneOptErase1_EndScene1: Symbol[
        Optional[list[int]],
        None,
    ]

    SceneOptErase1_EndScene2: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_SceneOptInfo: Symbol[
        Optional[list[int]],
        None,
    ]

    SceneOptInfo_InitGraphics: Symbol[
        Optional[list[int]],
        None,
    ]

    SceneOptInfo_DrawInfo: Symbol[
        Optional[list[int]],
        None,
    ]

    SceneOptInfo_ProcInit: Symbol[
        Optional[list[int]],
        None,
    ]

    SceneOptInfo_ProcInit1: Symbol[
        Optional[list[int]],
        None,
    ]

    SceneOptInfo_ProcInit2: Symbol[
        Optional[list[int]],
        None,
    ]

    SceneOptInfo_ProcScene: Symbol[
        Optional[list[int]],
        None,
    ]

    SceneOptInfo_Input: Symbol[
        Optional[list[int]],
        None,
    ]

    SceneOptInfo_Draw: Symbol[
        Optional[list[int]],
        None,
    ]

    SceneOptInfo_Button: Symbol[
        Optional[list[int]],
        None,
    ]

    SceneOptInfo_EndScene: Symbol[
        Optional[list[int]],
        None,
    ]

    SceneOptInfo_EndScene1: Symbol[
        Optional[list[int]],
        None,
    ]

    SceneOptInfo_EndScene2: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_SceneOptMenu: Symbol[
        Optional[list[int]],
        None,
    ]

    SceneOptMenu_InitGraphics: Symbol[
        Optional[list[int]],
        None,
    ]

    SceneOptMenu_ProcInit: Symbol[
        Optional[list[int]],
        None,
    ]

    SceneOptMenu_ProcInit1: Symbol[
        Optional[list[int]],
        None,
    ]

    SceneOptMenu_ProcInit2: Symbol[
        Optional[list[int]],
        None,
    ]

    SceneOptMenu_ProcScene: Symbol[
        Optional[list[int]],
        None,
    ]

    SceneOptMenu_Input: Symbol[
        Optional[list[int]],
        None,
    ]

    SceneOptMenu_Draw: Symbol[
        Optional[list[int]],
        None,
    ]

    SceneOptMenu_Button: Symbol[
        Optional[list[int]],
        None,
    ]

    SceneOptMenu_EndScene: Symbol[
        Optional[list[int]],
        None,
    ]

    SceneOptMenu_EndScene1: Symbol[
        Optional[list[int]],
        None,
    ]

    SceneOptMenu_EndScene2: Symbol[
        Optional[list[int]],
        None,
    ]

    SceneOptMenu_MoveFocus: Symbol[
        Optional[list[int]],
        None,
    ]

    SceneOptMenu_DispPush: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_SceneOptMovComm: Symbol[
        Optional[list[int]],
        None,
    ]

    SceneOptMovComm_InitGraphics: Symbol[
        Optional[list[int]],
        None,
    ]

    SceneOptMovComm_ProcInit: Symbol[
        Optional[list[int]],
        None,
    ]

    SceneOptMovComm_ProcInit1: Symbol[
        Optional[list[int]],
        None,
    ]

    SceneOptMovComm_ProcScene: Symbol[
        Optional[list[int]],
        None,
    ]

    SceneOptMovComm_Input: Symbol[
        Optional[list[int]],
        None,
    ]

    SceneOptMovComm_Draw: Symbol[
        Optional[list[int]],
        None,
    ]

    SceneOptMovComm_EndScene: Symbol[
        Optional[list[int]],
        None,
    ]

    SceneOptMovComm_EndScene1: Symbol[
        Optional[list[int]],
        None,
    ]

    SceneOptMoveComm_CbMov: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_SceneOptMovComplete: Symbol[
        Optional[list[int]],
        None,
    ]

    SceneOptMovComplete_InitGraphics: Symbol[
        Optional[list[int]],
        None,
    ]

    SceneOptMovComplete_ProcInit: Symbol[
        Optional[list[int]],
        None,
    ]

    SceneOptMovComplete_ProcInit1: Symbol[
        Optional[list[int]],
        None,
    ]

    SceneOptMovComplete_ProcInit2: Symbol[
        Optional[list[int]],
        None,
    ]

    SceneOptMovComplete_ProcScene: Symbol[
        Optional[list[int]],
        None,
    ]

    SceneOptMovComplete_Input: Symbol[
        Optional[list[int]],
        None,
    ]

    SceneOptMovComplete_Draw: Symbol[
        Optional[list[int]],
        None,
    ]

    SceneOptMovComplete_Button: Symbol[
        Optional[list[int]],
        None,
    ]

    SceneOptMovComplete_EndScene: Symbol[
        Optional[list[int]],
        None,
    ]

    SceneOptMovComplete_EndScene1: Symbol[
        Optional[list[int]],
        None,
    ]

    SceneOptMovComplete_EndScene2: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_SceneOptMovConfirm: Symbol[
        Optional[list[int]],
        None,
    ]

    SceneOptMovConfirm_InitGraphics: Symbol[
        Optional[list[int]],
        None,
    ]

    SceneOptMovConfirm_ProcInit: Symbol[
        Optional[list[int]],
        None,
    ]

    SceneOptMovConfirm_ProcInit1: Symbol[
        Optional[list[int]],
        None,
    ]

    SceneOptMovConfirm_ProcInit2: Symbol[
        Optional[list[int]],
        None,
    ]

    SceneOptMovConfirm_ProcScene: Symbol[
        Optional[list[int]],
        None,
    ]

    SceneOptMovConfirm_Input: Symbol[
        Optional[list[int]],
        None,
    ]

    SceneOptMovConfirm_Draw: Symbol[
        Optional[list[int]],
        None,
    ]

    SceneOptMovConfirm_Button: Symbol[
        Optional[list[int]],
        None,
    ]

    SceneOptMovConfirm_EndScene: Symbol[
        Optional[list[int]],
        None,
    ]

    SceneOptMovConfirm_EndScene1: Symbol[
        Optional[list[int]],
        None,
    ]

    SceneOptMovConfirm_EndScene2: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_SceneOptMovConfirm1: Symbol[
        Optional[list[int]],
        None,
    ]

    SceneOptMovConfirm1_InitGraphics: Symbol[
        Optional[list[int]],
        None,
    ]

    SceneOptMovConfirm1_ProcInit: Symbol[
        Optional[list[int]],
        None,
    ]

    SceneOptMovConfirm1_ProcInit1: Symbol[
        Optional[list[int]],
        None,
    ]

    SceneOptMovConfirm1_ProcInit2: Symbol[
        Optional[list[int]],
        None,
    ]

    SceneOptMovConfirm1_ProcScene: Symbol[
        Optional[list[int]],
        None,
    ]

    SceneOptMovConfirm1_Input: Symbol[
        Optional[list[int]],
        None,
    ]

    SceneOptMovConfirm1_Draw: Symbol[
        Optional[list[int]],
        None,
    ]

    SceneOptMovConfirm1_Button: Symbol[
        Optional[list[int]],
        None,
    ]

    SceneOptMovConfirm1_EndScene: Symbol[
        Optional[list[int]],
        None,
    ]

    SceneOptMovConfirm1_EndScene1: Symbol[
        Optional[list[int]],
        None,
    ]

    SceneOptMovConfirm1_EndScene2: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_SceneOptMovDisconnect: Symbol[
        Optional[list[int]],
        None,
    ]

    SceneOptMovDisconnect_InitGraphics: Symbol[
        Optional[list[int]],
        None,
    ]

    SceneOptMovDisconnect_ProcInit: Symbol[
        Optional[list[int]],
        None,
    ]

    SceneOptMovDisconnect_ProcInit1: Symbol[
        Optional[list[int]],
        None,
    ]

    SceneOptMovDisconnect_ProcScene: Symbol[
        Optional[list[int]],
        None,
    ]

    SceneOptMovDisconnect_Draw: Symbol[
        Optional[list[int]],
        None,
    ]

    SceneOptMovDisconnect_EndScene: Symbol[
        Optional[list[int]],
        None,
    ]

    SceneOptMovDisconnect_EndScene1: Symbol[
        Optional[list[int]],
        None,
    ]

    SceneOptMovDisconnect_Wait: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_SceneOptMovFailure: Symbol[
        Optional[list[int]],
        None,
    ]

    SceneOptMovFailure_InitGraphics: Symbol[
        Optional[list[int]],
        None,
    ]

    SceneOptMovFailure_ProcInit: Symbol[
        Optional[list[int]],
        None,
    ]

    SceneOptMovFailure_ProcInit1: Symbol[
        Optional[list[int]],
        None,
    ]

    SceneOptMovFailure_ProcInit2: Symbol[
        Optional[list[int]],
        None,
    ]

    SceneOptMovFailure_ProcScene: Symbol[
        Optional[list[int]],
        None,
    ]

    SceneOptMovFailure_Input: Symbol[
        Optional[list[int]],
        None,
    ]

    SceneOptMovFailure_Draw: Symbol[
        Optional[list[int]],
        None,
    ]

    SceneOptMovFailure_Button: Symbol[
        Optional[list[int]],
        None,
    ]

    SceneOptMovFailure_EndScene: Symbol[
        Optional[list[int]],
        None,
    ]

    SceneOptMovFailure_EndScene1: Symbol[
        Optional[list[int]],
        None,
    ]

    SceneOptMovFailure_EndScene2: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_SceneOptMovUser: Symbol[
        Optional[list[int]],
        None,
    ]

    SceneOptMovUser_InitGraphics: Symbol[
        Optional[list[int]],
        None,
    ]

    SceneOptMovUser_ProcInit: Symbol[
        Optional[list[int]],
        None,
    ]

    SceneOptMovUser_ProcInit1: Symbol[
        Optional[list[int]],
        None,
    ]

    SceneOptMovUser_ProcInit2: Symbol[
        Optional[list[int]],
        None,
    ]

    SceneOptMovUser_ProcScene: Symbol[
        Optional[list[int]],
        None,
    ]

    SceneOptMovUser_Input: Symbol[
        Optional[list[int]],
        None,
    ]

    SceneOptMovUser_Draw: Symbol[
        Optional[list[int]],
        None,
    ]

    SceneOptMovUser_EndScene: Symbol[
        Optional[list[int]],
        None,
    ]

    SceneOptMovUser_EndScene1: Symbol[
        Optional[list[int]],
        None,
    ]

    SceneOptMovUser_EndScene2: Symbol[
        Optional[list[int]],
        None,
    ]

    SceneOptMovUser_CbMov: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_IsFold: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_SceneOptMovWait: Symbol[
        Optional[list[int]],
        None,
    ]

    SceneOptMovWait_InitGraphics: Symbol[
        Optional[list[int]],
        None,
    ]

    SceneOptMovWait_ProcInit: Symbol[
        Optional[list[int]],
        None,
    ]

    SceneOptMovWait_ProcInit1: Symbol[
        Optional[list[int]],
        None,
    ]

    SceneOptMovWait_ProcInit2: Symbol[
        Optional[list[int]],
        None,
    ]

    SceneOptMovWait_ProcScene: Symbol[
        Optional[list[int]],
        None,
    ]

    SceneOptMovWait_Input: Symbol[
        Optional[list[int]],
        None,
    ]

    SceneOptMovWait_Draw: Symbol[
        Optional[list[int]],
        None,
    ]

    SceneOptMovWait_Button: Symbol[
        Optional[list[int]],
        None,
    ]

    SceneOptMovWait_EndScene: Symbol[
        Optional[list[int]],
        None,
    ]

    SceneOptMovWait_EndScene1: Symbol[
        Optional[list[int]],
        None,
    ]

    SceneOptMovWait_EndScene2: Symbol[
        Optional[list[int]],
        None,
    ]

    SceneOptMovWait_CbMov: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_SceneSetAossButton: Symbol[
        Optional[list[int]],
        None,
    ]

    SceneSetAossButton_InitGraphics: Symbol[
        Optional[list[int]],
        None,
    ]

    SceneSetAossButton_ProcInit: Symbol[
        Optional[list[int]],
        None,
    ]

    SceneSetAossButton_ProcInit1: Symbol[
        Optional[list[int]],
        None,
    ]

    SceneSetAossButton_ProcInit2: Symbol[
        Optional[list[int]],
        None,
    ]

    SceneSetAossButton_ProcScene: Symbol[
        Optional[list[int]],
        None,
    ]

    SceneSetAossButton_Input: Symbol[
        Optional[list[int]],
        None,
    ]

    SceneSetAossButton_Draw: Symbol[
        Optional[list[int]],
        None,
    ]

    SceneSetAossButton_Button: Symbol[
        Optional[list[int]],
        None,
    ]

    SceneSetAossButton_EndScene: Symbol[
        Optional[list[int]],
        None,
    ]

    SceneSetAossButton_EndScene1: Symbol[
        Optional[list[int]],
        None,
    ]

    SceneSetAossButton_EndScene2: Symbol[
        Optional[list[int]],
        None,
    ]

    SceneSetAossButton_TaskVBlank: Symbol[
        Optional[list[int]],
        None,
    ]

    SceneSetAossButton_ProcError: Symbol[
        Optional[list[int]],
        None,
    ]

    SceneSetAossButton_ProcError1: Symbol[
        Optional[list[int]],
        None,
    ]

    SceneSetAossButton_ProcWait: Symbol[
        Optional[list[int]],
        None,
    ]

    SceneSetAossButton_ProcCancel: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_SceneSetAossComplete: Symbol[
        Optional[list[int]],
        None,
    ]

    SceneSetAossComplete_InitGraphics: Symbol[
        Optional[list[int]],
        None,
    ]

    SceneSetAossComplete_ProcInit: Symbol[
        Optional[list[int]],
        None,
    ]

    SceneSetAossComplete_ProcInit1: Symbol[
        Optional[list[int]],
        None,
    ]

    SceneSetAossComplete_ProcScene: Symbol[
        Optional[list[int]],
        None,
    ]

    SceneSetAossComplete_Draw: Symbol[
        Optional[list[int]],
        None,
    ]

    SceneSetAossComplete_EndScene: Symbol[
        Optional[list[int]],
        None,
    ]

    SceneSetAossComplete_EndScene1: Symbol[
        Optional[list[int]],
        None,
    ]

    SceneSetAossComplete_Wait: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_SceneSetApList: Symbol[
        Optional[list[int]],
        None,
    ]

    SceneSetApList_InitGraphics: Symbol[
        Optional[list[int]],
        None,
    ]

    InitScrollBar: Symbol[
        Optional[list[int]],
        None,
    ]

    GetCharName: Symbol[
        Optional[list[int]],
        None,
    ]

    SceneSetApList_ProcInit: Symbol[
        Optional[list[int]],
        None,
    ]

    SceneSetApList_ProcInit1: Symbol[
        Optional[list[int]],
        None,
    ]

    SceneSetApList_ProcInit2: Symbol[
        Optional[list[int]],
        None,
    ]

    SceneSetApList_ProcScene: Symbol[
        Optional[list[int]],
        None,
    ]

    SceneSetApList_Input: Symbol[
        Optional[list[int]],
        None,
    ]

    SceneSetApList_Draw: Symbol[
        Optional[list[int]],
        None,
    ]

    SceneSetApList_Button: Symbol[
        Optional[list[int]],
        None,
    ]

    SceneSetApList_EndScene: Symbol[
        Optional[list[int]],
        None,
    ]

    SceneSetApList_EndScene1: Symbol[
        Optional[list[int]],
        None,
    ]

    SceneSetApList_EndScene2: Symbol[
        Optional[list[int]],
        None,
    ]

    DrawApInfo: Symbol[
        Optional[list[int]],
        None,
    ]

    DrawAp: Symbol[
        Optional[list[int]],
        None,
    ]

    DrapApObj: Symbol[
        Optional[list[int]],
        None,
    ]

    SceneSetApList_SetOffset: Symbol[
        Optional[list[int]],
        None,
    ]

    SceneSetApList_TaskUp: Symbol[
        Optional[list[int]],
        None,
    ]

    SceneSetApList_TaskDown: Symbol[
        Optional[list[int]],
        None,
    ]

    SceneSetApList_TaskVBlank: Symbol[
        Optional[list[int]],
        None,
    ]

    SceneSetApList_DispFocus: Symbol[
        Optional[list[int]],
        None,
    ]

    SceneSetApList_MoveFocus: Symbol[
        Optional[list[int]],
        None,
    ]

    ScrollUp: Symbol[
        Optional[list[int]],
        None,
    ]

    ScrollDown: Symbol[
        Optional[list[int]],
        None,
    ]

    SceneSetApList_DispPushButton: Symbol[
        Optional[list[int]],
        None,
    ]

    SceneSetApList_ProcError: Symbol[
        Optional[list[int]],
        None,
    ]

    SceneSetApList_ProcError1: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_SceneSetEdit32: Symbol[
        Optional[list[int]],
        None,
    ]

    SceneSetEdit32_InitGraphics: Symbol[
        Optional[list[int]],
        None,
    ]

    SceneSetEdit32_ProcInit: Symbol[
        Optional[list[int]],
        None,
    ]

    SceneSetEdit32_ProcInit1: Symbol[
        Optional[list[int]],
        None,
    ]

    SceneSetEdit32_ProcInit2: Symbol[
        Optional[list[int]],
        None,
    ]

    SceneSetEdit32_ProcScene: Symbol[
        Optional[list[int]],
        None,
    ]

    SceneSetEdit32_Input: Symbol[
        Optional[list[int]],
        None,
    ]

    SceneSetEdit32_Draw: Symbol[
        Optional[list[int]],
        None,
    ]

    SceneSetEdit32_EndScene: Symbol[
        Optional[list[int]],
        None,
    ]

    SceneSetEdit32_EndScene1: Symbol[
        Optional[list[int]],
        None,
    ]

    SceneSetEdit32_EndScene2: Symbol[
        Optional[list[int]],
        None,
    ]

    SceneSetEdit32_EndScene3: Symbol[
        Optional[list[int]],
        None,
    ]

    DrawSsid: Symbol[
        Optional[list[int]],
        None,
    ]

    SceneSetEdit32_DispCaret: Symbol[
        Optional[list[int]],
        None,
    ]

    SceneSetEdit32_ProcWin: Symbol[
        Optional[list[int]],
        None,
    ]

    SceneSetEdit32_ProcWin1: Symbol[
        Optional[list[int]],
        None,
    ]

    SceneSetEdit32_IsCorrect: Symbol[
        Optional[list[int]],
        None,
    ]

    SceneSetEdit32_ProcError: Symbol[
        Optional[list[int]],
        None,
    ]

    SceneSetEdit32_ProcError1: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_SceneSetEditAddress: Symbol[
        Optional[list[int]],
        None,
    ]

    SceneSetEditAddress_InitGraphics: Symbol[
        Optional[list[int]],
        None,
    ]

    SceneSetEditAddress_ProcInit: Symbol[
        Optional[list[int]],
        None,
    ]

    SceneSetEditAddress_ProcInit1: Symbol[
        Optional[list[int]],
        None,
    ]

    SceneSetEditAddress_ProcInit2: Symbol[
        Optional[list[int]],
        None,
    ]

    SceneSetEditAddress_ProcScene: Symbol[
        Optional[list[int]],
        None,
    ]

    SceneSetEditAddress_Input: Symbol[
        Optional[list[int]],
        None,
    ]

    IsOver: Symbol[
        Optional[list[int]],
        None,
    ]

    SceneSetEditAddress_Draw: Symbol[
        Optional[list[int]],
        None,
    ]

    SceneSetEditAddress_EndScene: Symbol[
        Optional[list[int]],
        None,
    ]

    SceneSetEditAddress_EndScene1: Symbol[
        Optional[list[int]],
        None,
    ]

    SceneSetEditAddress_EndScene2: Symbol[
        Optional[list[int]],
        None,
    ]

    SceneSetEditAddress_EndScene3: Symbol[
        Optional[list[int]],
        None,
    ]

    SceneSetEditAddress_DrawAddress: Symbol[
        Optional[list[int]],
        None,
    ]

    SceneSetEditAddress_DispCaret: Symbol[
        Optional[list[int]],
        None,
    ]

    SceneSetEditAddress_ProcWin: Symbol[
        Optional[list[int]],
        None,
    ]

    SceneSetEditAddress_ProcWin1: Symbol[
        Optional[list[int]],
        None,
    ]

    ArrangeAddress: Symbol[
        Optional[list[int]],
        None,
    ]

    SceneSetEditAddress_IsCorrect: Symbol[
        Optional[list[int]],
        None,
    ]

    SceneSetEditAddress_ProcError: Symbol[
        Optional[list[int]],
        None,
    ]

    SceneSetEditAddress_ProcError1: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_SceneSetError: Symbol[
        Optional[list[int]],
        None,
    ]

    SceneSetError_InitGraphics: Symbol[
        Optional[list[int]],
        None,
    ]

    DrawMessage: Symbol[
        Optional[list[int]],
        None,
    ]

    SceneSetError_ProcInit: Symbol[
        Optional[list[int]],
        None,
    ]

    SceneSetError_ProcInit1: Symbol[
        Optional[list[int]],
        None,
    ]

    SceneSetError_ProcInit2: Symbol[
        Optional[list[int]],
        None,
    ]

    SceneSetError_ProcScene: Symbol[
        Optional[list[int]],
        None,
    ]

    SceneSetError_Input: Symbol[
        Optional[list[int]],
        None,
    ]

    SceneSetError_Draw: Symbol[
        Optional[list[int]],
        None,
    ]

    SceneSetError_Button: Symbol[
        Optional[list[int]],
        None,
    ]

    SceneSetError_EndScene: Symbol[
        Optional[list[int]],
        None,
    ]

    SceneSetError_EndScene1: Symbol[
        Optional[list[int]],
        None,
    ]

    SceneSetError_EndScene2: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_SetErrorCode: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_SceneSetList: Symbol[
        Optional[list[int]],
        None,
    ]

    SceneSetList_InitGraphics: Symbol[
        Optional[list[int]],
        None,
    ]

    CalcParam: Symbol[
        Optional[list[int]],
        None,
    ]

    SceneSetList_ProcInit: Symbol[
        Optional[list[int]],
        None,
    ]

    SceneSetList_ProcInit1: Symbol[
        Optional[list[int]],
        None,
    ]

    SceneSetList_ProcScene: Symbol[
        Optional[list[int]],
        None,
    ]

    SceneSetList_Input: Symbol[
        Optional[list[int]],
        None,
    ]

    InputWinButton: Symbol[
        Optional[list[int]],
        None,
    ]

    PushWinButton: Symbol[
        Optional[list[int]],
        None,
    ]

    SceneSetList_PushIpAuto: Symbol[
        Optional[list[int]],
        None,
    ]

    SceneSetList_PushDnsAuto: Symbol[
        Optional[list[int]],
        None,
    ]

    SceneSetList_Draw: Symbol[
        Optional[list[int]],
        None,
    ]

    SceneSetList_EndScene: Symbol[
        Optional[list[int]],
        None,
    ]

    SceneSetList_EndScene1: Symbol[
        Optional[list[int]],
        None,
    ]

    SceneSetList_EndScene2: Symbol[
        Optional[list[int]],
        None,
    ]

    SceneSetList_DrawWindow: Symbol[
        Optional[list[int]],
        None,
    ]

    SceneSetList_DrawColumnChar: Symbol[
        Optional[list[int]],
        None,
    ]

    SceneSetList_DrawColumnObj: Symbol[
        Optional[list[int]],
        None,
    ]

    SceneSetList_IsEnablePush: Symbol[
        Optional[list[int]],
        None,
    ]

    SceneSetList_DispObj: Symbol[
        Optional[list[int]],
        None,
    ]

    SceneSetList_DrawString: Symbol[
        Optional[list[int]],
        None,
    ]

    SceneSetList_DrawAddress: Symbol[
        Optional[list[int]],
        None,
    ]

    SceneSetList_SetOffset: Symbol[
        Optional[list[int]],
        None,
    ]

    SceneSetList_IsPush: Symbol[
        Optional[list[int]],
        None,
    ]

    SceneSetList_CalcColumnIdx: Symbol[
        Optional[list[int]],
        None,
    ]

    SceneSetList_CalcIdxColumn: Symbol[
        Optional[list[int]],
        None,
    ]

    SceneSetList_TaskUp: Symbol[
        Optional[list[int]],
        None,
    ]

    SceneSetList_TaskDown: Symbol[
        Optional[list[int]],
        None,
    ]

    SceneSetList_TaskVBlank: Symbol[
        Optional[list[int]],
        None,
    ]

    SceneSetList_DispFocus: Symbol[
        Optional[list[int]],
        None,
    ]

    SceneSetList_ApplyForcus: Symbol[
        Optional[list[int]],
        None,
    ]

    SceneSetList_ApplyForcus1: Symbol[
        Optional[list[int]],
        None,
    ]

    SceneSetList_MoveFocus: Symbol[
        Optional[list[int]],
        None,
    ]

    SceneSetList_DispPushButton: Symbol[
        Optional[list[int]],
        None,
    ]

    SceneSetList_TaskPushCount: Symbol[
        Optional[list[int]],
        None,
    ]

    SceneSetList_PushButtonYesNo: Symbol[
        Optional[list[int]],
        None,
    ]

    SceneSetList_IsCorrect: Symbol[
        Optional[list[int]],
        None,
    ]

    SceneSetList_ProcError: Symbol[
        Optional[list[int]],
        None,
    ]

    SceneSetList_ProcError1: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_SetListReturn: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_SceneSetListSave: Symbol[
        Optional[list[int]],
        None,
    ]

    SceneSetListSave_InitGraphics: Symbol[
        Optional[list[int]],
        None,
    ]

    SceneSetListSave_ProcInit: Symbol[
        Optional[list[int]],
        None,
    ]

    SceneSetListSave_ProcInit1: Symbol[
        Optional[list[int]],
        None,
    ]

    SceneSetListSave_ProcScene: Symbol[
        Optional[list[int]],
        None,
    ]

    SceneSetListSave_Input: Symbol[
        Optional[list[int]],
        None,
    ]

    SceneSetListSave_Draw: Symbol[
        Optional[list[int]],
        None,
    ]

    SceneSetListSave_EndScene: Symbol[
        Optional[list[int]],
        None,
    ]

    SceneSetListSave_EndScene1: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_SceneSetRakuButton: Symbol[
        Optional[list[int]],
        None,
    ]

    SceneSetRakuButton_InitGraphics: Symbol[
        Optional[list[int]],
        None,
    ]

    SceneSetRakuButton_ProcInit: Symbol[
        Optional[list[int]],
        None,
    ]

    SceneSetRakuButton_ProcInit1: Symbol[
        Optional[list[int]],
        None,
    ]

    SceneSetRakuButton_ProcInit2: Symbol[
        Optional[list[int]],
        None,
    ]

    SceneSetRakuButton_ProcScene: Symbol[
        Optional[list[int]],
        None,
    ]

    SceneSetRakuButton_Input: Symbol[
        Optional[list[int]],
        None,
    ]

    SceneSetRakuButton_Draw: Symbol[
        Optional[list[int]],
        None,
    ]

    SceneSetRakuButton_Button: Symbol[
        Optional[list[int]],
        None,
    ]

    SceneSetRakuButton_EndScene: Symbol[
        Optional[list[int]],
        None,
    ]

    SceneSetRakuButton_EndScene1: Symbol[
        Optional[list[int]],
        None,
    ]

    SceneSetRakuButton_EndScene2: Symbol[
        Optional[list[int]],
        None,
    ]

    SceneSetRakuButton_CheckRaku: Symbol[
        Optional[list[int]],
        None,
    ]

    SceneSetRakuButton_ProcError: Symbol[
        Optional[list[int]],
        None,
    ]

    SceneSetRakuButton_ProcError1: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_SceneSetRakuButton1: Symbol[
        Optional[list[int]],
        None,
    ]

    SceneSetRakuButton1_InitGraphics: Symbol[
        Optional[list[int]],
        None,
    ]

    SceneSetRakuButton1_ProcInit: Symbol[
        Optional[list[int]],
        None,
    ]

    SceneSetRakuButton1_ProcInit1: Symbol[
        Optional[list[int]],
        None,
    ]

    SceneSetRakuButton1_ProcInit2: Symbol[
        Optional[list[int]],
        None,
    ]

    SceneSetRakuButton1_ProcScene: Symbol[
        Optional[list[int]],
        None,
    ]

    SceneSetRakuButton1_Input: Symbol[
        Optional[list[int]],
        None,
    ]

    SceneSetRakuButton1_Draw: Symbol[
        Optional[list[int]],
        None,
    ]

    SceneSetRakuButton1_Button: Symbol[
        Optional[list[int]],
        None,
    ]

    SceneSetRakuButton1_EndScene: Symbol[
        Optional[list[int]],
        None,
    ]

    SceneSetRakuButton1_EndScene1: Symbol[
        Optional[list[int]],
        None,
    ]

    SceneSetRakuButton1_EndScene2: Symbol[
        Optional[list[int]],
        None,
    ]

    SceneSetRakuButton1_CheckRaku: Symbol[
        Optional[list[int]],
        None,
    ]

    SceneSetRakuButton1_ProcError: Symbol[
        Optional[list[int]],
        None,
    ]

    SceneSetRakuButton1_ProcError1: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_SceneSetRakuComplete: Symbol[
        Optional[list[int]],
        None,
    ]

    SceneSetRakuComplete_InitGraphics: Symbol[
        Optional[list[int]],
        None,
    ]

    SceneSetRakuComplete_ProcInit: Symbol[
        Optional[list[int]],
        None,
    ]

    SceneSetRakuComplete_ProcInit1: Symbol[
        Optional[list[int]],
        None,
    ]

    SceneSetRakuComplete_ProcScene: Symbol[
        Optional[list[int]],
        None,
    ]

    SceneSetRakuComplete_Draw: Symbol[
        Optional[list[int]],
        None,
    ]

    SceneSetRakuComplete_EndScene: Symbol[
        Optional[list[int]],
        None,
    ]

    SceneSetRakuComplete_EndScene1: Symbol[
        Optional[list[int]],
        None,
    ]

    SceneSetRakuComplete_Wait: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_SceneSetRakuReady: Symbol[
        Optional[list[int]],
        None,
    ]

    SceneSetRakuReady_InitGraphics: Symbol[
        Optional[list[int]],
        None,
    ]

    SceneSetRakuReady_ProcInit: Symbol[
        Optional[list[int]],
        None,
    ]

    SceneSetRakuReady_ProcInit1: Symbol[
        Optional[list[int]],
        None,
    ]

    SceneSetRakuReady_ProcInit2: Symbol[
        Optional[list[int]],
        None,
    ]

    SceneSetRakuReady_ProcScene: Symbol[
        Optional[list[int]],
        None,
    ]

    SceneSetRakuReady_Input: Symbol[
        Optional[list[int]],
        None,
    ]

    SceneSetRakuReady_Draw: Symbol[
        Optional[list[int]],
        None,
    ]

    SceneSetRakuReady_Button: Symbol[
        Optional[list[int]],
        None,
    ]

    SceneSetRakuReady_EndScene: Symbol[
        Optional[list[int]],
        None,
    ]

    SceneSetRakuReady_EndScene1: Symbol[
        Optional[list[int]],
        None,
    ]

    SceneSetRakuReady_EndScene2: Symbol[
        Optional[list[int]],
        None,
    ]

    SceneSetRakuReady_CheckRaku: Symbol[
        Optional[list[int]],
        None,
    ]

    SceneSetRakuReady_ProcError: Symbol[
        Optional[list[int]],
        None,
    ]

    SceneSetRakuReady_ProcError1: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_SceneSetSearch: Symbol[
        Optional[list[int]],
        None,
    ]

    SceneSetSearch_InitGraphics: Symbol[
        Optional[list[int]],
        None,
    ]

    SceneSetSearch_ProcInit: Symbol[
        Optional[list[int]],
        None,
    ]

    SceneSetSearch_ProcInit1: Symbol[
        Optional[list[int]],
        None,
    ]

    SceneSetSearch_ProcInit2: Symbol[
        Optional[list[int]],
        None,
    ]

    SceneSetSearch_ProcScene: Symbol[
        Optional[list[int]],
        None,
    ]

    SceneSetSearch_IsEnd: Symbol[
        Optional[list[int]],
        None,
    ]

    SceneSetSearch_Input: Symbol[
        Optional[list[int]],
        None,
    ]

    SceneSetSearch_Draw: Symbol[
        Optional[list[int]],
        None,
    ]

    SceneSetSearch_Button: Symbol[
        Optional[list[int]],
        None,
    ]

    SceneSetSearch_EndScene: Symbol[
        Optional[list[int]],
        None,
    ]

    SceneSetSearch_EndScene1: Symbol[
        Optional[list[int]],
        None,
    ]

    SceneSetSearch_EndScene2: Symbol[
        Optional[list[int]],
        None,
    ]

    SceneSetSearch_ProcError: Symbol[
        Optional[list[int]],
        None,
    ]

    SceneSetSearch_ProcError1: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_SceneSetSelectAp: Symbol[
        Optional[list[int]],
        None,
    ]

    SceneSetSelectAp_InitGraphics: Symbol[
        Optional[list[int]],
        None,
    ]

    SceneSetSelectAp_InitObj: Symbol[
        Optional[list[int]],
        None,
    ]

    SceneSetSelectAp_ProcInit: Symbol[
        Optional[list[int]],
        None,
    ]

    SceneSetSelectAp_ProcInit1: Symbol[
        Optional[list[int]],
        None,
    ]

    SceneSetSelectAp_ProcInit2: Symbol[
        Optional[list[int]],
        None,
    ]

    SceneSetSelectAp_ProcScene: Symbol[
        Optional[list[int]],
        None,
    ]

    SceneSetSelectAp_Input: Symbol[
        Optional[list[int]],
        None,
    ]

    SceneSetSelectAp_Draw: Symbol[
        Optional[list[int]],
        None,
    ]

    SceneSetSelectAp_Button: Symbol[
        Optional[list[int]],
        None,
    ]

    SceneSetSelectAp_EndScene: Symbol[
        Optional[list[int]],
        None,
    ]

    SceneSetSelectAp_EndScene1: Symbol[
        Optional[list[int]],
        None,
    ]

    SceneSetSelectAp_EndScene2: Symbol[
        Optional[list[int]],
        None,
    ]

    SceneSetSelectAp_DispFocus: Symbol[
        Optional[list[int]],
        None,
    ]

    SceneSetSelectAp_MoveFocus: Symbol[
        Optional[list[int]],
        None,
    ]

    SceneSetSelectAp_DispPushClear: Symbol[
        Optional[list[int]],
        None,
    ]

    SceneSetSelectAp_ProcErase: Symbol[
        Optional[list[int]],
        None,
    ]

    SceneSetSelectAp_ProcErase1: Symbol[
        Optional[list[int]],
        None,
    ]

    SceneSetSelectAp_DispPush: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_SceneSetSelectWay: Symbol[
        Optional[list[int]],
        None,
    ]

    SceneSetSelectWay_InitGraphics: Symbol[
        Optional[list[int]],
        None,
    ]

    SceneSetSelectWay_ProcInit: Symbol[
        Optional[list[int]],
        None,
    ]

    SceneSetSelectWay_ProcInit1: Symbol[
        Optional[list[int]],
        None,
    ]

    SceneSetSelectWay_ProcInit2: Symbol[
        Optional[list[int]],
        None,
    ]

    SceneSetSelectWay_ProcScene: Symbol[
        Optional[list[int]],
        None,
    ]

    SceneSetSelectWay_Input: Symbol[
        Optional[list[int]],
        None,
    ]

    SceneSetSelectWay_Draw: Symbol[
        Optional[list[int]],
        None,
    ]

    SceneSetSelectWay_Button: Symbol[
        Optional[list[int]],
        None,
    ]

    SceneSetSelectWay_EndScene: Symbol[
        Optional[list[int]],
        None,
    ]

    SceneSetSelectWay_EndScene1: Symbol[
        Optional[list[int]],
        None,
    ]

    SceneSetSelectWay_EndScene2: Symbol[
        Optional[list[int]],
        None,
    ]

    SceneSetSelectWay_MoveFocus: Symbol[
        Optional[list[int]],
        None,
    ]

    SceneSetSelectWay_DispPush: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_SceneSetTest: Symbol[
        Optional[list[int]],
        None,
    ]

    SceneSetTest_InitGraphics: Symbol[
        Optional[list[int]],
        None,
    ]

    SceneSetTest_InitAc: Symbol[
        Optional[list[int]],
        None,
    ]

    SceneSetTest_ProcInit: Symbol[
        Optional[list[int]],
        None,
    ]

    SceneSetTest_ProcInit1: Symbol[
        Optional[list[int]],
        None,
    ]

    SceneSetTest_ProcScene: Symbol[
        Optional[list[int]],
        None,
    ]

    SceneSetTest_Input: Symbol[
        Optional[list[int]],
        None,
    ]

    SceneSetTest_Draw: Symbol[
        Optional[list[int]],
        None,
    ]

    SceneSetTest_Button: Symbol[
        Optional[list[int]],
        None,
    ]

    SceneSetTest_EndScene: Symbol[
        Optional[list[int]],
        None,
    ]

    SceneSetTest_EndScene1: Symbol[
        Optional[list[int]],
        None,
    ]

    SceneSetTest_EndScene2: Symbol[
        Optional[list[int]],
        None,
    ]

    SceneSetTest_TaskAc: Symbol[
        Optional[list[int]],
        None,
    ]

    AcAlloc: Symbol[
        Optional[list[int]],
        None,
    ]

    AcFree: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_SceneSetTestCompletet: Symbol[
        Optional[list[int]],
        None,
    ]

    SceneSetTestCompletet_InitGraphics: Symbol[
        Optional[list[int]],
        None,
    ]

    SceneSetTestCompletet_ProcInit: Symbol[
        Optional[list[int]],
        None,
    ]

    SceneSetTestCompletet_ProcInit1: Symbol[
        Optional[list[int]],
        None,
    ]

    SceneSetTestCompletet_ProcScene: Symbol[
        Optional[list[int]],
        None,
    ]

    SceneSetTestCompletet_Draw: Symbol[
        Optional[list[int]],
        None,
    ]

    SceneSetTestCompletet_EndScene: Symbol[
        Optional[list[int]],
        None,
    ]

    SceneSetTestCompletet_EndScene1: Symbol[
        Optional[list[int]],
        None,
    ]

    SceneSetTestCompletet_Wait: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_SceneSetTestConfirm: Symbol[
        Optional[list[int]],
        None,
    ]

    SceneSetTestConfirm_InitGraphics: Symbol[
        Optional[list[int]],
        None,
    ]

    SceneSetTestConfirm_ProcInit: Symbol[
        Optional[list[int]],
        None,
    ]

    SceneSetTestConfirm_ProcInit1: Symbol[
        Optional[list[int]],
        None,
    ]

    SceneSetTestConfirm_ProcScene: Symbol[
        Optional[list[int]],
        None,
    ]

    SceneSetTestConfirm_Input: Symbol[
        Optional[list[int]],
        None,
    ]

    SceneSetTestConfirm_Draw: Symbol[
        Optional[list[int]],
        None,
    ]

    SceneSetTestConfirm_EndScene: Symbol[
        Optional[list[int]],
        None,
    ]

    SceneSetTestConfirm_EndScene1: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_SceneSetUsbComplete: Symbol[
        Optional[list[int]],
        None,
    ]

    SceneSetUsbComplete_InitGraphics: Symbol[
        Optional[list[int]],
        None,
    ]

    SceneSetUsbComplete_ProcInit: Symbol[
        Optional[list[int]],
        None,
    ]

    SceneSetUsbComplete_ProcInit1: Symbol[
        Optional[list[int]],
        None,
    ]

    SceneSetUsbComplete_ProcScene: Symbol[
        Optional[list[int]],
        None,
    ]

    SceneSetUsbComplete_Draw: Symbol[
        Optional[list[int]],
        None,
    ]

    SceneSetUsbComplete_EndScene: Symbol[
        Optional[list[int]],
        None,
    ]

    SceneSetUsbComplete_EndScene1: Symbol[
        Optional[list[int]],
        None,
    ]

    SceneSetUsbComplete_Wait: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_SceneSetUsbReady: Symbol[
        Optional[list[int]],
        None,
    ]

    SceneSetUsbReady_InitGraphics: Symbol[
        Optional[list[int]],
        None,
    ]

    SceneSetUsbReady_ProcInit: Symbol[
        Optional[list[int]],
        None,
    ]

    SceneSetUsbReady_ProcInit1: Symbol[
        Optional[list[int]],
        None,
    ]

    SceneSetUsbReady_ProcInit2: Symbol[
        Optional[list[int]],
        None,
    ]

    SceneSetUsbReady_ProcScene: Symbol[
        Optional[list[int]],
        None,
    ]

    SceneSetUsbReady_Input: Symbol[
        Optional[list[int]],
        None,
    ]

    SceneSetUsbReady_Draw: Symbol[
        Optional[list[int]],
        None,
    ]

    SceneSetUsbReady_Button: Symbol[
        Optional[list[int]],
        None,
    ]

    SceneSetUsbReady_EndScene: Symbol[
        Optional[list[int]],
        None,
    ]

    SceneSetUsbReady_EndScene1: Symbol[
        Optional[list[int]],
        None,
    ]

    SceneSetUsbReady_EndScene2: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_SceneSetUsbReady1: Symbol[
        Optional[list[int]],
        None,
    ]

    SceneSetUsbReady1_InitGraphics: Symbol[
        Optional[list[int]],
        None,
    ]

    SceneSetUsbReady1_ProcInit: Symbol[
        Optional[list[int]],
        None,
    ]

    SceneSetUsbReady1_ProcInit1: Symbol[
        Optional[list[int]],
        None,
    ]

    SceneSetUsbReady1_ProcInit2: Symbol[
        Optional[list[int]],
        None,
    ]

    SceneSetUsbReady1_ProcScene: Symbol[
        Optional[list[int]],
        None,
    ]

    SceneSetUsbReady1_Input: Symbol[
        Optional[list[int]],
        None,
    ]

    SceneSetUsbReady1_Draw: Symbol[
        Optional[list[int]],
        None,
    ]

    SceneSetUsbReady1_Button: Symbol[
        Optional[list[int]],
        None,
    ]

    SceneSetUsbReady1_EndScene: Symbol[
        Optional[list[int]],
        None,
    ]

    SceneSetUsbReady1_EndScene1: Symbol[
        Optional[list[int]],
        None,
    ]

    SceneSetUsbReady1_EndScene2: Symbol[
        Optional[list[int]],
        None,
    ]

    SceneSetUsbReady1_CbUsb: Symbol[
        Optional[list[int]],
        None,
    ]

    SceneSetUsbReady1_ProcNotFound: Symbol[
        Optional[list[int]],
        None,
    ]

    SceneSetUsbReady1_ProcNotFound1: Symbol[
        Optional[list[int]],
        None,
    ]

    SceneSetUsbReady1_ProcBoth: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_ScreenlInit: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_ScreenlEnd: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_ScreenlRenew: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_ScreenlCopy: Symbol[
        Optional[list[int]],
        None,
    ]

    Screen_TaskLoad: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_ScreenlCopyPalette: Symbol[
        Optional[list[int]],
        None,
    ]

    Screen_TaskCopyPltt: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_ScreenlSetPalette: Symbol[
        Optional[list[int]],
        None,
    ]

    Screen_TaskSetPltt: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_SBlInit: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_SBlEnd: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_SBlGet: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_SBlGetState: Symbol[
        Optional[list[int]],
        None,
    ]

    Scrollbar_Disp: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_SBlEnable: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_SBlDisable: Symbol[
        Optional[list[int]],
        None,
    ]

    Scrollbar_TaskMain: Symbol[
        Optional[list[int]],
        None,
    ]

    Scrollbar_MoveBar: Symbol[
        Optional[list[int]],
        None,
    ]

    Scrollbar_PlaySound: Symbol[
        Optional[list[int]],
        None,
    ]

    Scrollbar_StepBar: Symbol[
        Optional[list[int]],
        None,
    ]

    Scrollbar_SetBar: Symbol[
        Optional[list[int]],
        None,
    ]

    Scrollbar_IsTrigger: Symbol[
        Optional[list[int]],
        None,
    ]

    Scrollbar_IsTouch: Symbol[
        Optional[list[int]],
        None,
    ]

    Scrollbar_CalcRect: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_SearchlInit: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_SearchlEnd: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_SearchlBegin: Symbol[
        Optional[list[int]],
        None,
    ]

    Search_StartScan: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_SearchlStop: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_SearchlGetApInfo: Symbol[
        Optional[list[int]],
        None,
    ]

    Search_Callback: Symbol[
        Optional[list[int]],
        None,
    ]

    Search_RenewInfo: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_SettignlInit: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_SettignlEnd: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_SettignlGet: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_SettinglSetIpAuto: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_SettinglSetDnsAuto: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_SettinglSetSsid: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_SettinglSetWep: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_SettinglSetIp: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_SettinglSetNetMask: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_SettinglSetGateway: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_SettinglSetDnsP: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_SettinglGetSsid: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_SettinglGetIp: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_SettinglGetNetMask: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_SettinglGetGateway: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_SettinglGetDnsP: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_SettinglGetDnsS: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_SettinglGetSetType: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_SettinglSetSetting: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_SettinglSet: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_SettinglSetRaku: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_SettinglSetAoss: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_SettinglGetMemMap: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_SettinglErasePage: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_SettinglEraseAll: Symbol[
        Optional[list[int]],
        None,
    ]

    Setting_Write: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_SettinglConvAddress: Symbol[
        Optional[list[int]],
        None,
    ]

    Setting_Ascii2Hex: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_SndlInit: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_SndlEnd: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_SndlPlay: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_SndlSetVolume: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_SndlSetPitch: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_SndlStop: Symbol[
        Optional[list[int]],
        None,
    ]

    Sound_TaskSound: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_SteplBegin: Symbol[
        Optional[list[int]],
        None,
    ]

    Step_TaskBegin0: Symbol[
        Optional[list[int]],
        None,
    ]

    Step_TaskBegin1: Symbol[
        Optional[list[int]],
        None,
    ]

    Step_TaskBegin2: Symbol[
        Optional[list[int]],
        None,
    ]

    Step_TaskBegin3: Symbol[
        Optional[list[int]],
        None,
    ]

    Step_TaskBegin4: Symbol[
        Optional[list[int]],
        None,
    ]

    Step_TaskBegin5: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_SteplEnd: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_SteplChange: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_SteplGet: Symbol[
        Optional[list[int]],
        None,
    ]

    Step_TaskEnd0: Symbol[
        Optional[list[int]],
        None,
    ]

    Step_TaskEnd1: Symbol[
        Optional[list[int]],
        None,
    ]

    Step_TaskEnd2: Symbol[
        Optional[list[int]],
        None,
    ]

    Step_TaskEnd3: Symbol[
        Optional[list[int]],
        None,
    ]

    Step_TaskEnd4: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_SteplIsEnd: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_SteplChangeScr: Symbol[
        Optional[list[int]],
        None,
    ]

    Step_TaskChange: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_UsbaplBegin: Symbol[
        Optional[list[int]],
        None,
    ]

    UsbAc_StartScan: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_UsbaplEnd: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_UsbaplSetCallback: Symbol[
        Optional[list[int]],
        None,
    ]

    UsbAc_CbWm: Symbol[
        Optional[list[int]],
        None,
    ]

    UsbAc_ScanFirst: Symbol[
        Optional[list[int]],
        None,
    ]

    UsbAc_ScanWait: Symbol[
        Optional[list[int]],
        None,
    ]

    UsbAc_TaskFirst: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_WinlInitEx: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_WinlEnd: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_WinlGet: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_WinlIsInit: Symbol[
        Optional[list[int]],
        None,
    ]

    Window_TaskV: Symbol[
        Optional[list[int]],
        None,
    ]

    Window_TaskMove: Symbol[
        Optional[list[int]],
        None,
    ]

    Window_TaskMain: Symbol[
        Optional[list[int]],
        None,
    ]

    Window_TaskMain1: Symbol[
        Optional[list[int]],
        None,
    ]

    Window_Disp: Symbol[
        Optional[list[int]],
        None,
    ]

    Window_DispCell: Symbol[
        Optional[list[int]],
        None,
    ]

    Window_PushButton: Symbol[
        Optional[list[int]],
        None,
    ]

    Window_TaskEnd: Symbol[
        Optional[list[int]],
        None,
    ]

    Window_TaskEnd1: Symbol[
        Optional[list[int]],
        None,
    ]

    WindowTaskEnd2: Symbol[
        Optional[list[int]],
        None,
    ]

    Window_TaskEnd3: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_Mov_Mbp_MemInit: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_Mov_Mbp_Init: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_Mov_Mbp_Start: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_Mov_Mbp_RegistFile: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_Mov_Mbp_AcceptChild: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_Mov_Mbp_KickChild: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_Mov_Mbp_StartDownload: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_Mov_Mbp_StartDownloadAll: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_Mov_Mbp_IsBootableAll: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_Mov_Mbp_StartRebootAll: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_Mov_Mbp_Cancel: Symbol[
        Optional[list[int]],
        None,
    ]

    ParentStateCallback_Helper: Symbol[
        Optional[list[int]],
        None,
    ]

    ParentStateCallback: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_Mov_Mbp_ChangeState: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_Mov_Mbp_GetState: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_Mov_Mbp_GetChildBmp: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_Mov_Mbp_GetChildState: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_Mov_Mbp_GetChildInfo: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_Mov_Mbp_GetPlayerNo: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_Mov_WH_MemInit: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_Mov_WH_ChangeSysState: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_Mov_WH_SetError: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_Mov_WH_StateInSetParentParam: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_Mov_WH_StateOutSetParentParam: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_Mov_WH_StateInStartParent: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_Mov_WH_StateOutSetParentWepKey: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_Mov_WH_StateInSetParentWepKey: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_Mov_WH_StateOutStartParent: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_Mov_WH_StateInStartParentMP: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_Mov_WH_StateOutStartParentMP: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_Mov_WH_StateInStartParentKeyShare: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_Mov_WH_StateInEndParentKeyShare: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_Mov_WH_StateInEndParentMP: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_Mov_WH_StateOutEndParentMP: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_Mov_WH_StateInEndParent: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_Mov_WH_StateOutEndParent: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_Mov_WH_StateInEndChildKeyShare: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_Mov_WH_StateInEndChildMP: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_Mov_WH_StateOutEndChildMP: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_Mov_WH_StateInEndChild: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_Mov_WH_StateOutEndChild: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_Mov_WH_StateInReset: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_Mov_WH_StateOutReset: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_Mov_WH_StateOutEnd: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_Mov_WH_SetGgid: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_Mov_WH_GetBitmap: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_Mov_WH_GetSystemState: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_Mov_WH_StartMeasureChannel: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_Mov_WH_StateInMeasureChannel: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_Mov_WH_StateOutMeasureChannel: Symbol[
        Optional[list[int]],
        None,
    ]

    WHi_MeasureChannel: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_Mov_WH_GetMeasureChannel: Symbol[
        Optional[list[int]],
        None,
    ]

    SelectChannel: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_Mov_WH_Initialize: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_Mov_WH_IndicateHandler: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_Mov_WH_StateInInitialize: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_Mov_WH_StateOutInitialize: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_Mov_WH_ParentConnect: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_Mov_WH_SetJudgeAcceptFunc: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_Mov_WH_GetSharedDataAdr: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_Mov_WH_StepDS: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_Mov_WH_Reset: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_Mov_WH_Finalize: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_Mov_WH_End: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_MovInit: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_MovFinalize: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_MovPrepare: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_MovStartAdmitChild: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_MovStartDownloadandBootChild: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_MovFramework: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_MovGetStatus: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_GetChildInfo: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_MovSearchChannel: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_MovStartWaitChild: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_Mov_WaitandDownloadandBoot_Child: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_Mov_ReadyMovUserID: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_Mov_MovUserID: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_Mov_EraseFlashData: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_MovEnd: Symbol[
        Optional[list[int]],
        None,
    ]

    JudgeConnectableChild: Symbol[
        Optional[list[int]],
        None,
    ]

    Parent_InitDataShare: Symbol[
        Optional[list[int]],
        None,
    ]

    Parent_StepDataShare: Symbol[
        Optional[list[int]],
        None,
    ]

    Parent_Data_Receive_Progress: Symbol[
        Optional[list[int]],
        None,
    ]

    Parent_Get_Child_Data_Kind: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_ArclInit: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_ArclEnd: Symbol[
        Optional[list[int]],
        None,
    ]

    UserProc: Symbol[
        Optional[list[int]],
        None,
    ]

    CbRead: Symbol[
        Optional[list[int]],
        None,
    ]

    CbReadRom: Symbol[
        Optional[list[int]],
        None,
    ]

    CbWrite: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_ArclReadEx: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_ArclRelease: Symbol[
        Optional[list[int]],
        None,
    ]

    CmpBack: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_CelllInit: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_CelllEnd: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_CelllForm: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_CelllDelete: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_CelllGetObj: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_CelllGetObjNum: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_CelllSetEffect: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_CelllSetPalette: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_CelllSetPosition: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_CelllSetPriority: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_CelllGetPosition: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_CeinlRead: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_CeinlRelease: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_CeinlSet: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_CeinlSetExObj: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_CeinlSetExCell: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_QuelForm: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_QuelFormEx: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_QuelDelete: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_QuelPushBack: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_QuelPopBack: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_EfflInit: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_EfflEnd: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_EfflCheck: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_EfflFade: Symbol[
        Optional[list[int]],
        None,
    ]

    Effect_TaskFade: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_EfflWait: Symbol[
        Optional[list[int]],
        None,
    ]

    Effect_TaskWait: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_FntlInit: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_FntlEnd: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_FntlFormEx: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_FntlDelete: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_FntlFormBgEx: Symbol[
        Optional[list[int]],
        None,
    ]

    Font_TaskLoad: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_FntlDeleteBg: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_FntlDeleteBgLcd: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_FntlDraw: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_FntlDrawCharEx: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_FntlDrawStringEx: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_FntlDrawRect: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_FntlClear: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_FntlDisp: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_FntlRenewBg: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_InputCoord: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_InputRect: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_Coord2Rect: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_GXlVisible: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_GXlInvisible: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_GXlSetWndPosition: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_GXlSetWndPlane: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_HeaplInit: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_HeaplEnd: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_HeaplAlloc: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_HeaplAllocEx: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_HeaplFree: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_HeaplFree2: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_IptlInit: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_IptlEnd: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_IptlRead: Symbol[
        Optional[list[int]],
        None,
    ]

    Input_ReadKey: Symbol[
        Optional[list[int]],
        None,
    ]

    Input_ReadTouch: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_IptlCheckTrigger: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_IptlCheckRepeat: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_IptlCheckRelease: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_TPlCheck: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_TPlCheckTrigger: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_TPlCheckRepeat: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_TPlCheckRelease: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_TPlCheckATrigger: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_TPlGet: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_IptlCheckFold: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_ItrlIntr: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_ItrlEnd: Symbol[
        Optional[list[int]],
        None,
    ]

    IntrVBlank: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_LstlForm: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_LstlDelete: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_LstlErase: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_LstlInsert: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_LstlPushBack: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_LstlPushFront: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_ObjlInit: Symbol[
        Optional[list[int]],
        None,
    ]

    Obj_TaskTransfer: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_ObjlEnd: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_ObjlFormGx: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_ObjlDelete: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_ObjlGetOam: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_OvrlInit: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_OvrlAlloc: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_OvrlFree: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_StrlNLen: Symbol[
        Optional[list[int]],
        None,
    ]

    swprintf_subroutine: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_ClearVram: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_RepairVram: Symbol[
        Optional[list[int]],
        None,
    ]

    Sub_ClearVram: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_SetLedWireless: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_SetLedNormal: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_TsklInit: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_TsklEnd: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_TsklAct: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_TsklForm: Symbol[
        Optional[list[int]],
        None,
    ]

    Task_FormTask: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_TsklChangeFunc: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_TsklDelete: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_TsklDeleteEx: Symbol[
        Optional[list[int]],
        None,
    ]

    Task_DeleteTcb: Symbol[
        Optional[list[int]],
        None,
    ]

    Dwci_TsklOperate: Symbol[
        Optional[list[int]],
        None,
    ]


class Overlay2DataProtocol(Protocol):

    OV2_STATIC_INITIALIZER: Symbol[
        Optional[list[int]],
        Optional[int],
    ]


Overlay2Protocol = SectionProtocol[
    Overlay2FunctionsProtocol,
    Overlay2DataProtocol,
    Optional[int],
]


class Overlay20FunctionsProtocol(Protocol):

    pass


class Overlay20DataProtocol(Protocol):

    OVERLAY20_UNKNOWN_POINTER__NA_238CF7C: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    RECYCLE_MENU_ITEMS_CONFIRM_1: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    RECYCLE_MENU_ITEMS_CONFIRM_2: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    RECYCLE_SUBMENU_ITEMS_1: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    RECYCLE_SUBMENU_ITEMS_2: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    RECYCLE_MAIN_MENU_ITEMS_1: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    OVERLAY20_UNKNOWN_TABLE__NA_238D014: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    RECYCLE_WINDOW_PARAMS_1: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    RECYCLE_WINDOW_PARAMS_2: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    RECYCLE_WINDOW_PARAMS_3: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    RECYCLE_WINDOW_PARAMS_4: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    RECYCLE_WINDOW_PARAMS_5: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    RECYCLE_WINDOW_PARAMS_6: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    RECYCLE_MAIN_MENU_ITEMS_2: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    RECYCLE_WINDOW_PARAMS_7: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    RECYCLE_WINDOW_PARAMS_8: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    RECYCLE_WINDOW_PARAMS_9: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    RECYCLE_WINDOW_PARAMS_10: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    RECYCLE_WINDOW_PARAMS_11: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    RECYCLE_MAIN_MENU_ITEMS_3: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    OV20_STATIC_INITIALIZER: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    OVERLAY20_UNKNOWN_POINTER__NA_238D120: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    OVERLAY20_UNKNOWN_POINTER__NA_238D124: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    OVERLAY20_UNKNOWN_POINTER__NA_238D128: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    OVERLAY20_UNKNOWN_POINTER__NA_238D12C: Symbol[
        Optional[list[int]],
        Optional[int],
    ]


Overlay20Protocol = SectionProtocol[
    Overlay20FunctionsProtocol,
    Overlay20DataProtocol,
    Optional[int],
]


class Overlay21FunctionsProtocol(Protocol):

    SwapShopDialogueManager: Symbol[
        Optional[list[int]],
        None,
    ]

    GetFirstExclusivePrerequisite: Symbol[
        Optional[list[int]],
        None,
    ]

    SwapShopEntryPoint: Symbol[
        Optional[list[int]],
        None,
    ]

    SwapShopDestructor: Symbol[
        Optional[list[int]],
        None,
    ]

    SwapShopMainManager: Symbol[
        Optional[list[int]],
        None,
    ]

    CloseTextboxAndSimpleMenu: Symbol[
        Optional[list[int]],
        None,
    ]

    SwapShopPrintCurrentGold: Symbol[
        Optional[list[int]],
        None,
    ]


class Overlay21DataProtocol(Protocol):

    SWAP_SHOP_WINDOW_PARAMS_1: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    SWAP_SHOP_MENU_ITEMS_CONFIRM: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    SWAP_SHOP_SUBMENU_ITEMS_1: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    SWAP_SHOP_SUBMENU_ITEMS_2: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    SWAP_SHOP_MAIN_MENU_ITEMS_1: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    SWAP_SHOP_MAIN_MENU_ITEMS_2: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    SWAP_SHOP_SUBMENU_ITEMS_3: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    OVERLAY21_UNKNOWN_STRING_IDS: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    SWAP_SHOP_WINDOW_PARAMS_2: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    SWAP_SHOP_WINDOW_PARAMS_3: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    SWAP_SHOP_WINDOW_PARAMS_4: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    SWAP_SHOP_WINDOW_PARAMS_5: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    SWAP_SHOP_WINDOW_PARAMS_6: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    SWAP_SHOP_WINDOW_PARAMS_7: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    SWAP_SHOP_WINDOW_PARAMS_8: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    SWAP_SHOP_WINDOW_PARAMS_9: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    SWAP_SHOP_TALK_WELCOME_DEBUG_STRING: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    SWAP_SHOP_MAIN_MENU_OPTIONS_DEBUG_STRING: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    SWAP_SHOP_TALK_CONTINUE_SWAP_DEBUG_STRING: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    SWAP_SHOP_TALK_SUBINFO_DEBUG_STRING: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    SWAP_SHOP_TALK_COME_AGAIN_DEBUG_STRING: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    SWAP_SHOP_TALK_LACKING_SWAP_ITEMS_DEBUG_STRING: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    SWAP_SHOP_TALK_SWAP_BROKE_DEBUG_STRING: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    SWAP_SHOP_TALK_SWAP_POOR_DEBUG_STRING: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    SWAP_SHOP_UNK_8_DEBUG_STRING: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    SWAP_SHOP_CLOSE_SHOP_DEBUG_STRING: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    SWAP_SHOP_TALK_WHAT_ITEMS_DEBUG_STRING: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    SWAP_SHOP_TALK_VALUABLE_SWAP_DEBUG_STRING: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    SWAP_SHOP_INIT_SWAP_ITEMS_MENU_DEBUG_STRING: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    SWAP_SHOP_SWAP_ITEMS_MENU_DEBUG_STRING: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    SWAP_SHOP_RETURN_SWAP_ITEMS_MENU_DEBUG_STRING: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    SWAP_SHOP_SELECT_SWAP_ITEM_OPTIONS_DEBUG_STRING: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    SWAP_SHOP_SWAP_ITEM_GET_INFO_DEBUG_STRING: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    SWAP_SHOP_ITEM_ZERO_STRING: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    SWAP_SHOP_TALK_CONFIRM_SWAP_DEBUG_STRING: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    SWAP_SHOP_CONFIRM_CHOICE_DEBUG_STRING: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    SWAP_SHOP_INIT_SCRIPT_ACTION_1_DEBUG_STRING: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    SWAP_SHOP_INIT_SCRIPT_ACTION_2_DEBUG_STRING: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    SWAP_SHOP_INIT_SCRIPT_ACTION_3_DEBUG_STRING: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    SWAP_SHOP_TEXT_PUT_IN_CAULDRON_DEBUG_STRING: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    SWAP_SHOP_DO_SWAP_THEN_TALK_DEBUG_STRING: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    OVERLAY21_JP_STRING: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    SWAP_SHOP_GOLD_STRING: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    OV21_STATIC_INITIALIZER: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    SWAP_SHOP_MENU_DATA_PTR: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    OVERLAY21_UNKNOWN_POINTER__NA_238CF44: Symbol[
        Optional[list[int]],
        Optional[int],
    ]


Overlay21Protocol = SectionProtocol[
    Overlay21FunctionsProtocol,
    Overlay21DataProtocol,
    Optional[int],
]


class Overlay22FunctionsProtocol(Protocol):

    pass


class Overlay22DataProtocol(Protocol):

    SHOP_WINDOW_PARAMS_1: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    SHOP_WINDOW_PARAMS_2: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    OVERLAY22_UNKNOWN_STRUCT__NA_238E85C: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    SHOP_MENU_ITEMS_CONFIRM: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    SHOP_MAIN_MENU_ITEMS_1: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    SHOP_MAIN_MENU_ITEMS_2: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    SHOP_MAIN_MENU_ITEMS_3: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    OVERLAY22_UNKNOWN_STRING_IDS: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    SHOP_WINDOW_PARAMS_3: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    SHOP_WINDOW_PARAMS_4: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    SHOP_WINDOW_PARAMS_5: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    SHOP_WINDOW_PARAMS_6: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    SHOP_WINDOW_PARAMS_7: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    SHOP_WINDOW_PARAMS_8: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    SHOP_WINDOW_PARAMS_9: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    SHOP_WINDOW_PARAMS_10: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    OV22_STATIC_INITIALIZER: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    OVERLAY22_UNKNOWN_POINTER__NA_238EC60: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    OVERLAY22_UNKNOWN_POINTER__NA_238EC64: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    OVERLAY22_UNKNOWN_POINTER__NA_238EC68: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    OVERLAY22_UNKNOWN_POINTER__NA_238EC6C: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    OVERLAY22_UNKNOWN_POINTER__NA_238EC70: Symbol[
        Optional[list[int]],
        Optional[int],
    ]


Overlay22Protocol = SectionProtocol[
    Overlay22FunctionsProtocol,
    Overlay22DataProtocol,
    Optional[int],
]


class Overlay23FunctionsProtocol(Protocol):

    pass


class Overlay23DataProtocol(Protocol):

    OVERLAY23_UNKNOWN_VALUE__NA_238D2E8: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    OVERLAY23_UNKNOWN_VALUE__NA_238D2EC: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    OVERLAY23_UNKNOWN_STRUCT__NA_238D2F0: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    STORAGE_MENU_ITEMS_CONFIRM: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    STORAGE_MAIN_MENU_ITEMS_1: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    STORAGE_MAIN_MENU_ITEMS_2: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    STORAGE_MAIN_MENU_ITEMS_3: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    STORAGE_MAIN_MENU_ITEMS_4: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    OVERLAY23_UNKNOWN_STRING_IDS: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    STORAGE_WINDOW_PARAMS_1: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    STORAGE_WINDOW_PARAMS_2: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    STORAGE_WINDOW_PARAMS_3: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    STORAGE_WINDOW_PARAMS_4: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    STORAGE_WINDOW_PARAMS_5: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    STORAGE_WINDOW_PARAMS_6: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    STORAGE_WINDOW_PARAMS_7: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    STORAGE_WINDOW_PARAMS_8: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    OV23_STATIC_INITIALIZER: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    OVERLAY23_UNKNOWN_POINTER__NA_238D8A0: Symbol[
        Optional[list[int]],
        Optional[int],
    ]


Overlay23Protocol = SectionProtocol[
    Overlay23FunctionsProtocol,
    Overlay23DataProtocol,
    Optional[int],
]


class Overlay24FunctionsProtocol(Protocol):

    pass


class Overlay24DataProtocol(Protocol):

    OVERLAY24_UNKNOWN_STRUCT__NA_238C508: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    OVERLAY24_UNKNOWN_STRUCT__NA_238C514: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    DAYCARE_MENU_ITEMS_CONFIRM: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    DAYCARE_MAIN_MENU_ITEMS: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    OVERLAY24_UNKNOWN_STRING_IDS: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    DAYCARE_WINDOW_PARAMS_1: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    DAYCARE_WINDOW_PARAMS_2: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    DAYCARE_WINDOW_PARAMS_3: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    DAYCARE_WINDOW_PARAMS_4: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    DAYCARE_WINDOW_PARAMS_5: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    OV24_STATIC_INITIALIZER: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    OVERLAY24_UNKNOWN_POINTER__NA_238C600: Symbol[
        Optional[list[int]],
        Optional[int],
    ]


Overlay24Protocol = SectionProtocol[
    Overlay24FunctionsProtocol,
    Overlay24DataProtocol,
    Optional[int],
]


class Overlay25FunctionsProtocol(Protocol):

    pass


class Overlay25DataProtocol(Protocol):

    OVERLAY25_UNKNOWN_STRUCT__NA_238B498: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    APPRAISAL_WINDOW_PARAMS_1: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    APPRAISAL_MENU_ITEMS_CONFIRM: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    APPRAISAL_MAIN_MENU_ITEMS: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    APPRAISAL_SUBMENU_ITEMS: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    OVERLAY25_UNKNOWN_STRING_IDS: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    APPRAISAL_WINDOW_PARAMS_2: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    APPRAISAL_WINDOW_PARAMS_3: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    APPRAISAL_WINDOW_PARAMS_4: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    APPRAISAL_WINDOW_PARAMS_5: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    APPRAISAL_WINDOW_PARAMS_6: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    APPRAISAL_WINDOW_PARAMS_7: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    APPRAISAL_WINDOW_PARAMS_8: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    OV25_STATIC_INITIALIZER: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    OVERLAY25_UNKNOWN_POINTER__NA_238B5E0: Symbol[
        Optional[list[int]],
        Optional[int],
    ]


Overlay25Protocol = SectionProtocol[
    Overlay25FunctionsProtocol,
    Overlay25DataProtocol,
    Optional[int],
]


class Overlay26FunctionsProtocol(Protocol):

    pass


class Overlay26DataProtocol(Protocol):

    OVERLAY26_UNKNOWN_TABLE__NA_238AE20: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    OV26_STATIC_INITIALIZER: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    OVERLAY26_UNKNOWN_POINTER__NA_238AF60: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    OVERLAY26_UNKNOWN_POINTER__NA_238AF64: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    OVERLAY26_UNKNOWN_POINTER__NA_238AF68: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    OVERLAY26_UNKNOWN_POINTER__NA_238AF6C: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    OVERLAY26_UNKNOWN_POINTER5__NA_238AF70: Symbol[
        Optional[list[int]],
        Optional[int],
    ]


Overlay26Protocol = SectionProtocol[
    Overlay26FunctionsProtocol,
    Overlay26DataProtocol,
    Optional[int],
]


class Overlay27FunctionsProtocol(Protocol):

    pass


class Overlay27DataProtocol(Protocol):

    OVERLAY27_UNKNOWN_VALUE__NA_238C948: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    OVERLAY27_UNKNOWN_VALUE__NA_238C94C: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    OVERLAY27_UNKNOWN_STRUCT__NA_238C950: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    DISCARD_ITEMS_MENU_ITEMS_CONFIRM: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    DISCARD_ITEMS_SUBMENU_ITEMS_1: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    DISCARD_ITEMS_SUBMENU_ITEMS_2: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    DISCARD_ITEMS_MAIN_MENU_ITEMS: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    OVERLAY27_UNKNOWN_STRING_IDS: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    DISCARD_WINDOW_PARAMS_1: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    DISCARD_WINDOW_PARAMS_2: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    DISCARD_WINDOW_PARAMS_3: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    DISCARD_WINDOW_PARAMS_4: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    DISCARD_WINDOW_PARAMS_5: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    DISCARD_WINDOW_PARAMS_6: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    DISCARD_WINDOW_PARAMS_7: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    DISCARD_WINDOW_PARAMS_8: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    OV27_STATIC_INITIALIZER: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    OVERLAY27_UNKNOWN_POINTER__NA_238CE80: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    OVERLAY27_UNKNOWN_POINTER__NA_238CE84: Symbol[
        Optional[list[int]],
        Optional[int],
    ]


Overlay27Protocol = SectionProtocol[
    Overlay27FunctionsProtocol,
    Overlay27DataProtocol,
    Optional[int],
]


class Overlay28FunctionsProtocol(Protocol):

    pass


class Overlay28DataProtocol(Protocol):

    OV28_STATIC_INITIALIZER: Symbol[
        Optional[list[int]],
        Optional[int],
    ]


Overlay28Protocol = SectionProtocol[
    Overlay28FunctionsProtocol,
    Overlay28DataProtocol,
    Optional[int],
]


class Overlay29FunctionsProtocol(Protocol):

    GetWeatherColorTable: Symbol[
        Optional[list[int]],
        None,
    ]

    DungeonAlloc: Symbol[
        Optional[list[int]],
        None,
    ]

    GetDungeonPtrMaster: Symbol[
        Optional[list[int]],
        None,
    ]

    DungeonZInit: Symbol[
        Optional[list[int]],
        None,
    ]

    DungeonFree: Symbol[
        Optional[list[int]],
        None,
    ]

    RunDungeon: Symbol[
        Optional[list[int]],
        None,
    ]

    EntityIsValid: Symbol[
        Optional[list[int]],
        None,
    ]

    FloorSecondaryTerrainIsChasm: Symbol[
        Optional[list[int]],
        None,
    ]

    GetFloorType: Symbol[
        Optional[list[int]],
        None,
    ]

    TryForcedLoss: Symbol[
        Optional[list[int]],
        None,
    ]

    IsBossFight: Symbol[
        Optional[list[int]],
        None,
    ]

    IsCurrentFixedRoomBossFight: Symbol[
        Optional[list[int]],
        None,
    ]

    IsMarowakTrainingMaze: Symbol[
        Optional[list[int]],
        None,
    ]

    FixedRoomIsSubstituteRoom: Symbol[
        Optional[list[int]],
        None,
    ]

    StoryRestrictionsEnabled: Symbol[
        Optional[list[int]],
        None,
    ]

    GetScenarioBalanceVeneer: Symbol[
        Optional[list[int]],
        None,
    ]

    FadeToBlack: Symbol[
        Optional[list[int]],
        None,
    ]

    SetDungeonEscapeFields: Symbol[
        Optional[list[int]],
        None,
    ]

    GetSuccessfulExitTracker: Symbol[
        Optional[list[int]],
        None,
    ]

    GetAndStoreButtonInput: Symbol[
        Optional[list[int]],
        None,
    ]

    CheckTouchscreenArea: Symbol[
        Optional[list[int]],
        None,
    ]

    GetTrapInfo: Symbol[
        Optional[list[int]],
        None,
    ]

    GetItemInfo: Symbol[
        Optional[list[int]],
        None,
    ]

    GetTileAtEntity: Symbol[
        Optional[list[int]],
        None,
    ]

    UpdateEntityPixelPos: Symbol[
        Optional[list[int]],
        None,
    ]

    SetEntityPixelPosXY: Symbol[
        Optional[list[int]],
        None,
    ]

    IncrementEntityPixelPosXY: Symbol[
        Optional[list[int]],
        None,
    ]

    CreateEnemyEntity: Symbol[
        Optional[list[int]],
        None,
    ]

    SpawnTrap: Symbol[
        Optional[list[int]],
        None,
    ]

    SpawnItemEntity: Symbol[
        Optional[list[int]],
        None,
    ]

    ShouldMinimapDisplayEntity: Symbol[
        Optional[list[int]],
        None,
    ]

    ShouldDisplayEntity: Symbol[
        Optional[list[int]],
        None,
    ]

    ShouldDisplayEntityWrapper: Symbol[
        Optional[list[int]],
        None,
    ]

    CanSeeTarget: Symbol[
        Optional[list[int]],
        None,
    ]

    CanTargetEntity: Symbol[
        Optional[list[int]],
        None,
    ]

    IsValidTargetEntity: Symbol[
        Optional[list[int]],
        None,
    ]

    CanSeePosition: Symbol[
        Optional[list[int]],
        None,
    ]

    CanTargetPosition: Symbol[
        Optional[list[int]],
        None,
    ]

    PopulateActiveMonsterPtrs: Symbol[
        Optional[list[int]],
        None,
    ]

    GetTeamMemberIndex: Symbol[
        Optional[list[int]],
        None,
    ]

    SubstitutePlaceholderStringTags: Symbol[
        Optional[list[int]],
        None,
    ]

    UpdateMapSurveyorFlag: Symbol[
        Optional[list[int]],
        None,
    ]

    PointCameraToMonster: Symbol[
        Optional[list[int]],
        None,
    ]

    UpdateCamera: Symbol[
        Optional[list[int]],
        None,
    ]

    ItemIsActive: Symbol[
        Optional[list[int]],
        None,
    ]

    GetVisibilityRange: Symbol[
        Optional[list[int]],
        None,
    ]

    RevealWholeFloor: Symbol[
        Optional[list[int]],
        None,
    ]

    PlayEffectAnimationEntity: Symbol[
        Optional[list[int]],
        None,
    ]

    PlayEffectAnimationPos: Symbol[
        Optional[list[int]],
        None,
    ]

    PlayEffectAnimationPixelPos: Symbol[
        Optional[list[int]],
        None,
    ]

    AnimationDelayOrSomething: Symbol[
        Optional[list[int]],
        None,
    ]

    UpdateStatusIconFlags: Symbol[
        Optional[list[int]],
        None,
    ]

    PlayQuestionMarkEffect: Symbol[
        Optional[list[int]],
        None,
    ]

    PlayExclamationPointEffect: Symbol[
        Optional[list[int]],
        None,
    ]

    PlayEffectAnimation0x171Full: Symbol[
        Optional[list[int]],
        None,
    ]

    PlayEffectAnimation0x171: Symbol[
        Optional[list[int]],
        None,
    ]

    PlayParalysisEffect: Symbol[
        Optional[list[int]],
        None,
    ]

    PlayEffectAnimationEntityStandard: Symbol[
        Optional[list[int]],
        None,
    ]

    PlaySpeedUpEffect: Symbol[
        Optional[list[int]],
        None,
    ]

    PlaySpeedDownEffect: Symbol[
        Optional[list[int]],
        None,
    ]

    ShowPpRestoreEffect: Symbol[
        Optional[list[int]],
        None,
    ]

    PlayOffensiveStatDownEffect: Symbol[
        Optional[list[int]],
        None,
    ]

    PlayDefensiveStatDownEffect: Symbol[
        Optional[list[int]],
        None,
    ]

    PlayOffensiveStatUpEffect: Symbol[
        Optional[list[int]],
        None,
    ]

    PlayDefensiveStatUpEffect: Symbol[
        Optional[list[int]],
        None,
    ]

    PlayOffensiveStatMultiplierUpEffect: Symbol[
        Optional[list[int]],
        None,
    ]

    PlayOffensiveStatMultiplierDownEffect: Symbol[
        Optional[list[int]],
        None,
    ]

    PlayDefensiveStatMultiplierUpEffect: Symbol[
        Optional[list[int]],
        None,
    ]

    PlayDefensiveStatMultiplierDownEffect: Symbol[
        Optional[list[int]],
        None,
    ]

    PlayHitChanceUpEffect: Symbol[
        Optional[list[int]],
        None,
    ]

    PlayHitChanceDownEffect: Symbol[
        Optional[list[int]],
        None,
    ]

    PlaySeByIdIfShouldDisplayEntity: Symbol[
        Optional[list[int]],
        None,
    ]

    ShouldDisplayEntityAdvanced: Symbol[
        Optional[list[int]],
        None,
    ]

    PlayEffectAnimation0x1A9: Symbol[
        Optional[list[int]],
        None,
    ]

    PlayEffectAnimation0x29: Symbol[
        Optional[list[int]],
        None,
    ]

    PlayEffectAnimation0x18E: Symbol[
        Optional[list[int]],
        None,
    ]

    LoadMappaFileAttributes: Symbol[
        Optional[list[int]],
        None,
    ]

    GetRandomTrapId: Symbol[
        Optional[list[int]],
        None,
    ]

    GetItemIdToSpawn: Symbol[
        Optional[list[int]],
        None,
    ]

    CopySpawnEntriesMaster: Symbol[
        Optional[list[int]],
        None,
    ]

    MonsterSpawnListPartialCopy: Symbol[
        Optional[list[int]],
        None,
    ]

    IsOnMonsterSpawnList: Symbol[
        Optional[list[int]],
        None,
    ]

    GetMonsterIdToSpawn: Symbol[
        Optional[list[int]],
        None,
    ]

    GetMonsterLevelToSpawn: Symbol[
        Optional[list[int]],
        None,
    ]

    AllocTopScreenStatus: Symbol[
        Optional[list[int]],
        None,
    ]

    FreeTopScreenStatus: Symbol[
        Optional[list[int]],
        None,
    ]

    InitializeTeamStats: Symbol[
        Optional[list[int]],
        None,
    ]

    UpdateTeamStatsWrapper: Symbol[
        Optional[list[int]],
        None,
    ]

    FreeTeamStatsWrapper: Symbol[
        Optional[list[int]],
        None,
    ]

    DisplayTeamStatsSprite: Symbol[
        Optional[list[int]],
        None,
    ]

    AssignTopScreenHandlers: Symbol[
        Optional[list[int]],
        None,
    ]

    HandleTopScreenFades: Symbol[
        Optional[list[int]],
        None,
    ]

    FreeTopScreen: Symbol[
        Optional[list[int]],
        None,
    ]

    GetDirectionTowardsPosition: Symbol[
        Optional[list[int]],
        None,
    ]

    GetChebyshevDistance: Symbol[
        Optional[list[int]],
        None,
    ]

    IsPositionActuallyInSight: Symbol[
        Optional[list[int]],
        None,
    ]

    IsPositionInSight: Symbol[
        Optional[list[int]],
        None,
    ]

    IsPositionWithinTwoTiles: Symbol[
        Optional[list[int]],
        None,
    ]

    GetLeader: Symbol[
        Optional[list[int]],
        None,
    ]

    GetLeaderMonster: Symbol[
        Optional[list[int]],
        None,
    ]

    GetRandomTile: Symbol[
        Optional[list[int]],
        None,
    ]

    FindNearbyUnoccupiedTile: Symbol[
        Optional[list[int]],
        None,
    ]

    FindClosestUnoccupiedTileWithin2: Symbol[
        Optional[list[int]],
        None,
    ]

    FindFarthestUnoccupiedTileWithin2: Symbol[
        Optional[list[int]],
        None,
    ]

    FindUnoccupiedTileWithin3: Symbol[
        Optional[list[int]],
        None,
    ]

    TickStatusTurnCounter: Symbol[
        Optional[list[int]],
        None,
    ]

    AdvanceFrame: Symbol[
        Optional[list[int]],
        None,
    ]

    UnkMapRelatedFunc: Symbol[
        Optional[list[int]],
        None,
    ]

    DisplayAnimatedNumbers: Symbol[
        Optional[list[int]],
        None,
    ]

    SetDungeonRngPreseed23Bit: Symbol[
        Optional[list[int]],
        None,
    ]

    GenerateDungeonRngSeed: Symbol[
        Optional[list[int]],
        None,
    ]

    GetDungeonRngPreseed: Symbol[
        Optional[list[int]],
        None,
    ]

    SetDungeonRngPreseed: Symbol[
        Optional[list[int]],
        None,
    ]

    InitDungeonRng: Symbol[
        Optional[list[int]],
        None,
    ]

    DungeonRand16Bit: Symbol[
        Optional[list[int]],
        None,
    ]

    DungeonRandInt: Symbol[
        Optional[list[int]],
        None,
    ]

    DungeonRandRange: Symbol[
        Optional[list[int]],
        None,
    ]

    DungeonRandOutcome: Symbol[
        Optional[list[int]],
        None,
    ]

    CalcStatusDuration: Symbol[
        Optional[list[int]],
        None,
    ]

    DungeonRngUnsetSecondary: Symbol[
        Optional[list[int]],
        None,
    ]

    DungeonRngSetSecondary: Symbol[
        Optional[list[int]],
        None,
    ]

    DungeonRngSetPrimary: Symbol[
        Optional[list[int]],
        None,
    ]

    PlaySeByIdIfNotSilence: Symbol[
        Optional[list[int]],
        None,
    ]

    MusicTableIdxToMusicId: Symbol[
        Optional[list[int]],
        None,
    ]

    ChangeDungeonMusic: Symbol[
        Optional[list[int]],
        None,
    ]

    TrySwitchPlace: Symbol[
        Optional[list[int]],
        None,
    ]

    ResetLeaderActionFields: Symbol[
        Optional[list[int]],
        None,
    ]

    SetLeaderActionFields: Symbol[
        Optional[list[int]],
        None,
    ]

    ClearMonsterActionFields: Symbol[
        Optional[list[int]],
        None,
    ]

    SetMonsterActionFields: Symbol[
        Optional[list[int]],
        None,
    ]

    SetActionPassTurnOrWalk: Symbol[
        Optional[list[int]],
        None,
    ]

    GetItemToUseByIndex: Symbol[
        Optional[list[int]],
        None,
    ]

    GetItemToUse: Symbol[
        Optional[list[int]],
        None,
    ]

    GetItemAction: Symbol[
        Optional[list[int]],
        None,
    ]

    RemoveUsedItem: Symbol[
        Optional[list[int]],
        None,
    ]

    AddDungeonSubMenuOption: Symbol[
        Optional[list[int]],
        None,
    ]

    DisableDungeonSubMenuOption: Symbol[
        Optional[list[int]],
        None,
    ]

    SetActionRegularAttack: Symbol[
        Optional[list[int]],
        None,
    ]

    SetActionStruggle: Symbol[
        Optional[list[int]],
        None,
    ]

    SetActionUseMovePlayer: Symbol[
        Optional[list[int]],
        None,
    ]

    SetActionUseMoveAi: Symbol[
        Optional[list[int]],
        None,
    ]

    RunFractionalTurn: Symbol[
        Optional[list[int]],
        None,
    ]

    RunLeaderTurn: Symbol[
        Optional[list[int]],
        None,
    ]

    TrySpawnMonsterAndActivatePlusMinus: Symbol[
        Optional[list[int]],
        None,
    ]

    IsFloorOver: Symbol[
        Optional[list[int]],
        None,
    ]

    DecrementWindCounter: Symbol[
        Optional[list[int]],
        None,
    ]

    IsDungeonEndReasonFailure: Symbol[
        Optional[list[int]],
        None,
    ]

    SetForcedLossReason: Symbol[
        Optional[list[int]],
        None,
    ]

    GetForcedLossReason: Symbol[
        Optional[list[int]],
        None,
    ]

    BindTrapToTile: Symbol[
        Optional[list[int]],
        None,
    ]

    AreLateGameTrapsEnabledWrapper: Symbol[
        Optional[list[int]],
        None,
    ]

    SpawnTraps: Symbol[
        Optional[list[int]],
        None,
    ]

    SpawnEnemyTrapAtPos: Symbol[
        Optional[list[int]],
        None,
    ]

    PrepareTrapperTrap: Symbol[
        Optional[list[int]],
        None,
    ]

    CanLayTrap: Symbol[
        Optional[list[int]],
        None,
    ]

    TrySpawnTrap: Symbol[
        Optional[list[int]],
        None,
    ]

    TrySpawnTrapperTrap: Symbol[
        Optional[list[int]],
        None,
    ]

    TryRemoveTrap: Symbol[
        Optional[list[int]],
        None,
    ]

    TryRevealAttackedTrap: Symbol[
        Optional[list[int]],
        None,
    ]

    SubstitutePlaceholderTrapTags2: Symbol[
        Optional[list[int]],
        None,
    ]

    SubstitutePlaceholderTrapTags: Symbol[
        Optional[list[int]],
        None,
    ]

    TryTriggerTrap: Symbol[
        Optional[list[int]],
        None,
    ]

    ApplyMudTrapEffect: Symbol[
        Optional[list[int]],
        None,
    ]

    ApplyStickyTrapEffect: Symbol[
        Optional[list[int]],
        None,
    ]

    ApplyGrimyTrapEffect: Symbol[
        Optional[list[int]],
        None,
    ]

    ApplyPitfallTrapEffect: Symbol[
        Optional[list[int]],
        None,
    ]

    ApplySummonTrapEffect: Symbol[
        Optional[list[int]],
        None,
    ]

    ApplyPpZeroTrapEffect: Symbol[
        Optional[list[int]],
        None,
    ]

    ApplyPokemonTrapEffect: Symbol[
        Optional[list[int]],
        None,
    ]

    ApplyTripTrapEffect: Symbol[
        Optional[list[int]],
        None,
    ]

    ApplyStealthRockTrapEffect: Symbol[
        Optional[list[int]],
        None,
    ]

    ApplyToxicSpikesTrapEffect: Symbol[
        Optional[list[int]],
        None,
    ]

    ApplyRandomTrapEffect: Symbol[
        Optional[list[int]],
        None,
    ]

    ApplyGrudgeTrapEffect: Symbol[
        Optional[list[int]],
        None,
    ]

    ApplyTrapEffect: Symbol[
        Optional[list[int]],
        None,
    ]

    SpawnMonstersAroundPos: Symbol[
        Optional[list[int]],
        None,
    ]

    RevealTrapsNearby: Symbol[
        Optional[list[int]],
        None,
    ]

    ShouldRunMonsterAi: Symbol[
        Optional[list[int]],
        None,
    ]

    DebugRecruitingEnabled: Symbol[
        Optional[list[int]],
        None,
    ]

    TryActivateIqBooster: Symbol[
        Optional[list[int]],
        None,
    ]

    IsBehaviorLoneOutlaw: Symbol[
        Optional[list[int]],
        None,
    ]

    IsSecretBazaarNpcBehavior: Symbol[
        Optional[list[int]],
        None,
    ]

    GetLeaderAction: Symbol[
        Optional[list[int]],
        None,
    ]

    GetLeaderActionId: Symbol[
        Optional[list[int]],
        None,
    ]

    GetEntityTouchscreenArea: Symbol[
        Optional[list[int]],
        None,
    ]

    SetLeaderAction: Symbol[
        Optional[list[int]],
        None,
    ]

    ShouldLeaderKeepRunning: Symbol[
        Optional[list[int]],
        None,
    ]

    CheckLeaderTile: Symbol[
        Optional[list[int]],
        None,
    ]

    ChangeLeader: Symbol[
        Optional[list[int]],
        None,
    ]

    GetPlayerGender: Symbol[
        Optional[list[int]],
        None,
    ]

    HandleHeldItemSwaps: Symbol[
        Optional[list[int]],
        None,
    ]

    UseSingleUseItemWrapper: Symbol[
        Optional[list[int]],
        None,
    ]

    UseSingleUseItem: Symbol[
        Optional[list[int]],
        None,
    ]

    UseThrowableItem: Symbol[
        Optional[list[int]],
        None,
    ]

    ResetDamageData: Symbol[
        Optional[list[int]],
        None,
    ]

    FreeLoadedAttackSpriteAndMore: Symbol[
        Optional[list[int]],
        None,
    ]

    SetAndLoadCurrentAttackAnimation: Symbol[
        Optional[list[int]],
        None,
    ]

    ClearLoadedAttackSprite: Symbol[
        Optional[list[int]],
        None,
    ]

    GetLoadedAttackSpriteId: Symbol[
        Optional[list[int]],
        None,
    ]

    DungeonGetTotalSpriteFileSize: Symbol[
        Optional[list[int]],
        None,
    ]

    DungeonGetSpriteIndex: Symbol[
        Optional[list[int]],
        None,
    ]

    JoinedAtRangeCheck2Veneer: Symbol[
        Optional[list[int]],
        None,
    ]

    FloorNumberIsEven: Symbol[
        Optional[list[int]],
        None,
    ]

    GetKecleonIdToSpawnByFloor: Symbol[
        Optional[list[int]],
        None,
    ]

    StoreSpriteFileIndexBothGenders: Symbol[
        Optional[list[int]],
        None,
    ]

    LoadMonsterSpriteInner: Symbol[
        Optional[list[int]],
        None,
    ]

    SwapMonsterWanFileIndex: Symbol[
        Optional[list[int]],
        None,
    ]

    LoadMonsterSprite: Symbol[
        Optional[list[int]],
        None,
    ]

    DeleteMonsterSpriteFile: Symbol[
        Optional[list[int]],
        None,
    ]

    DeleteAllMonsterSpriteFiles: Symbol[
        Optional[list[int]],
        None,
    ]

    EuFaintCheck: Symbol[
        Optional[list[int]],
        None,
    ]

    HandleFaint: Symbol[
        Optional[list[int]],
        None,
    ]

    MoveMonsterToPos: Symbol[
        Optional[list[int]],
        None,
    ]

    CreateMonsterSummaryFromEntity: Symbol[
        Optional[list[int]],
        None,
    ]

    UpdateAiTargetPos: Symbol[
        Optional[list[int]],
        None,
    ]

    SetMonsterTypeAndAbility: Symbol[
        Optional[list[int]],
        None,
    ]

    TryActivateSlowStart: Symbol[
        Optional[list[int]],
        None,
    ]

    TryActivateArtificialWeatherAbilities: Symbol[
        Optional[list[int]],
        None,
    ]

    GetMonsterApparentId: Symbol[
        Optional[list[int]],
        None,
    ]

    TryActivateTraceAndColorChange: Symbol[
        Optional[list[int]],
        None,
    ]

    DefenderAbilityIsActive: Symbol[
        Optional[list[int]],
        None,
    ]

    IsMonster: Symbol[
        Optional[list[int]],
        None,
    ]

    TryActivateConversion2: Symbol[
        Optional[list[int]],
        None,
    ]

    TryActivateTruant: Symbol[
        Optional[list[int]],
        None,
    ]

    TryPointCameraToMonster: Symbol[
        Optional[list[int]],
        None,
    ]

    ReevaluateSnatchMonster: Symbol[
        Optional[list[int]],
        None,
    ]

    GetRandomExplorerMazeMonster: Symbol[
        Optional[list[int]],
        None,
    ]

    RestorePpAllMovesSetFlags: Symbol[
        Optional[list[int]],
        None,
    ]

    CheckTeamMemberIdxVeneer: Symbol[
        Optional[list[int]],
        None,
    ]

    IsMonsterIdInNormalRangeVeneer: Symbol[
        Optional[list[int]],
        None,
    ]

    BoostIQ: Symbol[
        Optional[list[int]],
        None,
    ]

    ShouldMonsterHeadToStairs: Symbol[
        Optional[list[int]],
        None,
    ]

    MewSpawnCheck: Symbol[
        Optional[list[int]],
        None,
    ]

    TryEndStatusWithAbility: Symbol[
        Optional[list[int]],
        None,
    ]

    ExclusiveItemEffectIsActive: Symbol[
        Optional[list[int]],
        None,
    ]

    GetTeamMemberWithIqSkill: Symbol[
        Optional[list[int]],
        None,
    ]

    TeamMemberHasEnabledIqSkill: Symbol[
        Optional[list[int]],
        None,
    ]

    TeamLeaderIqSkillIsEnabled: Symbol[
        Optional[list[int]],
        None,
    ]

    CountMovesOutOfPp: Symbol[
        Optional[list[int]],
        None,
    ]

    HasSuperEffectiveMoveAgainstUser: Symbol[
        Optional[list[int]],
        None,
    ]

    TryEatItem: Symbol[
        Optional[list[int]],
        None,
    ]

    SetDecoyAiTracker: Symbol[
        Optional[list[int]],
        None,
    ]

    CheckSpawnThreshold: Symbol[
        Optional[list[int]],
        None,
    ]

    HasLowHealth: Symbol[
        Optional[list[int]],
        None,
    ]

    AreEntitiesAdjacent: Symbol[
        Optional[list[int]],
        None,
    ]

    IsHero: Symbol[
        Optional[list[int]],
        None,
    ]

    FindMoveOnMonster: Symbol[
        Optional[list[int]],
        None,
    ]

    DoesMonsterHaveMove: Symbol[
        Optional[list[int]],
        None,
    ]

    IsSpecialStoryAllyOrClient: Symbol[
        Optional[list[int]],
        None,
    ]

    ResetTriggerFlags: Symbol[
        Optional[list[int]],
        None,
    ]

    IsSpecialStoryAlly: Symbol[
        Optional[list[int]],
        None,
    ]

    IsExperienceLocked: Symbol[
        Optional[list[int]],
        None,
    ]

    FindMonsterWithBehavior: Symbol[
        Optional[list[int]],
        None,
    ]

    IsMonsterLoneOutlaw: Symbol[
        Optional[list[int]],
        None,
    ]

    IsSecretBazaarNpc: Symbol[
        Optional[list[int]],
        None,
    ]

    IsTeamMemberOnFirstTurnInFixedRoom: Symbol[
        Optional[list[int]],
        None,
    ]

    InitOtherMonsterData: Symbol[
        Optional[list[int]],
        None,
    ]

    InitEnemySpawnStats: Symbol[
        Optional[list[int]],
        None,
    ]

    InitEnemyStatsAndMoves: Symbol[
        Optional[list[int]],
        None,
    ]

    SpawnTeam: Symbol[
        Optional[list[int]],
        None,
    ]

    SpawnInitialMonsters: Symbol[
        Optional[list[int]],
        None,
    ]

    SpawnMonster: Symbol[
        Optional[list[int]],
        None,
    ]

    InitTeamMember: Symbol[
        Optional[list[int]],
        None,
    ]

    InitMonster: Symbol[
        Optional[list[int]],
        None,
    ]

    SubInitMonster: Symbol[
        Optional[list[int]],
        None,
    ]

    MarkShopkeeperSpawn: Symbol[
        Optional[list[int]],
        None,
    ]

    SpawnShopkeepers: Symbol[
        Optional[list[int]],
        None,
    ]

    GetMaxHpAtLevel: Symbol[
        Optional[list[int]],
        None,
    ]

    GetOffensiveStatAtLevel: Symbol[
        Optional[list[int]],
        None,
    ]

    GetDefensiveStatAtLevel: Symbol[
        Optional[list[int]],
        None,
    ]

    GetOutlawSpawnData: Symbol[
        Optional[list[int]],
        None,
    ]

    ExecuteMonsterAction: Symbol[
        Optional[list[int]],
        None,
    ]

    TryActivateFlashFireOnAllMonsters: Symbol[
        Optional[list[int]],
        None,
    ]

    HasStatusThatPreventsActing: Symbol[
        Optional[list[int]],
        None,
    ]

    GetMobilityTypeCheckSlip: Symbol[
        Optional[list[int]],
        None,
    ]

    GetMobilityTypeCheckSlipAndFloating: Symbol[
        Optional[list[int]],
        None,
    ]

    IsInvalidSpawnTile: Symbol[
        Optional[list[int]],
        None,
    ]

    GetMobilityTypeAfterIqSkills: Symbol[
        Optional[list[int]],
        None,
    ]

    CanMoveThroughWalls: Symbol[
        Optional[list[int]],
        None,
    ]

    CannotStandOnTile: Symbol[
        Optional[list[int]],
        None,
    ]

    CalcSpeedStage: Symbol[
        Optional[list[int]],
        None,
    ]

    CalcSpeedStageWrapper: Symbol[
        Optional[list[int]],
        None,
    ]

    GetNumberOfAttacks: Symbol[
        Optional[list[int]],
        None,
    ]

    GetMonsterDisplayNameType: Symbol[
        Optional[list[int]],
        None,
    ]

    GetMonsterName: Symbol[
        Optional[list[int]],
        None,
    ]

    SprintfStatic: Symbol[
        Optional[list[int]],
        None,
    ]

    SetPreprocessorArgsStringToName: Symbol[
        Optional[list[int]],
        None,
    ]

    IsMonsterDrowsy: Symbol[
        Optional[list[int]],
        None,
    ]

    MonsterHasNonvolatileNonsleepStatus: Symbol[
        Optional[list[int]],
        None,
    ]

    MonsterHasImmobilizingStatus: Symbol[
        Optional[list[int]],
        None,
    ]

    MonsterHasAttackInterferingStatus: Symbol[
        Optional[list[int]],
        None,
    ]

    MonsterHasSkillInterferingStatus: Symbol[
        Optional[list[int]],
        None,
    ]

    MonsterHasLeechSeedStatus: Symbol[
        Optional[list[int]],
        None,
    ]

    MonsterHasWhifferStatus: Symbol[
        Optional[list[int]],
        None,
    ]

    IsMonsterVisuallyImpaired: Symbol[
        Optional[list[int]],
        None,
    ]

    IsMonsterMuzzled: Symbol[
        Optional[list[int]],
        None,
    ]

    MonsterHasMiracleEyeStatus: Symbol[
        Optional[list[int]],
        None,
    ]

    MonsterHasNegativeStatus: Symbol[
        Optional[list[int]],
        None,
    ]

    IsMonsterSleeping: Symbol[
        Optional[list[int]],
        None,
    ]

    MonsterHasQuarterHp: Symbol[
        Optional[list[int]],
        None,
    ]

    CheckVariousStatuses2: Symbol[
        Optional[list[int]],
        None,
    ]

    CheckVariousConditions: Symbol[
        Optional[list[int]],
        None,
    ]

    CheckVariousStatuses: Symbol[
        Optional[list[int]],
        None,
    ]

    MonsterCannotAttack: Symbol[
        Optional[list[int]],
        None,
    ]

    CanMonsterMoveInDirection: Symbol[
        Optional[list[int]],
        None,
    ]

    GetDirectionalMobilityType: Symbol[
        Optional[list[int]],
        None,
    ]

    CanMonsterMoveOrSwapWithAllyInAnyDirection: Symbol[
        Optional[list[int]],
        None,
    ]

    CanMonsterMoveOrSwapWithAllyInDirection: Symbol[
        Optional[list[int]],
        None,
    ]

    CanAttackInDirection: Symbol[
        Optional[list[int]],
        None,
    ]

    CanAiMonsterMoveInDirection: Symbol[
        Optional[list[int]],
        None,
    ]

    IsAtJunction: Symbol[
        Optional[list[int]],
        None,
    ]

    ShouldAvoidFirstHit: Symbol[
        Optional[list[int]],
        None,
    ]

    ShouldMonsterRunAway: Symbol[
        Optional[list[int]],
        None,
    ]

    ShouldMonsterRunAwayAndShowEffect: Symbol[
        Optional[list[int]],
        None,
    ]

    DisplayRunAwayIfTriggered: Symbol[
        Optional[list[int]],
        None,
    ]

    GetTreatmentBetweenMonsters: Symbol[
        Optional[list[int]],
        None,
    ]

    GetTreatmentBetweenMonstersIgnoreStatus: Symbol[
        Optional[list[int]],
        None,
    ]

    SafeguardIsActive: Symbol[
        Optional[list[int]],
        None,
    ]

    LeafGuardIsActive: Symbol[
        Optional[list[int]],
        None,
    ]

    IsProtectedFromStatDrops: Symbol[
        Optional[list[int]],
        None,
    ]

    NoGastroAcidStatus: Symbol[
        Optional[list[int]],
        None,
    ]

    AbilityIsActive: Symbol[
        Optional[list[int]],
        None,
    ]

    AbilityIsActiveVeneer: Symbol[
        Optional[list[int]],
        None,
    ]

    OtherMonsterAbilityIsActive: Symbol[
        Optional[list[int]],
        None,
    ]

    LevitateIsActive: Symbol[
        Optional[list[int]],
        None,
    ]

    MonsterIsType: Symbol[
        Optional[list[int]],
        None,
    ]

    IsTypeAffectedByGravity: Symbol[
        Optional[list[int]],
        None,
    ]

    HasTypeAffectedByGravity: Symbol[
        Optional[list[int]],
        None,
    ]

    CanSeeInvisibleMonsters: Symbol[
        Optional[list[int]],
        None,
    ]

    IsTacticSet: Symbol[
        Optional[list[int]],
        None,
    ]

    HasDropeyeStatus: Symbol[
        Optional[list[int]],
        None,
    ]

    IqSkillIsEnabled: Symbol[
        Optional[list[int]],
        None,
    ]

    UpdateIqSkills: Symbol[
        Optional[list[int]],
        None,
    ]

    CanSeeTeammate: Symbol[
        Optional[list[int]],
        None,
    ]

    GetMoveTypeForMonster: Symbol[
        Optional[list[int]],
        None,
    ]

    GetMovePower: Symbol[
        Optional[list[int]],
        None,
    ]

    MonsterCanThrowItems: Symbol[
        Optional[list[int]],
        None,
    ]

    UpdateStateFlags: Symbol[
        Optional[list[int]],
        None,
    ]

    IsProtectedFromNegativeStatus: Symbol[
        Optional[list[int]],
        None,
    ]

    AddExpSpecial: Symbol[
        Optional[list[int]],
        None,
    ]

    EnemyEvolution: Symbol[
        Optional[list[int]],
        None,
    ]

    LevelUpItemEffect: Symbol[
        Optional[list[int]],
        None,
    ]

    TryDecreaseLevel: Symbol[
        Optional[list[int]],
        None,
    ]

    LevelUp: Symbol[
        Optional[list[int]],
        None,
    ]

    DungeonTmLearnMove: Symbol[
        Optional[list[int]],
        None,
    ]

    GetMonsterMoves: Symbol[
        Optional[list[int]],
        None,
    ]

    EvolveMonster: Symbol[
        Optional[list[int]],
        None,
    ]

    ChangeMonsterAnimation: Symbol[
        Optional[list[int]],
        None,
    ]

    GetIdleAnimationId: Symbol[
        Optional[list[int]],
        None,
    ]

    DetermineAllMonsterShadow: Symbol[
        Optional[list[int]],
        None,
    ]

    DetermineMonsterShadow: Symbol[
        Optional[list[int]],
        None,
    ]

    DisplayActions: Symbol[
        Optional[list[int]],
        None,
    ]

    CheckNonLeaderTile: Symbol[
        Optional[list[int]],
        None,
    ]

    EndNegativeStatusCondition: Symbol[
        Optional[list[int]],
        None,
    ]

    EndNegativeStatusConditionWrapper: Symbol[
        Optional[list[int]],
        None,
    ]

    TransferNegativeStatusCondition: Symbol[
        Optional[list[int]],
        None,
    ]

    EndSleepClassStatus: Symbol[
        Optional[list[int]],
        None,
    ]

    EndBurnClassStatus: Symbol[
        Optional[list[int]],
        None,
    ]

    EndFrozenClassStatus: Symbol[
        Optional[list[int]],
        None,
    ]

    EndCringeClassStatus: Symbol[
        Optional[list[int]],
        None,
    ]

    EndReflectClassStatus: Symbol[
        Optional[list[int]],
        None,
    ]

    TryRemoveSnatchedMonsterFromDungeonStruct: Symbol[
        Optional[list[int]],
        None,
    ]

    EndCurseClassStatus: Symbol[
        Optional[list[int]],
        None,
    ]

    EndLeechSeedClassStatus: Symbol[
        Optional[list[int]],
        None,
    ]

    EndSureShotClassStatus: Symbol[
        Optional[list[int]],
        None,
    ]

    EndInvisibleClassStatus: Symbol[
        Optional[list[int]],
        None,
    ]

    EndBlinkerClassStatus: Symbol[
        Optional[list[int]],
        None,
    ]

    EndMuzzledStatus: Symbol[
        Optional[list[int]],
        None,
    ]

    EndMiracleEyeStatus: Symbol[
        Optional[list[int]],
        None,
    ]

    EndMagnetRiseStatus: Symbol[
        Optional[list[int]],
        None,
    ]

    TransferNegativeBlinkerClassStatus: Symbol[
        Optional[list[int]],
        None,
    ]

    TryEndPetrifiedOrSleepStatus: Symbol[
        Optional[list[int]],
        None,
    ]

    EndFrozenStatus: Symbol[
        Optional[list[int]],
        None,
    ]

    EndProtectStatus: Symbol[
        Optional[list[int]],
        None,
    ]

    TryRestoreRoostTyping: Symbol[
        Optional[list[int]],
        None,
    ]

    TryTriggerMonsterHouse: Symbol[
        Optional[list[int]],
        None,
    ]

    ShouldMonsterFollowLeader: Symbol[
        Optional[list[int]],
        None,
    ]

    GetLeaderIfVisible: Symbol[
        Optional[list[int]],
        None,
    ]

    RunMonsterAi: Symbol[
        Optional[list[int]],
        None,
    ]

    ApplyDamageAndEffects: Symbol[
        Optional[list[int]],
        None,
    ]

    ApplyDamage: Symbol[
        Optional[list[int]],
        None,
    ]

    AftermathCheck: Symbol[
        Optional[list[int]],
        None,
    ]

    GetTypeMatchupBothTypes: Symbol[
        Optional[list[int]],
        None,
    ]

    ScrappyShouldActivate: Symbol[
        Optional[list[int]],
        None,
    ]

    IsTypeIneffectiveAgainstGhost: Symbol[
        Optional[list[int]],
        None,
    ]

    GhostImmunityIsActive: Symbol[
        Optional[list[int]],
        None,
    ]

    GetTypeMatchup: Symbol[
        Optional[list[int]],
        None,
    ]

    CalcTypeBasedDamageEffects: Symbol[
        Optional[list[int]],
        None,
    ]

    WeightWeakTypePicker: Symbol[
        Optional[list[int]],
        None,
    ]

    CalcDamage: Symbol[
        Optional[list[int]],
        None,
    ]

    ApplyDamageAndEffectsWrapper: Symbol[
        Optional[list[int]],
        None,
    ]

    CalcRecoilDamageFixed: Symbol[
        Optional[list[int]],
        None,
    ]

    CalcDamageFixed: Symbol[
        Optional[list[int]],
        None,
    ]

    CalcDamageFixedNoCategory: Symbol[
        Optional[list[int]],
        None,
    ]

    CalcDamageFixedWrapper: Symbol[
        Optional[list[int]],
        None,
    ]

    UpdateShopkeeperModeAfterAttack: Symbol[
        Optional[list[int]],
        None,
    ]

    UpdateShopkeeperModeAfterTrap: Symbol[
        Optional[list[int]],
        None,
    ]

    ResetDamageCalcDiagnostics: Symbol[
        Optional[list[int]],
        None,
    ]

    SpecificRecruitCheck: Symbol[
        Optional[list[int]],
        None,
    ]

    RecruitCheck: Symbol[
        Optional[list[int]],
        None,
    ]

    TryRecruit: Symbol[
        Optional[list[int]],
        None,
    ]

    TrySpawnMonsterAndTickSpawnCounter: Symbol[
        Optional[list[int]],
        None,
    ]

    AiDecideUseItem: Symbol[
        Optional[list[int]],
        None,
    ]

    GetPossibleAiThrownItemDirections: Symbol[
        Optional[list[int]],
        None,
    ]

    GetPossibleAiArcItemTargets: Symbol[
        Optional[list[int]],
        None,
    ]

    TryNonLeaderItemPickUp: Symbol[
        Optional[list[int]],
        None,
    ]

    GetExclusiveItemWithEffectFromBag: Symbol[
        Optional[list[int]],
        None,
    ]

    AuraBowIsActive: Symbol[
        Optional[list[int]],
        None,
    ]

    ExclusiveItemOffenseBoost: Symbol[
        Optional[list[int]],
        None,
    ]

    ExclusiveItemDefenseBoost: Symbol[
        Optional[list[int]],
        None,
    ]

    TeamMemberHasItemActive: Symbol[
        Optional[list[int]],
        None,
    ]

    TeamMemberHasExclusiveItemEffectActive: Symbol[
        Optional[list[int]],
        None,
    ]

    FindDirectionOfAdjacentMonsterWithItem: Symbol[
        Optional[list[int]],
        None,
    ]

    TrySpawnEnemyItemDrop: Symbol[
        Optional[list[int]],
        None,
    ]

    TickNoSlipCap: Symbol[
        Optional[list[int]],
        None,
    ]

    ActivateEndOfTurnEffects: Symbol[
        Optional[list[int]],
        None,
    ]

    TickStatusAndHealthRegen: Symbol[
        Optional[list[int]],
        None,
    ]

    InflictSleepStatusSingle: Symbol[
        Optional[list[int]],
        None,
    ]

    TryInflictSleepStatus: Symbol[
        Optional[list[int]],
        None,
    ]

    IsProtectedFromSleepClassStatus: Symbol[
        Optional[list[int]],
        None,
    ]

    TryInflictNightmareStatus: Symbol[
        Optional[list[int]],
        None,
    ]

    TryInflictNappingStatus: Symbol[
        Optional[list[int]],
        None,
    ]

    TryInflictYawningStatus: Symbol[
        Optional[list[int]],
        None,
    ]

    TryInflictSleeplessStatus: Symbol[
        Optional[list[int]],
        None,
    ]

    TryInflictPausedStatus: Symbol[
        Optional[list[int]],
        None,
    ]

    TryInflictInfatuatedStatus: Symbol[
        Optional[list[int]],
        None,
    ]

    TryInflictBurnStatus: Symbol[
        Optional[list[int]],
        None,
    ]

    TryInflictBurnStatusWholeTeam: Symbol[
        Optional[list[int]],
        None,
    ]

    TryInflictPoisonedStatus: Symbol[
        Optional[list[int]],
        None,
    ]

    TryInflictBadlyPoisonedStatus: Symbol[
        Optional[list[int]],
        None,
    ]

    TryInflictFrozenStatus: Symbol[
        Optional[list[int]],
        None,
    ]

    TryInflictConstrictionStatus: Symbol[
        Optional[list[int]],
        None,
    ]

    TryInflictShadowHoldStatus: Symbol[
        Optional[list[int]],
        None,
    ]

    TryInflictIngrainStatus: Symbol[
        Optional[list[int]],
        None,
    ]

    TryInflictWrappedStatus: Symbol[
        Optional[list[int]],
        None,
    ]

    FreeOtherWrappedMonsters: Symbol[
        Optional[list[int]],
        None,
    ]

    TryInflictPetrifiedStatus: Symbol[
        Optional[list[int]],
        None,
    ]

    LowerOffensiveStat: Symbol[
        Optional[list[int]],
        None,
    ]

    LowerDefensiveStat: Symbol[
        Optional[list[int]],
        None,
    ]

    BoostOffensiveStat: Symbol[
        Optional[list[int]],
        None,
    ]

    BoostDefensiveStat: Symbol[
        Optional[list[int]],
        None,
    ]

    FlashFireShouldActivate: Symbol[
        Optional[list[int]],
        None,
    ]

    ActivateFlashFire: Symbol[
        Optional[list[int]],
        None,
    ]

    ApplyOffensiveStatMultiplier: Symbol[
        Optional[list[int]],
        None,
    ]

    ApplyDefensiveStatMultiplier: Symbol[
        Optional[list[int]],
        None,
    ]

    BoostHitChanceStat: Symbol[
        Optional[list[int]],
        None,
    ]

    LowerHitChanceStat: Symbol[
        Optional[list[int]],
        None,
    ]

    TryInflictCringeStatus: Symbol[
        Optional[list[int]],
        None,
    ]

    TryInflictParalysisStatus: Symbol[
        Optional[list[int]],
        None,
    ]

    BoostSpeed: Symbol[
        Optional[list[int]],
        None,
    ]

    BoostSpeedOneStage: Symbol[
        Optional[list[int]],
        None,
    ]

    LowerSpeed: Symbol[
        Optional[list[int]],
        None,
    ]

    TrySealMove: Symbol[
        Optional[list[int]],
        None,
    ]

    BoostOrLowerSpeed: Symbol[
        Optional[list[int]],
        None,
    ]

    ResetHitChanceStat: Symbol[
        Optional[list[int]],
        None,
    ]

    ExclusiveItemEffectIsActiveWithLogging: Symbol[
        Optional[list[int]],
        None,
    ]

    TryActivateQuickFeet: Symbol[
        Optional[list[int]],
        None,
    ]

    TryInflictTerrifiedStatus: Symbol[
        Optional[list[int]],
        None,
    ]

    TryInflictGrudgeStatus: Symbol[
        Optional[list[int]],
        None,
    ]

    TryInflictConfusedStatus: Symbol[
        Optional[list[int]],
        None,
    ]

    TryInflictCoweringStatus: Symbol[
        Optional[list[int]],
        None,
    ]

    TryRestoreHp: Symbol[
        Optional[list[int]],
        None,
    ]

    TryIncreaseHp: Symbol[
        Optional[list[int]],
        None,
    ]

    RevealItems: Symbol[
        Optional[list[int]],
        None,
    ]

    RevealStairs: Symbol[
        Optional[list[int]],
        None,
    ]

    RevealEnemies: Symbol[
        Optional[list[int]],
        None,
    ]

    TryInflictLeechSeedStatus: Symbol[
        Optional[list[int]],
        None,
    ]

    TryInflictDestinyBondStatus: Symbol[
        Optional[list[int]],
        None,
    ]

    TryInflictSureShotStatus: Symbol[
        Optional[list[int]],
        None,
    ]

    TryInflictWhifferStatus: Symbol[
        Optional[list[int]],
        None,
    ]

    TryInflictSetDamageStatus: Symbol[
        Optional[list[int]],
        None,
    ]

    TryInflictFocusEnergyStatus: Symbol[
        Optional[list[int]],
        None,
    ]

    TryInflictDecoyStatus: Symbol[
        Optional[list[int]],
        None,
    ]

    TryInflictCurseStatus: Symbol[
        Optional[list[int]],
        None,
    ]

    TryInflictSnatchStatus: Symbol[
        Optional[list[int]],
        None,
    ]

    TryInflictTauntStatus: Symbol[
        Optional[list[int]],
        None,
    ]

    TryInflictStockpileStatus: Symbol[
        Optional[list[int]],
        None,
    ]

    TryInflictInvisibleStatus: Symbol[
        Optional[list[int]],
        None,
    ]

    TryInflictPerishSongStatus: Symbol[
        Optional[list[int]],
        None,
    ]

    TryInflictEncoreStatus: Symbol[
        Optional[list[int]],
        None,
    ]

    TryDecreaseBelly: Symbol[
        Optional[list[int]],
        None,
    ]

    TryIncreaseBelly: Symbol[
        Optional[list[int]],
        None,
    ]

    TryInflictMuzzledStatus: Symbol[
        Optional[list[int]],
        None,
    ]

    TryTransform: Symbol[
        Optional[list[int]],
        None,
    ]

    TryInflictMobileStatus: Symbol[
        Optional[list[int]],
        None,
    ]

    TryInflictExposedStatus: Symbol[
        Optional[list[int]],
        None,
    ]

    TryActivateIdentifyCondition: Symbol[
        Optional[list[int]],
        None,
    ]

    TryInflictBlinkerStatus: Symbol[
        Optional[list[int]],
        None,
    ]

    IsBlinded: Symbol[
        Optional[list[int]],
        None,
    ]

    TryInflictCrossEyedStatus: Symbol[
        Optional[list[int]],
        None,
    ]

    TryInflictEyedropStatus: Symbol[
        Optional[list[int]],
        None,
    ]

    TryInflictSlipStatus: Symbol[
        Optional[list[int]],
        None,
    ]

    TryInflictDropeyeStatus: Symbol[
        Optional[list[int]],
        None,
    ]

    RestoreAllMovePP: Symbol[
        Optional[list[int]],
        None,
    ]

    RestoreOneMovePP: Symbol[
        Optional[list[int]],
        None,
    ]

    RestoreRandomMovePP: Symbol[
        Optional[list[int]],
        None,
    ]

    ApplyProteinEffect: Symbol[
        Optional[list[int]],
        None,
    ]

    ApplyCalciumEffect: Symbol[
        Optional[list[int]],
        None,
    ]

    ApplyIronEffect: Symbol[
        Optional[list[int]],
        None,
    ]

    ApplyZincEffect: Symbol[
        Optional[list[int]],
        None,
    ]

    TryInflictLongTossStatus: Symbol[
        Optional[list[int]],
        None,
    ]

    TryInflictPierceStatus: Symbol[
        Optional[list[int]],
        None,
    ]

    TryInflictGastroAcidStatus: Symbol[
        Optional[list[int]],
        None,
    ]

    SetAquaRingHealingCountdownTo4: Symbol[
        Optional[list[int]],
        None,
    ]

    ApplyAquaRingHealing: Symbol[
        Optional[list[int]],
        None,
    ]

    TryInflictAquaRingStatus: Symbol[
        Optional[list[int]],
        None,
    ]

    TryInflictLuckyChantStatus: Symbol[
        Optional[list[int]],
        None,
    ]

    TryInflictHealBlockStatus: Symbol[
        Optional[list[int]],
        None,
    ]

    MonsterHasEmbargoStatus: Symbol[
        Optional[list[int]],
        None,
    ]

    LogItemBlockedByEmbargo: Symbol[
        Optional[list[int]],
        None,
    ]

    TryInflictEmbargoStatus: Symbol[
        Optional[list[int]],
        None,
    ]

    TryInflictMiracleEyeStatus: Symbol[
        Optional[list[int]],
        None,
    ]

    TryInflictMagnetRiseStatus: Symbol[
        Optional[list[int]],
        None,
    ]

    IsFloating: Symbol[
        Optional[list[int]],
        None,
    ]

    SetTwoTurnInvincibility: Symbol[
        Optional[list[int]],
        None,
    ]

    SetReflectStatus: Symbol[
        Optional[list[int]],
        None,
    ]

    TryInflictSafeguardStatus: Symbol[
        Optional[list[int]],
        None,
    ]

    TryInflictMistStatus: Symbol[
        Optional[list[int]],
        None,
    ]

    TryInflictWishStatus: Symbol[
        Optional[list[int]],
        None,
    ]

    TryInflictMagicCoatStatus: Symbol[
        Optional[list[int]],
        None,
    ]

    TryInflictLightScreenStatus: Symbol[
        Optional[list[int]],
        None,
    ]

    TryInflictReflectStatus: Symbol[
        Optional[list[int]],
        None,
    ]

    TryInflictProtectStatus: Symbol[
        Optional[list[int]],
        None,
    ]

    TryInflictMirrorCoatStatus: Symbol[
        Optional[list[int]],
        None,
    ]

    TryInflictEndureStatus: Symbol[
        Optional[list[int]],
        None,
    ]

    TryInflictMirrorMoveStatus: Symbol[
        Optional[list[int]],
        None,
    ]

    TryInflictConversion2Status: Symbol[
        Optional[list[int]],
        None,
    ]

    TryInflictVitalThrowStatus: Symbol[
        Optional[list[int]],
        None,
    ]

    TryResetStatChanges: Symbol[
        Optional[list[int]],
        None,
    ]

    MirrorMoveIsActive: Symbol[
        Optional[list[int]],
        None,
    ]

    MistIsActive: Symbol[
        Optional[list[int]],
        None,
    ]

    Conversion2IsActive: Symbol[
        Optional[list[int]],
        None,
    ]

    ResetAiCanAttackInDirection: Symbol[
        Optional[list[int]],
        None,
    ]

    AiConsiderMove: Symbol[
        Optional[list[int]],
        None,
    ]

    TryAddTargetToAiTargetList: Symbol[
        Optional[list[int]],
        None,
    ]

    IsAiTargetEligible: Symbol[
        Optional[list[int]],
        None,
    ]

    WeightMoveWithIqSkills: Symbol[
        Optional[list[int]],
        None,
    ]

    TargetRegularAttack: Symbol[
        Optional[list[int]],
        None,
    ]

    IsTargetInRange: Symbol[
        Optional[list[int]],
        None,
    ]

    ShouldUsePp: Symbol[
        Optional[list[int]],
        None,
    ]

    GetEntityMoveTargetAndRange: Symbol[
        Optional[list[int]],
        None,
    ]

    GetEntityNaturalGiftInfo: Symbol[
        Optional[list[int]],
        None,
    ]

    GetEntityWeatherBallType: Symbol[
        Optional[list[int]],
        None,
    ]

    UseMoveByMoveId: Symbol[
        Optional[list[int]],
        None,
    ]

    ActivateMotorDrive: Symbol[
        Optional[list[int]],
        None,
    ]

    TryActivateFrisk: Symbol[
        Optional[list[int]],
        None,
    ]

    TryActivateBadDreams: Symbol[
        Optional[list[int]],
        None,
    ]

    ActivateStench: Symbol[
        Optional[list[int]],
        None,
    ]

    TryActivateSteadfast: Symbol[
        Optional[list[int]],
        None,
    ]

    IsInSpawnList: Symbol[
        Optional[list[int]],
        None,
    ]

    ChangeShayminForme: Symbol[
        Optional[list[int]],
        None,
    ]

    ApplyItemEffect: Symbol[
        Optional[list[int]],
        None,
    ]

    ApplyCheriBerryEffect: Symbol[
        Optional[list[int]],
        None,
    ]

    ApplyPechaBerryEffect: Symbol[
        Optional[list[int]],
        None,
    ]

    ApplyRawstBerryEffect: Symbol[
        Optional[list[int]],
        None,
    ]

    ApplyHungerSeedEffect: Symbol[
        Optional[list[int]],
        None,
    ]

    ApplyVileSeedEffect: Symbol[
        Optional[list[int]],
        None,
    ]

    ApplyViolentSeedEffect: Symbol[
        Optional[list[int]],
        None,
    ]

    ApplyGinsengEffect: Symbol[
        Optional[list[int]],
        None,
    ]

    ApplyBlastSeedEffect: Symbol[
        Optional[list[int]],
        None,
    ]

    ApplyGummiBoostsDungeonMode: Symbol[
        Optional[list[int]],
        None,
    ]

    CanMonsterUseItem: Symbol[
        Optional[list[int]],
        None,
    ]

    ApplyGrimyFoodEffect: Symbol[
        Optional[list[int]],
        None,
    ]

    ApplyMixElixirEffect: Symbol[
        Optional[list[int]],
        None,
    ]

    ApplyDoughSeedEffect: Symbol[
        Optional[list[int]],
        None,
    ]

    ApplyViaSeedEffect: Symbol[
        Optional[list[int]],
        None,
    ]

    ApplyGravelyrockEffect: Symbol[
        Optional[list[int]],
        None,
    ]

    ApplyGonePebbleEffect: Symbol[
        Optional[list[int]],
        None,
    ]

    ApplyGracideaEffect: Symbol[
        Optional[list[int]],
        None,
    ]

    GetAiUseItemProbability: Symbol[
        Optional[list[int]],
        None,
    ]

    IsAdjacentToEnemy: Symbol[
        Optional[list[int]],
        None,
    ]

    ShouldTryEatItem: Symbol[
        Optional[list[int]],
        None,
    ]

    GetMaxPpWrapper: Symbol[
        Optional[list[int]],
        None,
    ]

    InitMoveWrapper: Symbol[
        Optional[list[int]],
        None,
    ]

    MoveIsNotPhysical: Symbol[
        Optional[list[int]],
        None,
    ]

    CategoryIsNotPhysical: Symbol[
        Optional[list[int]],
        None,
    ]

    MakeFloorOneRoom: Symbol[
        Optional[list[int]],
        None,
    ]

    TryHurl: Symbol[
        Optional[list[int]],
        None,
    ]

    TryDrought: Symbol[
        Optional[list[int]],
        None,
    ]

    TryTrawl: Symbol[
        Optional[list[int]],
        None,
    ]

    TryPounce: Symbol[
        Optional[list[int]],
        None,
    ]

    TryBlowAway: Symbol[
        Optional[list[int]],
        None,
    ]

    TryExplosion: Symbol[
        Optional[list[int]],
        None,
    ]

    TryAftermathExplosion: Symbol[
        Optional[list[int]],
        None,
    ]

    TryWarp: Symbol[
        Optional[list[int]],
        None,
    ]

    EnsureCanStandCurrentTile: Symbol[
        Optional[list[int]],
        None,
    ]

    UseMove: Symbol[
        Optional[list[int]],
        None,
    ]

    TryActivateNondamagingDefenderAbility: Symbol[
        Optional[list[int]],
        None,
    ]

    TryActivateNondamagingDefenderExclusiveItem: Symbol[
        Optional[list[int]],
        None,
    ]

    GetMoveRangeDistance: Symbol[
        Optional[list[int]],
        None,
    ]

    MoveHitCheck: Symbol[
        Optional[list[int]],
        None,
    ]

    BuildMoveTargetList: Symbol[
        Optional[list[int]],
        None,
    ]

    IsHyperBeamVariant: Symbol[
        Optional[list[int]],
        None,
    ]

    IsChargingTwoTurnMove: Symbol[
        Optional[list[int]],
        None,
    ]

    IsChargingAnyTwoTurnMove: Symbol[
        Optional[list[int]],
        None,
    ]

    HasMaxGinsengBoost99: Symbol[
        Optional[list[int]],
        None,
    ]

    TwoTurnMoveForcedMiss: Symbol[
        Optional[list[int]],
        None,
    ]

    DungeonRandOutcomeUserTargetInteraction: Symbol[
        Optional[list[int]],
        None,
    ]

    DungeonRandOutcomeUserAction: Symbol[
        Optional[list[int]],
        None,
    ]

    CanAiUseMove: Symbol[
        Optional[list[int]],
        None,
    ]

    CanMonsterUseMove: Symbol[
        Optional[list[int]],
        None,
    ]

    UpdateMovePp: Symbol[
        Optional[list[int]],
        None,
    ]

    GetDamageSourceWrapper: Symbol[
        Optional[list[int]],
        None,
    ]

    LowerSshort: Symbol[
        Optional[list[int]],
        None,
    ]

    PlayMoveAnimation: Symbol[
        Optional[list[int]],
        None,
    ]

    GetMoveAnimationId: Symbol[
        Optional[list[int]],
        None,
    ]

    ShouldMovePlayAlternativeAnimation: Symbol[
        Optional[list[int]],
        None,
    ]

    ExecuteMoveEffect: Symbol[
        Optional[list[int]],
        None,
    ]

    DoMoveDamageInlined: Symbol[
        Optional[list[int]],
        None,
    ]

    DealDamage: Symbol[
        Optional[list[int]],
        None,
    ]

    DealDamageWithTypeAndPowerBoost: Symbol[
        Optional[list[int]],
        None,
    ]

    DealDamageProjectile: Symbol[
        Optional[list[int]],
        None,
    ]

    DealDamageWithType: Symbol[
        Optional[list[int]],
        None,
    ]

    PerformDamageSequence: Symbol[
        Optional[list[int]],
        None,
    ]

    CanHitWithRegularAttack: Symbol[
        Optional[list[int]],
        None,
    ]

    StatusCheckerCheck: Symbol[
        Optional[list[int]],
        None,
    ]

    StatusCheckerCheckOnTarget: Symbol[
        Optional[list[int]],
        None,
    ]

    HasLastUsedMove: Symbol[
        Optional[list[int]],
        None,
    ]

    GetApparentWeather: Symbol[
        Optional[list[int]],
        None,
    ]

    TryWeatherFormChange: Symbol[
        Optional[list[int]],
        None,
    ]

    ActivateSportCondition: Symbol[
        Optional[list[int]],
        None,
    ]

    TryActivateWeather: Symbol[
        Optional[list[int]],
        None,
    ]

    DigitCount: Symbol[
        Optional[list[int]],
        None,
    ]

    LoadTextureUi: Symbol[
        Optional[list[int]],
        None,
    ]

    GetPaletteBaseAddress: Symbol[
        Optional[list[int]],
        None,
    ]

    DisplayNumberTextureUi: Symbol[
        Optional[list[int]],
        None,
    ]

    DisplayCharTextureUi: Symbol[
        Optional[list[int]],
        None,
    ]

    DisplayUi: Symbol[
        Optional[list[int]],
        None,
    ]

    GetTile: Symbol[
        Optional[list[int]],
        None,
    ]

    GetTileSafe: Symbol[
        Optional[list[int]],
        None,
    ]

    IsFullFloorFixedRoom: Symbol[
        Optional[list[int]],
        None,
    ]

    IsCurrentTilesetBackground: Symbol[
        Optional[list[int]],
        None,
    ]

    TrySpawnGoldenChamber: Symbol[
        Optional[list[int]],
        None,
    ]

    CountItemsOnFloorForAcuteSniffer: Symbol[
        Optional[list[int]],
        None,
    ]

    GetStairsSpawnPosition: Symbol[
        Optional[list[int]],
        None,
    ]

    PositionIsOnStairs: Symbol[
        Optional[list[int]],
        None,
    ]

    GetStairsRoom: Symbol[
        Optional[list[int]],
        None,
    ]

    GetDefaultTileTextureId: Symbol[
        Optional[list[int]],
        None,
    ]

    DetermineAllTilesWalkableNeighbors: Symbol[
        Optional[list[int]],
        None,
    ]

    DetermineTileWalkableNeighbors: Symbol[
        Optional[list[int]],
        None,
    ]

    UpdateTrapsVisibility: Symbol[
        Optional[list[int]],
        None,
    ]

    DrawTileGrid: Symbol[
        Optional[list[int]],
        None,
    ]

    HideTileGrid: Symbol[
        Optional[list[int]],
        None,
    ]

    DiscoverMinimap: Symbol[
        Optional[list[int]],
        None,
    ]

    PositionHasItem: Symbol[
        Optional[list[int]],
        None,
    ]

    PositionHasMonster: Symbol[
        Optional[list[int]],
        None,
    ]

    TrySmashWall: Symbol[
        Optional[list[int]],
        None,
    ]

    IsTileGround: Symbol[
        Optional[list[int]],
        None,
    ]

    IsWaterTileset: Symbol[
        Optional[list[int]],
        None,
    ]

    GetRandomSpawnMonsterID: Symbol[
        Optional[list[int]],
        None,
    ]

    NearbyAllyIqSkillIsEnabled: Symbol[
        Optional[list[int]],
        None,
    ]

    FindAdjacentEnemy: Symbol[
        Optional[list[int]],
        None,
    ]

    IsAdjacentToEnemyIgnoreTreatment: Symbol[
        Optional[list[int]],
        None,
    ]

    ResetGravity: Symbol[
        Optional[list[int]],
        None,
    ]

    GravityIsActive: Symbol[
        Optional[list[int]],
        None,
    ]

    TryActivateGravity: Symbol[
        Optional[list[int]],
        None,
    ]

    RevealAttackedTile: Symbol[
        Optional[list[int]],
        None,
    ]

    ResetVictoryCounter: Symbol[
        Optional[list[int]],
        None,
    ]

    ShouldBoostKecleonShopSpawnChance: Symbol[
        Optional[list[int]],
        None,
    ]

    SetShouldBoostKecleonShopSpawnChance: Symbol[
        Optional[list[int]],
        None,
    ]

    UpdateShouldBoostKecleonShopSpawnChance: Symbol[
        Optional[list[int]],
        None,
    ]

    GetDoughSeedFlag: Symbol[
        Optional[list[int]],
        None,
    ]

    SetDoughSeedFlag: Symbol[
        Optional[list[int]],
        None,
    ]

    TrySpawnDoughSeedPoke: Symbol[
        Optional[list[int]],
        None,
    ]

    IsSecretBazaar: Symbol[
        Optional[list[int]],
        None,
    ]

    ShouldBoostHiddenStairsSpawnChance: Symbol[
        Optional[list[int]],
        None,
    ]

    SetShouldBoostHiddenStairsSpawnChance: Symbol[
        Optional[list[int]],
        None,
    ]

    UpdateShouldBoostHiddenStairsSpawnChance: Symbol[
        Optional[list[int]],
        None,
    ]

    IsSecretRoom: Symbol[
        Optional[list[int]],
        None,
    ]

    IsSecretFloor: Symbol[
        Optional[list[int]],
        None,
    ]

    GetCurrentHiddenStairsType: Symbol[
        Optional[list[int]],
        None,
    ]

    HiddenStairsPresent: Symbol[
        Optional[list[int]],
        None,
    ]

    PositionIsOnHiddenStairs: Symbol[
        Optional[list[int]],
        None,
    ]

    HiddenStairsTrigger: Symbol[
        Optional[list[int]],
        None,
    ]

    GetHiddenStairsField: Symbol[
        Optional[list[int]],
        None,
    ]

    SetHiddenStairsField: Symbol[
        Optional[list[int]],
        None,
    ]

    GetHiddenFloorField: Symbol[
        Optional[list[int]],
        None,
    ]

    SetHiddenFloorField: Symbol[
        Optional[list[int]],
        None,
    ]

    LoadWeather3DFiles: Symbol[
        Optional[list[int]],
        None,
    ]

    RenderWeather3D: Symbol[
        Optional[list[int]],
        None,
    ]

    GetMinimapData: Symbol[
        Optional[list[int]],
        None,
    ]

    DrawMinimapTile: Symbol[
        Optional[list[int]],
        None,
    ]

    FlashLeaderIcon: Symbol[
        Optional[list[int]],
        None,
    ]

    UpdateMinimap: Symbol[
        Optional[list[int]],
        None,
    ]

    SetMinimapDataE447: Symbol[
        Optional[list[int]],
        None,
    ]

    GetMinimapDataE447: Symbol[
        Optional[list[int]],
        None,
    ]

    SetMinimapDataE448: Symbol[
        Optional[list[int]],
        None,
    ]

    InitWeirdMinimapMatrix: Symbol[
        Optional[list[int]],
        None,
    ]

    InitMinimapDisplayTile: Symbol[
        Optional[list[int]],
        None,
    ]

    LoadFixedRoomDataVeneer: Symbol[
        Optional[list[int]],
        None,
    ]

    UnloadFixedRoomData: Symbol[
        Optional[list[int]],
        None,
    ]

    IsNormalFloor: Symbol[
        Optional[list[int]],
        None,
    ]

    GenerateFloor: Symbol[
        Optional[list[int]],
        None,
    ]

    GetTileTerrain: Symbol[
        Optional[list[int]],
        None,
    ]

    DungeonRand100: Symbol[
        Optional[list[int]],
        None,
    ]

    ClearHiddenStairs: Symbol[
        Optional[list[int]],
        None,
    ]

    FlagHallwayJunctions: Symbol[
        Optional[list[int]],
        None,
    ]

    GenerateStandardFloor: Symbol[
        Optional[list[int]],
        None,
    ]

    GenerateOuterRingFloor: Symbol[
        Optional[list[int]],
        None,
    ]

    GenerateCrossroadsFloor: Symbol[
        Optional[list[int]],
        None,
    ]

    GenerateLineFloor: Symbol[
        Optional[list[int]],
        None,
    ]

    GenerateCrossFloor: Symbol[
        Optional[list[int]],
        None,
    ]

    GenerateBeetleFloor: Symbol[
        Optional[list[int]],
        None,
    ]

    MergeRoomsVertically: Symbol[
        Optional[list[int]],
        None,
    ]

    GenerateOuterRoomsFloor: Symbol[
        Optional[list[int]],
        None,
    ]

    IsNotFullFloorFixedRoom: Symbol[
        Optional[list[int]],
        None,
    ]

    GenerateFixedRoom: Symbol[
        Optional[list[int]],
        None,
    ]

    GenerateOneRoomMonsterHouseFloor: Symbol[
        Optional[list[int]],
        None,
    ]

    GenerateTwoRoomsWithMonsterHouseFloor: Symbol[
        Optional[list[int]],
        None,
    ]

    GenerateExtraHallways: Symbol[
        Optional[list[int]],
        None,
    ]

    GetGridPositions: Symbol[
        Optional[list[int]],
        None,
    ]

    InitDungeonGrid: Symbol[
        Optional[list[int]],
        None,
    ]

    AssignRooms: Symbol[
        Optional[list[int]],
        None,
    ]

    CreateRoomsAndAnchors: Symbol[
        Optional[list[int]],
        None,
    ]

    GenerateSecondaryStructures: Symbol[
        Optional[list[int]],
        None,
    ]

    AssignGridCellConnections: Symbol[
        Optional[list[int]],
        None,
    ]

    CreateGridCellConnections: Symbol[
        Optional[list[int]],
        None,
    ]

    GenerateRoomImperfections: Symbol[
        Optional[list[int]],
        None,
    ]

    CreateHallway: Symbol[
        Optional[list[int]],
        None,
    ]

    EnsureConnectedGrid: Symbol[
        Optional[list[int]],
        None,
    ]

    SetTerrainObstacleChecked: Symbol[
        Optional[list[int]],
        None,
    ]

    FinalizeJunctions: Symbol[
        Optional[list[int]],
        None,
    ]

    GenerateKecleonShop: Symbol[
        Optional[list[int]],
        None,
    ]

    GenerateMonsterHouse: Symbol[
        Optional[list[int]],
        None,
    ]

    GenerateMazeRoom: Symbol[
        Optional[list[int]],
        None,
    ]

    GenerateMaze: Symbol[
        Optional[list[int]],
        None,
    ]

    GenerateMazeLine: Symbol[
        Optional[list[int]],
        None,
    ]

    SetSpawnFlag5: Symbol[
        Optional[list[int]],
        None,
    ]

    IsNextToHallway: Symbol[
        Optional[list[int]],
        None,
    ]

    ResolveInvalidSpawns: Symbol[
        Optional[list[int]],
        None,
    ]

    ConvertSecondaryTerrainToChasms: Symbol[
        Optional[list[int]],
        None,
    ]

    EnsureImpassableTilesAreWalls: Symbol[
        Optional[list[int]],
        None,
    ]

    InitializeTile: Symbol[
        Optional[list[int]],
        None,
    ]

    ResetFloor: Symbol[
        Optional[list[int]],
        None,
    ]

    PosIsOutOfBounds: Symbol[
        Optional[list[int]],
        None,
    ]

    ShuffleSpawnPositions: Symbol[
        Optional[list[int]],
        None,
    ]

    MarkNonEnemySpawns: Symbol[
        Optional[list[int]],
        None,
    ]

    MarkEnemySpawns: Symbol[
        Optional[list[int]],
        None,
    ]

    SetSecondaryTerrainOnWall: Symbol[
        Optional[list[int]],
        None,
    ]

    GenerateSecondaryTerrainFormations: Symbol[
        Optional[list[int]],
        None,
    ]

    StairsAlwaysReachable: Symbol[
        Optional[list[int]],
        None,
    ]

    GetNextFixedRoomAction: Symbol[
        Optional[list[int]],
        None,
    ]

    ConvertWallsToChasms: Symbol[
        Optional[list[int]],
        None,
    ]

    ResetInnerBoundaryTileRows: Symbol[
        Optional[list[int]],
        None,
    ]

    ResetImportantSpawnPositions: Symbol[
        Optional[list[int]],
        None,
    ]

    SpawnStairs: Symbol[
        Optional[list[int]],
        None,
    ]

    GetHiddenStairsType: Symbol[
        Optional[list[int]],
        None,
    ]

    GetFinalKecleonShopSpawnChance: Symbol[
        Optional[list[int]],
        None,
    ]

    ResetHiddenStairsSpawn: Symbol[
        Optional[list[int]],
        None,
    ]

    PlaceFixedRoomTile: Symbol[
        Optional[list[int]],
        None,
    ]

    FixedRoomActionParamToDirection: Symbol[
        Optional[list[int]],
        None,
    ]

    ApplyKeyEffect: Symbol[
        Optional[list[int]],
        None,
    ]

    LoadFixedRoomData: Symbol[
        Optional[list[int]],
        None,
    ]

    LoadFixedRoom: Symbol[
        Optional[list[int]],
        None,
    ]

    OpenFixedBin: Symbol[
        Optional[list[int]],
        None,
    ]

    CloseFixedBin: Symbol[
        Optional[list[int]],
        None,
    ]

    AreOrbsAllowed: Symbol[
        Optional[list[int]],
        None,
    ]

    AreTileJumpsAllowed: Symbol[
        Optional[list[int]],
        None,
    ]

    AreTrawlOrbsAllowed: Symbol[
        Optional[list[int]],
        None,
    ]

    AreOrbsAllowedVeneer: Symbol[
        Optional[list[int]],
        None,
    ]

    AreLateGameTrapsEnabled: Symbol[
        Optional[list[int]],
        None,
    ]

    AreMovesEnabled: Symbol[
        Optional[list[int]],
        None,
    ]

    IsRoomIlluminated: Symbol[
        Optional[list[int]],
        None,
    ]

    GetMatchingMonsterId: Symbol[
        Optional[list[int]],
        None,
    ]

    GenerateItemExplicit: Symbol[
        Optional[list[int]],
        None,
    ]

    GenerateAndSpawnItem: Symbol[
        Optional[list[int]],
        None,
    ]

    IsHiddenStairsFloor: Symbol[
        Optional[list[int]],
        None,
    ]

    IsSecretBazaarVeneer: Symbol[
        Optional[list[int]],
        None,
    ]

    PrepareItemForPrinting: Symbol[
        Optional[list[int]],
        None,
    ]

    PrepareItemForPrinting2: Symbol[
        Optional[list[int]],
        None,
    ]

    GenerateStandardItem: Symbol[
        Optional[list[int]],
        None,
    ]

    GenerateCleanItem: Symbol[
        Optional[list[int]],
        None,
    ]

    TryLeaderItemPickUp: Symbol[
        Optional[list[int]],
        None,
    ]

    SpawnItem: Symbol[
        Optional[list[int]],
        None,
    ]

    RemoveGroundItem: Symbol[
        Optional[list[int]],
        None,
    ]

    SpawnDroppedItemWrapper: Symbol[
        Optional[list[int]],
        None,
    ]

    SpawnDroppedItem: Symbol[
        Optional[list[int]],
        None,
    ]

    TryGenerateUnownStoneDrop: Symbol[
        Optional[list[int]],
        None,
    ]

    HasHeldItem: Symbol[
        Optional[list[int]],
        None,
    ]

    GenerateMoneyQuantity: Symbol[
        Optional[list[int]],
        None,
    ]

    CheckTeamItemsFlags: Symbol[
        Optional[list[int]],
        None,
    ]

    AddHeldItemToBag: Symbol[
        Optional[list[int]],
        None,
    ]

    RemoveEmptyItemsInBagWrapper: Symbol[
        Optional[list[int]],
        None,
    ]

    GenerateItem: Symbol[
        Optional[list[int]],
        None,
    ]

    HandleCurvedProjectileThrow: Symbol[
        Optional[list[int]],
        None,
    ]

    DoesProjectileHitTarget: Symbol[
        Optional[list[int]],
        None,
    ]

    DisplayFloorCard: Symbol[
        Optional[list[int]],
        None,
    ]

    HandleFloorCard: Symbol[
        Optional[list[int]],
        None,
    ]

    FillMissionDestinationInfo: Symbol[
        Optional[list[int]],
        None,
    ]

    IsItemUnkMissionItem2: Symbol[
        Optional[list[int]],
        None,
    ]

    CheckActiveChallengeRequest: Symbol[
        Optional[list[int]],
        None,
    ]

    GetMissionDestination: Symbol[
        Optional[list[int]],
        None,
    ]

    IsOutlawOrChallengeRequestFloor: Symbol[
        Optional[list[int]],
        None,
    ]

    IsDestinationFloor: Symbol[
        Optional[list[int]],
        None,
    ]

    IsCurrentMissionType: Symbol[
        Optional[list[int]],
        None,
    ]

    IsCurrentMissionTypeExact: Symbol[
        Optional[list[int]],
        None,
    ]

    IsOutlawMonsterHouseFloor: Symbol[
        Optional[list[int]],
        None,
    ]

    IsGoldenChamber: Symbol[
        Optional[list[int]],
        None,
    ]

    IsLegendaryChallengeFloor: Symbol[
        Optional[list[int]],
        None,
    ]

    IsJirachiChallengeFloor: Symbol[
        Optional[list[int]],
        None,
    ]

    IsDestinationFloorWithMonster: Symbol[
        Optional[list[int]],
        None,
    ]

    LoadMissionMonsterSprites: Symbol[
        Optional[list[int]],
        None,
    ]

    MissionTargetEnemyIsDefeated: Symbol[
        Optional[list[int]],
        None,
    ]

    SetMissionTargetEnemyDefeated: Symbol[
        Optional[list[int]],
        None,
    ]

    IsDestinationFloorWithFixedRoom: Symbol[
        Optional[list[int]],
        None,
    ]

    GetItemToRetrieve: Symbol[
        Optional[list[int]],
        None,
    ]

    GetItemToDeliver: Symbol[
        Optional[list[int]],
        None,
    ]

    GetSpecialTargetItem: Symbol[
        Optional[list[int]],
        None,
    ]

    IsDestinationFloorWithItem: Symbol[
        Optional[list[int]],
        None,
    ]

    IsDestinationFloorWithHiddenOutlaw: Symbol[
        Optional[list[int]],
        None,
    ]

    IsDestinationFloorWithFleeingOutlaw: Symbol[
        Optional[list[int]],
        None,
    ]

    GetMissionTargetEnemy: Symbol[
        Optional[list[int]],
        None,
    ]

    GetMissionEnemyMinionGroup: Symbol[
        Optional[list[int]],
        None,
    ]

    SetTargetMonsterNotFoundFlag: Symbol[
        Optional[list[int]],
        None,
    ]

    GetTargetMonsterNotFoundFlag: Symbol[
        Optional[list[int]],
        None,
    ]

    FloorHasMissionMonster: Symbol[
        Optional[list[int]],
        None,
    ]

    GetMissionIfActiveOnFloor: Symbol[
        Optional[list[int]],
        None,
    ]

    GenerateMissionEggMonster: Symbol[
        Optional[list[int]],
        None,
    ]

    GetFirstExperienceLockedTeamMember: Symbol[
        Optional[list[int]],
        None,
    ]

    TeleportFleeingOutlaw: Symbol[
        Optional[list[int]],
        None,
    ]

    InitAlertBoxInfo: Symbol[
        Optional[list[int]],
        None,
    ]

    FreeAlertBoxInfo: Symbol[
        Optional[list[int]],
        None,
    ]

    SetMessageLogGroupStartFlag: Symbol[
        Optional[list[int]],
        None,
    ]

    GetMessageLogPreprocessorArgs: Symbol[
        Optional[list[int]],
        None,
    ]

    InitMessageLogPreprocessorArgs: Symbol[
        Optional[list[int]],
        None,
    ]

    SetMessageLogPreprocessorArgsFlagVal: Symbol[
        Optional[list[int]],
        None,
    ]

    SetMessageLogPreprocessorArgsIdVal: Symbol[
        Optional[list[int]],
        None,
    ]

    SetMessageLogPreprocessorArgsNumberVal: Symbol[
        Optional[list[int]],
        None,
    ]

    SetMessageLogPreprocessorArgsString: Symbol[
        Optional[list[int]],
        None,
    ]

    SetMessageLogPreprocessorArgsStringToName: Symbol[
        Optional[list[int]],
        None,
    ]

    SetMessageLogPreprocessorArgsSpeakerId: Symbol[
        Optional[list[int]],
        None,
    ]

    SetMessageLogPreprocessorArgsSpeakerId0x30000: Symbol[
        Optional[list[int]],
        None,
    ]

    LogMessageByIdWithPopupAndAbility: Symbol[
        Optional[list[int]],
        None,
    ]

    WaitUntilAlertBoxTextIsLoadedWrapper: Symbol[
        Optional[list[int]],
        None,
    ]

    LogMessageByIdWithPopupCheckUser: Symbol[
        Optional[list[int]],
        None,
    ]

    LogMessageWithPopupCheckUser: Symbol[
        Optional[list[int]],
        None,
    ]

    LogMessageByIdQuiet: Symbol[
        Optional[list[int]],
        None,
    ]

    LogMessageQuiet: Symbol[
        Optional[list[int]],
        None,
    ]

    LogMessageByIdWithPopupCheckUserTarget: Symbol[
        Optional[list[int]],
        None,
    ]

    LogMessageWithPopupCheckUserTarget: Symbol[
        Optional[list[int]],
        None,
    ]

    LogMessageByIdQuietCheckUserTarget: Symbol[
        Optional[list[int]],
        None,
    ]

    LogMessageByIdWithPopupCheckUserUnknown: Symbol[
        Optional[list[int]],
        None,
    ]

    LogMessageByIdWithPopup: Symbol[
        Optional[list[int]],
        None,
    ]

    LogMessageWithPopup: Symbol[
        Optional[list[int]],
        None,
    ]

    LogMessage: Symbol[
        Optional[list[int]],
        None,
    ]

    LogMessageById: Symbol[
        Optional[list[int]],
        None,
    ]

    AlertBoxIsScrolling: Symbol[
        Optional[list[int]],
        None,
    ]

    WaitUntilAlertBoxTextIsLoaded: Symbol[
        Optional[list[int]],
        None,
    ]

    InitPortraitDungeon: Symbol[
        Optional[list[int]],
        None,
    ]

    OpenMessageLog: Symbol[
        Optional[list[int]],
        None,
    ]

    RunDungeonMode: Symbol[
        Optional[list[int]],
        None,
    ]

    StartFadeDungeon: Symbol[
        Optional[list[int]],
        None,
    ]

    StartFadeDungeonWrapper: Symbol[
        Optional[list[int]],
        None,
    ]

    HandleFadesDungeon: Symbol[
        Optional[list[int]],
        None,
    ]

    HandleFadesDungeonBothScreens: Symbol[
        Optional[list[int]],
        None,
    ]

    DisplayFloorTip: Symbol[
        Optional[list[int]],
        None,
    ]

    DisplayItemTip: Symbol[
        Optional[list[int]],
        None,
    ]

    DisplayDungeonTip: Symbol[
        Optional[list[int]],
        None,
    ]

    SetBothScreensWindowColorToDefault: Symbol[
        Optional[list[int]],
        None,
    ]

    GetPersonalityIndex: Symbol[
        Optional[list[int]],
        None,
    ]

    DisplayMessage: Symbol[
        Optional[list[int]],
        None,
    ]

    DisplayMessage2: Symbol[
        Optional[list[int]],
        None,
    ]

    YesNoMenu: Symbol[
        Optional[list[int]],
        None,
    ]

    DisplayMessageInternal: Symbol[
        Optional[list[int]],
        None,
    ]

    InitSecretBazaarDialogueInfo: Symbol[
        Optional[list[int]],
        None,
    ]

    OpenMenu: Symbol[
        Optional[list[int]],
        None,
    ]

    StairsMenuAfterStep: Symbol[
        Optional[list[int]],
        None,
    ]

    DungeonModeSetupAndShowNameKeyboard: Symbol[
        Optional[list[int]],
        None,
    ]

    OthersMenuLoop: Symbol[
        Optional[list[int]],
        None,
    ]

    OthersMenu: Symbol[
        Optional[list[int]],
        None,
    ]


class Overlay29DataProtocol(Protocol):

    DUNGEON_STRUCT_SIZE: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    MAX_HP_CAP: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    OFFSET_OF_DUNGEON_FLOOR_PROPERTIES: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    SPAWN_RAND_MAX: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    DUNGEON_PRNG_LCG_MULTIPLIER: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    DUNGEON_PRNG_LCG_INCREMENT_SECONDARY: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    ATTACK_SPRITE_BUFFER_SIZE: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    KECLEON_FEMALE_ID: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    KECLEON_MALE_ID: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    MSG_ID_SLOW_START: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    EXPERIENCE_POINT_GAIN_CAP: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    JUDGMENT_MOVE_ID: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    REGULAR_ATTACK_MOVE_ID: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    DEOXYS_ATTACK_ID: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    DEOXYS_SPEED_ID: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    GIRATINA_ALTERED_ID: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    PUNISHMENT_MOVE_ID: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    OFFENSE_STAT_MAX: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    PROJECTILE_MOVE_ID: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    BELLY_LOST_PER_TURN: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    MONSTER_HEAL_HP_MAX: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    MOVE_TARGET_AND_RANGE_SPECIAL_USER_HEALING: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    PLAIN_SEED_STRING_ID: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    MAX_ELIXIR_PP_RESTORATION: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    SLIP_SEED_FAIL_STRING_ID: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    ROCK_WRECKER_MOVE_ID: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    CASTFORM_NORMAL_FORM_MALE_ID: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    CASTFORM_NORMAL_FORM_FEMALE_ID: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    CHERRIM_SUNSHINE_FORM_MALE_ID: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    CHERRIM_OVERCAST_FORM_FEMALE_ID: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    CHERRIM_SUNSHINE_FORM_FEMALE_ID: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    FLOOR_GENERATION_STATUS_PTR: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    OFFSET_OF_DUNGEON_N_NORMAL_ITEM_SPAWNS: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    DUNGEON_GRID_COLUMN_BYTES: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    DEFAULT_MAX_POSITION: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    OFFSET_OF_DUNGEON_GUARANTEED_ITEM_ID: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    FIXED_ROOM_TILE_SPAWN_TABLE: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    TREASURE_BOX_1_ITEM_IDS: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    FIXED_ROOM_REVISIT_OVERRIDES: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    FIXED_ROOM_MONSTER_SPAWN_TABLE: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    FIXED_ROOM_ITEM_SPAWN_TABLE: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    FIXED_ROOM_ENTITY_SPAWN_TABLE: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    STATUS_ICON_ARRAY_MUZZLED: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    STATUS_ICON_ARRAY_MAGNET_RISE: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    STATUS_ICON_ARRAY_MIRACLE_EYE: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    STATUS_ICON_ARRAY_LEECH_SEED: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    STATUS_ICON_ARRAY_LONG_TOSS: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    STATUS_ICON_ARRAY_BLINDED: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    STATUS_ICON_ARRAY_BURN: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    STATUS_ICON_ARRAY_SURE_SHOT: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    STATUS_ICON_ARRAY_INVISIBLE: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    STATUS_ICON_ARRAY_SLEEP: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    STATUS_ICON_ARRAY_CURSE: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    STATUS_ICON_ARRAY_FREEZE: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    STATUS_ICON_ARRAY_CRINGE: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    STATUS_ICON_ARRAY_BIDE: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    STATUS_ICON_ARRAY_REFLECT: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    POSITION_DISPLACEMENT_TO_DIRECTION: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    DIRECTIONS_XY: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    FACING_DIRECTION_INCREMENTS: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    DISPLACEMENTS_WITHIN_2_LARGEST_FIRST: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    DISPLACEMENTS_WITHIN_2_SMALLEST_FIRST: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    DISPLACEMENTS_WITHIN_3: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    ITEM_CATEGORY_ACTIONS: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    FRACTIONAL_TURN_SEQUENCE: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    BELLY_DRAIN_IN_WALLS_INT: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    BELLY_DRAIN_IN_WALLS_THOUSANDTHS: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    DIRECTIONAL_BIT_MASKS: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    MONSTER_TREATMENT_DATA: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    DAMAGE_MULTIPLIER_0_5: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    DAMAGE_MULTIPLIER_1_5: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    DAMAGE_MULTIPLIER_2: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    CLOUDY_DAMAGE_MULTIPLIER: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    SOLID_ROCK_MULTIPLIER: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    DAMAGE_FORMULA_MAX_BASE: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    WONDER_GUARD_MULTIPLIER: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    DAMAGE_FORMULA_MIN_BASE: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    WEAK_TYPE_PICKER_MATCHUP_MULTIPLIERS: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    TYPE_DAMAGE_NEGATING_EXCLUSIVE_ITEM_EFFECTS: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    TWO_TURN_STATUSES: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    TWO_TURN_MOVES_AND_STATUSES: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    SPATK_STAT_IDX: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    ATK_STAT_IDX: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    ROLLOUT_DAMAGE_MULT_TABLE: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    MAP_COLOR_TABLE: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    CORNER_CARDINAL_NEIGHBOR_IS_OPEN: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    GUMMI_LIKE_STRING_IDS: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    GUMMI_IQ_STRING_IDS: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    DAMAGE_STRING_IDS: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    OV29_STATIC_INITIALIZER: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    DUNGEON_PTR: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    DUNGEON_PTR_MASTER: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    TOP_SCREEN_STATUS_PTR: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    LEADER_PTR: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    DUNGEON_PRNG_STATE: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    DUNGEON_PRNG_STATE_SECONDARY_VALUES: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    LOADED_ATTACK_SPRITE_FILE_INDEX: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    LOADED_ATTACK_SPRITE_PACK_ID: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    EXCL_ITEM_EFFECTS_WEATHER_ATK_SPEED_BOOST: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    EXCL_ITEM_EFFECTS_WEATHER_MOVE_SPEED_BOOST: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    EXCL_ITEM_EFFECTS_WEATHER_NO_STATUS: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    AI_THROWN_ITEM_ACTION_CHOICE_COUNT: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    EXCL_ITEM_EFFECTS_EVASION_BOOST: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    DEFAULT_TILE: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    HIDDEN_STAIRS_SPAWN_BLOCKED: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    FIXED_ROOM_DATA_PTR: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    MESSAGE_LOG_INFO: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    DUNGEON_FADES_PTR: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    VISIBLE_TRAP_FAIL_CHANCE: Symbol[
        Optional[list[int]],
        None,
    ]

    HIDDEN_TRAP_FAIL_CHANCE: Symbol[
        Optional[list[int]],
        None,
    ]

    NECTAR_IQ_BOOST: Symbol[
        Optional[list[int]],
        None,
    ]

    COMPRESSED_SPRITE_BUFFER_SIZE: Symbol[
        Optional[list[int]],
        None,
    ]


Overlay29Protocol = SectionProtocol[
    Overlay29FunctionsProtocol,
    Overlay29DataProtocol,
    Optional[int],
]


class Overlay3FunctionsProtocol(Protocol):

    pass


class Overlay3DataProtocol(Protocol):

    OV3_STATIC_INITIALIZER: Symbol[
        Optional[list[int]],
        Optional[int],
    ]


Overlay3Protocol = SectionProtocol[
    Overlay3FunctionsProtocol,
    Overlay3DataProtocol,
    Optional[int],
]


class Overlay30FunctionsProtocol(Protocol):

    WriteQuicksaveData: Symbol[
        Optional[list[int]],
        None,
    ]


class Overlay30DataProtocol(Protocol):

    OVERLAY30_JP_STRING_1: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    OVERLAY30_JP_STRING_2: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    OV30_STATIC_INITIALIZER: Symbol[
        Optional[list[int]],
        Optional[int],
    ]


Overlay30Protocol = SectionProtocol[
    Overlay30FunctionsProtocol,
    Overlay30DataProtocol,
    Optional[int],
]


class Overlay31FunctionsProtocol(Protocol):

    InitDungeonMenu: Symbol[
        Optional[list[int]],
        None,
    ]

    DrawDungeonMenuStatusWindow: Symbol[
        Optional[list[int]],
        None,
    ]

    DungeonMenuSwitch: Symbol[
        Optional[list[int]],
        None,
    ]

    DungeonMenuLoop: Symbol[
        Optional[list[int]],
        None,
    ]

    FreeDungeonMenu: Symbol[
        Optional[list[int]],
        None,
    ]

    StairsMenu: Symbol[
        Optional[list[int]],
        None,
    ]

    InitStairsMenu: Symbol[
        Optional[list[int]],
        None,
    ]

    StairsSubheadingCallback: Symbol[
        Optional[list[int]],
        None,
    ]

    StairsMenuLoop: Symbol[
        Optional[list[int]],
        None,
    ]

    CloseMainStairsMenu: Symbol[
        Optional[list[int]],
        None,
    ]

    FreeStairsMenu: Symbol[
        Optional[list[int]],
        None,
    ]

    EntityIsValidOverlay31: Symbol[
        Optional[list[int]],
        None,
    ]

    ItemsMenu: Symbol[
        Optional[list[int]],
        None,
    ]

    MovesMenu: Symbol[
        Optional[list[int]],
        None,
    ]

    HandleMovesMenuWrapper0: Symbol[
        Optional[list[int]],
        None,
    ]

    HandleMovesMenuWrapper1: Symbol[
        Optional[list[int]],
        None,
    ]

    HandleMovesMenu: Symbol[
        Optional[list[int]],
        None,
    ]

    TeamMenu: Symbol[
        Optional[list[int]],
        None,
    ]

    RestMenu: Symbol[
        Optional[list[int]],
        None,
    ]

    RecruitmentSearchMenuLoop: Symbol[
        Optional[list[int]],
        None,
    ]

    DrawDungeonHintContents: Symbol[
        Optional[list[int]],
        None,
    ]

    HelpMenuLoop: Symbol[
        Optional[list[int]],
        None,
    ]


class Overlay31DataProtocol(Protocol):

    DUNGEON_WINDOW_PARAMS_1: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    DUNGEON_WINDOW_PARAMS_2: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    DUNGEON_WINDOW_PARAMS_3: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    DUNGEON_WINDOW_PARAMS_4: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    DUNGEON_MAIN_MENU_ITEMS: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    DUNGEON_MENU_SWITCH_STR1: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    OVERLAY31_UNKNOWN_STRING_IDS: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    OVERLAY31_UNKNOWN_STRUCT__NA_2389E30: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    DUNGEON_WINDOW_PARAMS_5: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    DUNGEON_WINDOW_PARAMS_6: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    DUNGEON_WINDOW_PARAMS_7: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    STAIRS_MENU_ITEMS_NORMAL: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    STAIRS_MENU_ITEMS_WARP_ZONE: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    STAIRS_MENU_ITEMS_RESCUE_POINT: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    STAIRS_MENU_ITEMS_HIDDEN_STAIRS: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    OVERLAY31_UNKNOWN_STRUCT__NA_2389EF0: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    DUNGEON_WINDOW_PARAMS_8: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    DUNGEON_WINDOW_PARAMS_9: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    DUNGEON_WINDOW_PARAMS_10: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    DUNGEON_WINDOW_PARAMS_11: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    DUNGEON_WINDOW_PARAMS_12: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    DUNGEON_WINDOW_PARAMS_13: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    OVERLAY31_JP_STRING: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    DUNGEON_WINDOW_PARAMS_14: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    DUNGEON_WINDOW_PARAMS_15: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    DUNGEON_WINDOW_PARAMS_16: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    DUNGEON_WINDOW_PARAMS_17: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    DUNGEON_WINDOW_PARAMS_18: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    DUNGEON_WINDOW_PARAMS_19: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    OVERLAY31_UNKNOWN_STRUCT__NA_2389FE8: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    DUNGEON_WINDOW_PARAMS_20: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    DUNGEON_WINDOW_PARAMS_21: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    DUNGEON_WINDOW_PARAMS_22: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    DUNGEON_WINDOW_PARAMS_23: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    DUNGEON_WINDOW_PARAMS_24: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    DUNGEON_WINDOW_PARAMS_25: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    DUNGEON_SUBMENU_ITEMS_5: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    DUNGEON_WINDOW_PARAMS_26: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    OVERLAY31_UNKNOWN_STRUCT__NA_238A144: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    DUNGEON_WINDOW_PARAMS_27: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    DUNGEON_WINDOW_PARAMS_28: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    OVERLAY31_UNKNOWN_STRUCT__NA_238A190: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    DUNGEON_SUBMENU_ITEMS_6: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    DUNGEON_WINDOW_PARAMS_29: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    DUNGEON_WINDOW_PARAMS_30: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    DUNGEON_WINDOW_PARAMS_31: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    DUNGEON_WINDOW_PARAMS_32: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    OV31_STATIC_INITIALIZER: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    OVERLAY31_UNKNOWN_POINTER__NA_238A260: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    OVERLAY31_UNKNOWN_VALUE__NA_238A264: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    OVERLAY31_UNKNOWN_POINTER__NA_238A268: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    OVERLAY31_UNKNOWN_POINTER__NA_238A26C: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    OVERLAY31_UNKNOWN_POINTER__NA_238A270: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    OVERLAY31_UNKNOWN_POINTER__NA_238A274: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    OVERLAY31_UNKNOWN_POINTER__NA_238A278: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    OVERLAY31_UNKNOWN_POINTER__NA_238A27C: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    OVERLAY31_UNKNOWN_POINTER__NA_238A280: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    OVERLAY31_UNKNOWN_POINTER__NA_238A284: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    OVERLAY31_UNKNOWN_POINTER__NA_238A288: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    OVERLAY31_UNKNOWN_POINTER__NA_238A28C: Symbol[
        Optional[list[int]],
        Optional[int],
    ]


Overlay31Protocol = SectionProtocol[
    Overlay31FunctionsProtocol,
    Overlay31DataProtocol,
    Optional[int],
]


class Overlay32FunctionsProtocol(Protocol):

    pass


class Overlay32DataProtocol(Protocol):

    OV32_STATIC_INITIALIZER: Symbol[
        Optional[list[int]],
        Optional[int],
    ]


Overlay32Protocol = SectionProtocol[
    Overlay32FunctionsProtocol,
    Overlay32DataProtocol,
    Optional[int],
]


class Overlay33FunctionsProtocol(Protocol):

    pass


class Overlay33DataProtocol(Protocol):

    OV33_STATIC_INITIALIZER: Symbol[
        Optional[list[int]],
        Optional[int],
    ]


Overlay33Protocol = SectionProtocol[
    Overlay33FunctionsProtocol,
    Overlay33DataProtocol,
    Optional[int],
]


class Overlay34FunctionsProtocol(Protocol):

    ExplorersOfSkyMain: Symbol[
        Optional[list[int]],
        None,
    ]


class Overlay34DataProtocol(Protocol):

    OVERLAY34_UNKNOWN_STRUCT__NA_22DD014: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    START_MENU_ITEMS_CONFIRM: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    OVERLAY34_UNKNOWN_STRUCT__NA_22DD03C: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    DUNGEON_DEBUG_MENU_ITEMS: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    OV34_STATIC_INITIALIZER: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    OVERLAY34_UNKNOWN_POINTER__NA_22DD080: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    OVERLAY34_UNKNOWN_POINTER__NA_22DD084: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    OVERLAY34_UNKNOWN_POINTER__NA_22DD088: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    OVERLAY34_UNKNOWN_POINTER__NA_22DD08C: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    OVERLAY34_UNKNOWN_POINTER__NA_22DD090: Symbol[
        Optional[list[int]],
        Optional[int],
    ]


Overlay34Protocol = SectionProtocol[
    Overlay34FunctionsProtocol,
    Overlay34DataProtocol,
    Optional[int],
]


class Overlay35FunctionsProtocol(Protocol):

    pass


class Overlay35DataProtocol(Protocol):

    OV35_STATIC_INITIALIZER: Symbol[
        Optional[list[int]],
        Optional[int],
    ]


Overlay35Protocol = SectionProtocol[
    Overlay35FunctionsProtocol,
    Overlay35DataProtocol,
    Optional[int],
]


class Overlay4FunctionsProtocol(Protocol):

    pass


class Overlay4DataProtocol(Protocol):

    OV4_STATIC_INITIALIZER: Symbol[
        Optional[list[int]],
        Optional[int],
    ]


Overlay4Protocol = SectionProtocol[
    Overlay4FunctionsProtocol,
    Overlay4DataProtocol,
    Optional[int],
]


class Overlay5FunctionsProtocol(Protocol):

    pass


class Overlay5DataProtocol(Protocol):

    OV5_STATIC_INITIALIZER: Symbol[
        Optional[list[int]],
        Optional[int],
    ]


Overlay5Protocol = SectionProtocol[
    Overlay5FunctionsProtocol,
    Overlay5DataProtocol,
    Optional[int],
]


class Overlay6FunctionsProtocol(Protocol):

    pass


class Overlay6DataProtocol(Protocol):

    OV6_STATIC_INITIALIZER: Symbol[
        Optional[list[int]],
        Optional[int],
    ]


Overlay6Protocol = SectionProtocol[
    Overlay6FunctionsProtocol,
    Overlay6DataProtocol,
    Optional[int],
]


class Overlay7FunctionsProtocol(Protocol):

    pass


class Overlay7DataProtocol(Protocol):

    OV7_STATIC_INITIALIZER: Symbol[
        Optional[list[int]],
        Optional[int],
    ]


Overlay7Protocol = SectionProtocol[
    Overlay7FunctionsProtocol,
    Overlay7DataProtocol,
    Optional[int],
]


class Overlay8FunctionsProtocol(Protocol):

    pass


class Overlay8DataProtocol(Protocol):

    OV8_STATIC_INITIALIZER: Symbol[
        Optional[list[int]],
        Optional[int],
    ]


Overlay8Protocol = SectionProtocol[
    Overlay8FunctionsProtocol,
    Overlay8DataProtocol,
    Optional[int],
]


class Overlay9FunctionsProtocol(Protocol):

    CreateJukeboxTrackMenu: Symbol[
        Optional[list[int]],
        None,
    ]

    CloseJukeboxTrackMenu: Symbol[
        Optional[list[int]],
        None,
    ]

    IsJukeboxTrackMenuActive: Symbol[
        Optional[list[int]],
        None,
    ]

    UpdateJukeboxTrackMenu: Symbol[
        Optional[list[int]],
        None,
    ]

    CreatePlaybackControlsMenu: Symbol[
        Optional[list[int]],
        None,
    ]

    ClosePlaybackControlsMenu: Symbol[
        Optional[list[int]],
        None,
    ]

    IsPlaybackControlsMenuActive: Symbol[
        Optional[list[int]],
        None,
    ]

    UpdatePlaybackControlsMenu: Symbol[
        Optional[list[int]],
        None,
    ]

    CreateInputLockBox: Symbol[
        Optional[list[int]],
        None,
    ]

    CloseInputLockBox: Symbol[
        Optional[list[int]],
        None,
    ]

    IsInputLockBoxActive: Symbol[
        Optional[list[int]],
        None,
    ]

    UpdateInputLockBox: Symbol[
        Optional[list[int]],
        None,
    ]


class Overlay9DataProtocol(Protocol):

    JUKEBOX_TRACK_MENU_DEFAULT_WINDOW_PARAMS: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    PLAYBACK_CONTROLS_MENU_DEFAULT_WINDOW_PARAMS: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    INPUT_LOCK_BOX_DEFAULT_WINDOW_PARAMS: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    OV9_STATIC_INITIALIZER: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    TOP_MENU_RETURN_MUSIC_ID: Symbol[
        Optional[list[int]],
        None,
    ]


Overlay9Protocol = SectionProtocol[
    Overlay9FunctionsProtocol,
    Overlay9DataProtocol,
    Optional[int],
]


class RamFunctionsProtocol(Protocol):

    pass


class RamDataProtocol(Protocol):

    DEFAULT_MEMORY_ARENA_MEMORY: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    GROUND_MEMORY_ARENA_2: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    GROUND_MEMORY_ARENA_2_BLOCKS: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    GROUND_MEMORY_ARENA_2_MEMORY: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    DUNGEON_COLORMAP_PTR: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    DUNGEON_STRUCT: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    MOVE_DATA_TABLE: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    SOUND_MEMORY_ARENA: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    SOUND_MEMORY_ARENA_BLOCKS: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    SOUND_MEMORY_ARENA_MEMORY: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    FRAMES_SINCE_LAUNCH: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    TOUCHSCREEN_STATUS: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    BAG_ITEMS: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    BAG_ITEMS_PTR: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    STORAGE_ITEMS: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    STORAGE_ITEM_QUANTITIES: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    KECLEON_SHOP_ITEMS_PTR: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    KECLEON_SHOP_ITEMS: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    UNUSED_KECLEON_SHOP_ITEMS: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    KECLEON_WARES_ITEMS_PTR: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    KECLEON_WARES_ITEMS: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    UNUSED_KECLEON_WARES_ITEMS: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    MONEY_CARRIED: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    MONEY_STORED: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    AUDIO_COMMANDS_BUFFER: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    SOUND_MEMORY_ARENA_PTR: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    WINDOW_LIST: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    CURSOR_16_SPRITE_ID: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    CURSOR_SPRITE_ID: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    CURSOR_ANIMATION_CONTROL: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    CURSOR_16_ANIMATION_CONTROL: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    ALERT_SPRITE_ID: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    ALERT_ANIMATION_CONTROL: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    LAST_NEW_MOVE: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    OPTIONS: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    SCRIPT_VARS_VALUES: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    BAG_LEVEL: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    DEBUG_SPECIAL_EPISODE_NUMBER: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    KAOMADO_STREAM: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    PENDING_DUNGEON_ID: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    PENDING_STARTING_FLOOR: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    PLAY_TIME_SECONDS: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    PLAY_TIME_FRAME_COUNTER: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    TEAM_NAME: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    LEVEL_UP_DATA_MONSTER_ID: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    LEVEL_UP_DATA_DECOMPRESS_BUFFER: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    TEAM_MEMBER_TABLE: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    DRIVER_WORK: Symbol[
        Optional[list[int]],
        None,
    ]

    DISP_MODE: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    GXI_VRAM_LOCK_ID: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    ENABLED_VRAM_BANKS: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    SUB_BG_EXT_PLTT: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    CLR_IMG: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    THREAD_INFO_STRUCT: Symbol[
        Optional[list[int]],
        None,
    ]

    OSI_TIMER_RESERVED: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    OSI_USE_TICK: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    OSI_USE_ALARM: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    FRAMES_SINCE_LAUNCH_TIMES_THREE: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    OSI_VRAM_EXCLUSIVE: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    OSI_VRAM_LOCK_ID: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    GROUND_MEMORY_ARENA_1_PTR: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    GROUND_MEMORY_ARENA_2_PTR: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    LOCK_NOTIFY_ARRAY: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    GROUND_MEMORY_ARENA_1: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    GROUND_MEMORY_ARENA_1_BLOCKS: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    GROUND_MEMORY_ARENA_1_MEMORY: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    SENTRY_DUTY_STRUCT: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    DUNGEON_BUTTON_INPUT: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    DUNGEON_FRAMES_PASSED: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    TURNING_ON_THE_SPOT_FLAG: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    LOADED_ATTACK_SPRITE_DATA: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    MOBILITY_TYPE_TO_DUNGEON_MOBILITY_TYPE: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    AI_THROWN_ITEM_DIRECTION_IS_USED: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    AI_THROWN_ITEM_PROBABILITIES: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    AI_THROWN_ITEM_DIRECTIONS: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    AI_CAN_ATTACK_IN_DIRECTION: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    AI_POTENTIAL_ATTACK_TARGET_DIRECTIONS: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    AI_POTENTIAL_ATTACK_TARGET_WEIGHTS: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    AI_POTENTIAL_ATTACK_TARGETS: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    ROLLOUT_ICE_BALL_MISSED: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    MULTIHIT_FATIGUE_MOVE_USED: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    TWINEEDLE_HIT_TRACKER: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    RAPID_SPIN_BINDING_REMOVAL: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    ROLLOUT_ICE_BALL_SUCCESSIVE_HITS: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    MULTIHIT_MOVE_SUCCESSIVE_HITS: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    TRIPLE_KICK_SUCCESSIVE_HITS: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    METRONOME_NEXT_INDEX: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    DEFAULT_TILE_COPY: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    FLOOR_GENERATION_STATUS: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    SECRET_BAZAAR_DIALOGUE_INFO_PTR: Symbol[
        Optional[list[int]],
        Optional[int],
    ]

    STAIRS_MENU_PTR: Symbol[
        Optional[list[int]],
        Optional[int],
    ]


RamProtocol = SectionProtocol[
    RamFunctionsProtocol,
    RamDataProtocol,
    Optional[int],
]


class AllSymbolsProtocol(Protocol):

    arm7: Arm7Protocol

    arm9: Arm9Protocol

    itcm: ItcmProtocol

    libs: LibsProtocol

    move_effects: Move_effectsProtocol

    overlay0: Overlay0Protocol

    overlay1: Overlay1Protocol

    overlay10: Overlay10Protocol

    overlay11: Overlay11Protocol

    overlay12: Overlay12Protocol

    overlay13: Overlay13Protocol

    overlay14: Overlay14Protocol

    overlay15: Overlay15Protocol

    overlay16: Overlay16Protocol

    overlay17: Overlay17Protocol

    overlay18: Overlay18Protocol

    overlay19: Overlay19Protocol

    overlay2: Overlay2Protocol

    overlay20: Overlay20Protocol

    overlay21: Overlay21Protocol

    overlay22: Overlay22Protocol

    overlay23: Overlay23Protocol

    overlay24: Overlay24Protocol

    overlay25: Overlay25Protocol

    overlay26: Overlay26Protocol

    overlay27: Overlay27Protocol

    overlay28: Overlay28Protocol

    overlay29: Overlay29Protocol

    overlay3: Overlay3Protocol

    overlay30: Overlay30Protocol

    overlay31: Overlay31Protocol

    overlay32: Overlay32Protocol

    overlay33: Overlay33Protocol

    overlay34: Overlay34Protocol

    overlay35: Overlay35Protocol

    overlay4: Overlay4Protocol

    overlay5: Overlay5Protocol

    overlay6: Overlay6Protocol

    overlay7: Overlay7Protocol

    overlay8: Overlay8Protocol

    overlay9: Overlay9Protocol

    ram: RamProtocol
